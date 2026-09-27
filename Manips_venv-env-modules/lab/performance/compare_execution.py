"""Compare a Python loop, NumPy and NumPy across disjoint thread slices."""

import argparse
import itertools
from concurrent.futures import ThreadPoolExecutor
from statistics import median
from time import perf_counter

import numpy as np


def divide_loop(values: np.ndarray) -> np.ndarray:
    output = np.empty_like(values)
    for index, value in enumerate(values):
        output[index] = value / 60.0
    return output


def divide_numpy(values: np.ndarray) -> np.ndarray:
    return values / 60.0


def divide_threads(values: np.ndarray, workers: int) -> np.ndarray:
    output = np.empty_like(values)
    boundaries = np.linspace(0, len(values), workers + 1, dtype=int)

    def divide_slice(bounds: tuple[int, int]) -> None:
        start, stop = bounds
        # Each worker writes to its own slice; the input is read-only here.
        np.divide(values[start:stop], 60.0, out=output[start:stop])

    with ThreadPoolExecutor(max_workers=workers) as pool:
        # plusieurs fils pour executer / attente
        list(pool.map(divide_slice, itertools.pairwise(boundaries)))
    return output


def measure(function, expected: np.ndarray, repeats: int) -> list[float]:
    # Validate and warm up once before recording; exclude comparisons from time.
    np.testing.assert_array_equal(function(), expected)
    timings = []
    for _ in range(repeats):
        start = perf_counter()
        result = function()
        timings.append(perf_counter() - start)
        np.testing.assert_array_equal(result, expected)
    return timings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--size", type=int, default=200_000)
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=2)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--seed", type=int, default=404)
    args = parser.parse_args()
    if not 1 <= args.size <= 5_000_000:
        parser.error("--size doit être compris entre 1 et 5000000.")
    if not 2 <= args.repeats <= 20:
        parser.error("--repeats doit être compris entre 2 et 20.")
    if args.seed < 0:
        parser.error("--seed doit être positif ou nul.")

    values = np.random.default_rng(args.seed).uniform(0, 300, args.size)
    # Check the operation on explicit known inputs before the larger comparison.
    known = np.array([0.0, 60.0, 90.0])
    for result in (
        divide_loop(known), divide_numpy(known), divide_threads(known, args.workers)
    ):
        np.testing.assert_array_equal(result, np.array([0.0, 1.0, 1.5]))
    expected = divide_numpy(values)
    methods = {
        "Boucle Python": lambda: divide_loop(values),
        "NumPy": lambda: divide_numpy(values),
        f"NumPy + {args.workers} thread(s)": lambda: divide_threads(values, args.workers),
    }
    print(f"{args.size:,} valeurs ; seed={args.seed} ; {args.repeats} mesures.")
    print("Résultats vérifiés avant et après chaque mesure.")
    print("Temps : calcul + allocation ; threads : création/fermeture du pool incluses.")
    print("Génération des données et comparaison des résultats exclues des temps.\n")
    for name, function in methods.items():
        timings = measure(function, expected, args.repeats)
        samples = ", ".join(f"{elapsed * 1000:.3f}" for elapsed in timings)
        print(f"{name:23} médiane={median(timings) * 1000:9.3f} ms ; mesures=[{samples}]")
    print("\nAucun gain n'est garanti : taille, mémoire, calcul et démarrage comptent.")


if __name__ == "__main__":
    main()
