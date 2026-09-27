"""Run identical seeded simulation tasks sequentially and with spawned processes."""

import argparse
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support, get_context
from statistics import median
from time import perf_counter

from process_tasks import SimulationTask, simulate_sample


def run_sequential(tasks):
    return [simulate_sample(task) for task in tasks]


def run_parallel(tasks, workers):
    # Spawn re-imports the worker module instead of copying notebook state.
    with ProcessPoolExecutor(
        max_workers=workers,
        mp_context=get_context("spawn")
    ) as pool:
        return list(pool.map(simulate_sample, tasks))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=int, default=8)
    parser.add_argument("--samples", type=int, default=50_000)
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=2)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--seed", type=int, default=404)
    args = parser.parse_args()
    if not 1 <= args.tasks <= 32:
        parser.error("--tasks doit être compris entre 1 et 32.")
    if not 1 <= args.samples <= 1_000_000:
        parser.error("--samples doit être compris entre 1 et 1000000.")
    if not 2 <= args.repeats <= 10:
        parser.error("--repeats doit être compris entre 2 et 10.")
    if args.seed < 0:
        parser.error("--seed doit être positif ou nul.")

    tasks = [SimulationTask(args.seed + index, args.samples) for index in range(args.tasks)]
    expected = run_sequential(tasks)
    if run_parallel(tasks, args.workers) != expected:
        raise AssertionError("Les résumés séquentiels et parallèles diffèrent.")
    print(f"{args.tasks} tâches × {args.samples:,} observations synthétiques ; {args.workers} processus.")
    print("Simulation N(100, 18²) ; une valeur seed différente par tâche.")
    print("Résultats identiques vérifiés AVANT les mesures.")
    print("Temps de bout en bout : démarrage/fermeture du pool et transferts inclus.")
    print("Les comparaisons de résultats sont exclues des temps.\n")
    print("seed  observations  moyenne   proportion > 130")
    for summary in expected:
        print(f"{summary.seed:<5} {summary.samples:<13} {summary.sample_mean:8.3f}   {summary.fraction_above_130:.4f}")
    for label, function in (
        ("Séquentiel", lambda: run_sequential(tasks)),
        ("Processus", lambda: run_parallel(tasks, args.workers)),
    ):
        timings = []
        for _ in range(args.repeats):
            start = perf_counter()
            result = function()
            timings.append(perf_counter() - start)
            if result != expected:
                raise AssertionError("Un résultat a changé pendant les mesures.")
        samples = ", ".join(f"{elapsed * 1000:.2f}" for elapsed in timings)
        print(f"\n{label} : médiane={median(timings) * 1000:.2f} ms ; mesures=[{samples}]")
    print("\nLe parallélisme change l'exécution, pas la taille des échantillons ni leur précision.")
    print("Un démarrage coûteux peut annuler le gain : comparer plusieurs tailles.")


if __name__ == "__main__":
    freeze_support()
    main()
