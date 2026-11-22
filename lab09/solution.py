import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 22, 3)


def vector_report(values: list[float]) -> dict:
    return {
        'third': values[2],
        'last': values[-1],
        'slice': values[2:6],
        'every_second': values[::2],
        'flattened' : np.array(values).flatten()
    }


def change_vector(values: list[float]) -> list[float]:
    vector = np.array(values)

    vector[2:5] = 99
    vector[::2] = -1
    return vector.tolist()




