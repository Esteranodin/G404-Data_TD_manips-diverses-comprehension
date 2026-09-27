"""Read the functions in order, then compare identical tasks in two modes."""

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context

from mean_task import sample_mean


def run_sequential(tasks):
    results = []
    for task in tasks:
        result = sample_mean(task)
        results.append(result)
    return results


def run_parallel(tasks, workers):
    context = get_context("spawn")
    with ProcessPoolExecutor(
    # plusieurs processeur pour executer en parallèle
        max_workers=workers, mp_context=context
    ) as pool:
        results = list(pool.map(sample_mean, tasks))
    return results


def main():
    tasks = [(404, 20_000), (405, 20_000)]
    expected = run_sequential(tasks)
    result = run_parallel(tasks, workers=2)
    assert result == expected
    print("Moyennes en séquentiel :", expected)
    print("Moyennes avec deux processus :", result)
    print("Mêmes tâches, mêmes résultats, dans le même ordre.")


if __name__ == "__main__":
    main()
