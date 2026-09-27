"""Small, readable array example; demonstrates equality, not a speed gain."""

from concurrent.futures import ThreadPoolExecutor

import numpy as np


def divide_chunk(chunk):
    return chunk / 60.0


def main():
    values = np.array([0, 60, 90, 120], dtype=float)

    output = np.empty_like(values)
    for i, value in enumerate(values):
        output[i] = value / 60.0
        
    expected = values / 60.0

    np.testing.assert_array_equal(output, expected)

    chunks = [values[:2], values[2:]]
    # chunks égale donc [array([0., 60.]), array([90., 120.])]
    with ThreadPoolExecutor(max_workers=2) as pool:
        parts = list(pool.map(divide_chunk, chunks))
        # [
        #     array([0.0, 1.0]),
        #     array([1.5, 2.0])
        # ]
    result = np.concatenate(parts)
    # array([0.0, 1.0, 1.5, 2.0])
    np.testing.assert_array_equal(result, expected)
    print("Minutes :", values)
    print("Heures, avec une boucle :", output)
    print("Heures, avec NumPy :", expected)
    print("Heures, avec deux threads :", result)
    print("Quatre valeurs pour comprendre ; aucune mesure de vitesse ici.")


if __name__ == "__main__":
    main()
