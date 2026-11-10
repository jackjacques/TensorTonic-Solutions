import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs)
    if max_len :
        L = max_len
    elif len(seqs)!= 0 :
        L = max(len(seq) for seq in seqs)
    else :
        L = 0
    seqs_pad = np.full((N,L), pad_value)
    for seq in range(len(seqs)):
        for s in range(min(len(seqs[seq]), L)):
            seqs_pad[seq][s] = seqs[seq][s]
    return seqs_pad
        
        
            
            