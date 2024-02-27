import numpy as np

def func(array):

    scaled = np.interp(array, (array.min(), array.max()), (0.0, 1.0))
    return scaled


import unittest

class TestFunc(unittest.TestCase):

    def test_func_positive_numbers(self):
        array = np.array([1, 2, 3, 4, 5])
        result = func(array)
        expected_result = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_func_negative_numbers(self):
        array = np.array([-5, -4, -3, -2, -1])
        result = func(array)
        expected_result = np.array([1.0, 0.75, 0.5, 0.25, 0.0])
        np.testing.assert_array_almost_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()

# Feedback:
    # No defensive programming (assert)
    # No documentation