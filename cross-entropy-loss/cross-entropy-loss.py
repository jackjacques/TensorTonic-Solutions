import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    y_pred_arr = np.asarray(y_pred, dtype=float)
    y_true_arr = np.asarray(y_true, dtype=int)
    
    indices = np.arange(len(y_true_arr))
    N = len(y_true_arr)
    

    return np.mean(-np.log(y_pred_arr[indices, y_true_arr]))