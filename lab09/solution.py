import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    return {
        'third': values[2],
        'last': values[-1],
        'middle': values[2:6],
        'every_second': values[::2],
        'reversed' : np.array(values)[::-1].tolist()
    }


def change_vector(values: list[float]) -> list[float]:
    vector = np.array(values).copy()

    vector[2:5] = 99
    vector[::2] = -1
    return vector.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.array(values)
    arr[arr > limit] = limit
    return arr.tolist()


def celsius_to_fahrenheit(celsius: list[float]) -> list[float]:
    return (np.array(celsius) * 9/5 + 32).tolist()
