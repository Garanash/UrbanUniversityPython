import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Операция И (AND)
W = np.zeros(3)
for xi, target in zip(X, y):
    print(xi, target)
    print(np.dot())
