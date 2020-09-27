import numpy as np


def move_to_start(arr: np.ndarray, i):
    """
    Move `i` line of `arr` to the beginning
    """
    result = np.empty_like(arr)
    result[0] = arr[i]
    result[1 : i + 1] = arr[:i]
    result[i + 1 :] = arr[i + 1 :]
    return result


def move_to_end(arr: np.ndarray, i):
    """
    Move `i` line of `arr` to the end
    """
    result = np.empty_like(arr)
    result[:i] = arr[:i]
    result[i:-1] = arr[i + 1 :]
    result[-1] = arr[i]
    return result
