import numpy as np

def adam_step(
    param: list,
    grad: list,
    m: list,
    v: list,
    t: int,
    lr: float = 1e-3,
    beta1: float = 0.9,
    beta2: float = 0.999,
    eps: float = 1e-8,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Returns (param_new, m_new, v_new) as NumPy arrays.
    """
    # Write code here
    param_new = np.asarray(param, dtype = float)
    mt = np.asarray(m, dtype = float)
    vt = np.asarray(v, dtype = float)
    gradt = np.asarray(grad, dtype = float)
    mt = beta1 * mt + (1-beta1)*gradt
    vt = beta2*vt + (1-beta2)*gradt**2
    param_new += - lr * (mt/(1-beta1**t))/(np.sqrt(vt/(1-beta2**t)) + eps)
    return (param_new, mt, vt)