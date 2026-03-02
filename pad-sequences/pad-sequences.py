import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    n=len(seqs)
    l = max(len(seq) for seq in seqs)
    if max_len:
        l= max_len
    for i in seqs:
        while len(i) < l:
            i.append(pad_value)
        while len(i) > l:
            i.pop()
    return seqs
    pass