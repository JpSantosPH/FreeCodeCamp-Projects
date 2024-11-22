import numpy as np

def _calculate_3axis(np_func, np_array):
    axis1 = list(np_func(np_array, axis=0))
    axis2 = list(np_func(np_array, axis=1))
    flatttened = np_func(np_array)
    return [axis1, axis2, flatttened]

def calculate(list9):
    if len(list9) != 9:
        raise ValueError('List must contain nine numbers.')

    array = np.array(list9).reshape(3,3)

    calculations = {
        'mean': _calculate_3axis(np.mean, array),
        'variance': _calculate_3axis(np.var, array),
        'standard deviation': _calculate_3axis(np.std, array),
        'max': _calculate_3axis(np.max, array),
        'min': _calculate_3axis(np.min, array),
        'sum': _calculate_3axis(np.sum, array)
    }

    return calculations