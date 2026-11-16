import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    x_arr = np.asarray(x, dtype = float)
    dropout_pattern = np.zeros(x_arr.shape)
    output = np.zeros(x_arr.shape)
    if rng == None :
        rng = np.random.random(x_arr.shape)
    keep = rng.random(x_arr.shape)< 1- p 
    output = 1/(1-p)*keep*x_arr
    dropout_pattern = 1/(1-p)*keep
    return (output, dropout_pattern)