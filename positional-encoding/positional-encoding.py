import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    x_arr = np.zeros((seq_len, d_model))
    x = np.asarray(x_arr, dtype = float)
    for pos in range(seq_len):
        for i in range(d_model):
            if i%2 == 0:
                x[pos, i] = np.sin(pos/base**(2*(i//2)/d_model))
            else:
                x[pos, i] = np.cos(pos/base**(2*(i//2)/d_model))
    return x