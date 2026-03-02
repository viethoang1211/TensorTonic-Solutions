import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    ans=[]
    for j in range(len(A[0])):
        ans.append([i[j] for i in A])
    return np.array(ans)
