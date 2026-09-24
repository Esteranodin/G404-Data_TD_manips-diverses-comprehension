"""One fixed teaching task: mean of a seeded normal sample."""

from random import Random


def sample_mean(task):
    # The provided tasks use a positive integer size.
    seed, size = task
    rng = Random(seed)
    total = 0.0
    for _ in range(size):
        total += rng.gauss(100, 18)
    return total / size
