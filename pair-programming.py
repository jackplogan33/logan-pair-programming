import numpy as np

def func(array):

    scaled = np.interp(array, (array.min(), array.max()), (0.0, 1.0))
    return scaled
