import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Write code here
    w = np.zeros(X.shape[1])
    b = 0.0
    z = X @ w + b
    p = _sigmoid(z)
    Loss = -1/len(y) * np.sum([y[i]*np.log(p[i])+(1-y[i])*np.log(1-p[i]) for i in range(len(y))])
    for s in range(steps) :
        dw = 1/len(y)*X.T@(p-y)
        db = 1/len(y) * np.sum([p[i] - y[i] for i in range(len(y))])
        w += -lr * dw 
        b += -lr * db
        z = X @ w + b
        p = _sigmoid(z)
    return w, float(b)
        