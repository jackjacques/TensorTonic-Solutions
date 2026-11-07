import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    Lambda, alpha = 1.0507, 1.6733
    res = []
    for c in x :
        if c > 0:
            res.append(Lambda * c)
        else:
            res.append(Lambda * alpha * (math.exp(c) -1))
    return res