"""Repair the returned value, then implement the complete input contract."""
import math


def minutes_to_hours(minutes: object) -> float:
    """Return hours as a float for a finite, nonnegative real number.

    Zero and fractional minutes are valid. Reject bool and non-real values
    with TypeError; reject negative, infinite or NaN values with ValueError.
    This starter intentionally returns text and lacks input validation.
    """
    # return f"{minutes / 60:g} hours"

    if isinstance(minutes, bool):
        raise TypeError("minutes must be a real number, not bool")
    if not isinstance(minutes, (int, float)):
        raise TypeError("minutes must be a real number")
    if minutes < 0 or not math.isfinite(minutes):
        raise ValueError("minutes must be finite and nonnegative")
    return float(minutes) / 60.0