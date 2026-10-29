import numpy as np


def reshape_rows(values, width):
    if len(values) % width != 0:
        return []

    matrix = np.asarray(values, dtype=float).reshape(-1, width)
    return matrix.round(6).tolist()


def block(matrix, rows, columns):
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    selected = array[np.ix_(rows, columns)]
    return selected.round(6).tolist()

def column_means(matrix):
    if not matrix:
        return []

    array = np.asarray(matrix, dtype=float)
    means = np.mean(array, axis=0)
    return means.round(6).tolist()