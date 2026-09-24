"""Importable deterministic tasks used by run_processes.py on every process."""

from random import Random
from typing import NamedTuple


class SimulationTask(NamedTuple):
    seed: int
    samples: int


class SimulationSummary(NamedTuple):
    seed: int
    samples: int
    sample_mean: float
    fraction_above_130: float


def simulate_sample(task: SimulationTask) -> SimulationSummary:
    """Summarize a synthetic normal sample with mean 100 and std dev 18."""
    if task.samples < 1:
        raise ValueError("samples must be positive")
    rng = Random(task.seed)
    total = 0.0
    above = 0
    for _ in range(task.samples):
        value = rng.gauss(100.0, 18.0)
        total += value
        above += value > 130.0
    return SimulationSummary(task.seed, task.samples, total / task.samples, above / task.samples)
