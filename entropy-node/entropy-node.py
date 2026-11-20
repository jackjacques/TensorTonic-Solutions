import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    # Write code here
    values, counts = np.unique(y, return_counts=True)
    p = [counts[i]/len(y) for i in range(len(values))]
    Entropy = 0
    for e in range(len(p)):
        if p[e]==0:
            Entropy+=0
        else:
            Entropy += p[e]*np.log2(p[e])
    return - float(Entropy)