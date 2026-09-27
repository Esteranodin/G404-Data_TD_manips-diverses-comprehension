import numpy as np

class TemperatureSeries:

    def __init__(self, fahrenheit: np.ndarray):
        self.fahrenheit = np.asarray(fahrenheit, dtype=float)

    def celsius(self) -> np.ndarray:
        return(self.fahrenheit - 32) * 5 / 9