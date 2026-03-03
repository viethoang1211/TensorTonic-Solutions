import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if sum(p) != 1 or len(x)!=len(p):
        raise ValueError
    return sum([x[i]*p[i] for i in range(len(p))])
    pass
