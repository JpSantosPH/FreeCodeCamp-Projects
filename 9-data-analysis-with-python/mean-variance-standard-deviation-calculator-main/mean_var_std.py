import numpy as np

def _calculate(np_func, np_array):
    axis1 = list(np_func(np_array, axis=0))
    axis2 = list(np_func(np_array, axis=1))
    flatttened = np_func(np_array)
    return [axis1, axis2, flatttened]

def calculate(list9):
    if len(list9) != 9:
        raise ValueError('List must contain nine numbers.')

    array = np.array(list9).reshape(3,3)

    calculations = {
        'mean': _calculate(np.mean, array),
        'variance': _calculate(np.var, array),
        'standard deviation': _calculate(np.std, array),
        'max': _calculate(np.max, array),
        'min': _calculate(np.min, array),
        'sum': _calculate(np.sum, array)
    }

    return calculations