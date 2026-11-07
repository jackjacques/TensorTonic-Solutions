import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x_arr = np.asarray(x, dtype = float)
    m = np.max(x_arr, axis=-1, keepdims= True)
    exp_values = np.exp(x_arr - m)
    return exp_values/exp_values.sum(axis = -1, keepdims=True)