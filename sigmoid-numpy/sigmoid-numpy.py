import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    def s(z):
        return 1.0 / (1.0 + np.exp(-z))
    if isinstance(x,(int,float)):
        return s(x)
    elif isinstance(x,list):
        return [sigmoid(y) for y in x]
    pass