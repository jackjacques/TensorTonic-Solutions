import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x_arr = np.asarray(x, dtype=float)
    vect_erf = np.vectorize(math.erf)
    return (x_arr/2.0)*(1 + vect_erf(x_arr / math.sqrt(2.0)))