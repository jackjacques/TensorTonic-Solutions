import math
 
def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    res = []
    for c in x :
        if c>0:
            res.append(c)
        else:
            res.append(alpha * (math.exp(c) -1))
    return res