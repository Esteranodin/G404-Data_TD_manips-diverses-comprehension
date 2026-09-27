def delay_minutes(actual: int, promises: int) -> int:
    delay = actual - promises
    if delay < 0:
        return 0
    return delay