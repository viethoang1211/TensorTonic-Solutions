import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    ans = [0]*len(vocab)
    for i in tokens:
        for j in range(len(vocab)):
            if i == vocab[j]:
                ans[j]+=1
                break
    return np.array(ans,dtype=int)
    pass