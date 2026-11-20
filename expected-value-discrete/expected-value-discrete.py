import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    esp = 0
    for i in range(len(x)):
        esp += float(x[i]*p[i])
    return esp