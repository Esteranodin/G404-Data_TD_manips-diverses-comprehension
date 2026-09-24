"""Repair the returned value, then implement the complete input contract."""


def minutes_to_hours(minutes: float) -> float:
    """Return hours as a float for a finite, nonnegative real number.

    Zero and fractional minutes are valid. Reject bool and non-real values
    with TypeError; reject negative, infinite or NaN values with ValueError.
    This starter intentionally returns text and lacks input validation.
    """
    return minutes / 60
    # return f"{minutes / 60:g} hours"
