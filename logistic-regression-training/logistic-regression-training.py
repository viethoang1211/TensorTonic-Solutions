import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    w= np.zeros(len(X[0]))
    b=0
    n = len(X)
    for _ in range(steps):
        z =  w @ X.T +b
        p = np.array([_sigmoid(i) for i in z])
        w = w - lr * 1/n * X.T @ (p-y)
        b= b - lr * 1/n * (sum(p)-sum(y))
    return (w,b)
    pass