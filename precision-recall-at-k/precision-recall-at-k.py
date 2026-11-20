def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    precision, recall = [], []
    for rel in relevant:
        for K in range(k):
            if rel == recommended[K]:
                precision.append(rel)
                recall.append(rel)
    return [float(len(precision)/k), float(len(recall)/len(relevant))]