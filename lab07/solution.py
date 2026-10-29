import numpy as np


def reshape_rows(values, width):
    if len(values) % width != 0:
        return []

    matrix = np.asarray(values, dtype=float).reshape(-1, width)
    return matrix.round(6).tolist()