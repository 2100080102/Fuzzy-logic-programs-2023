import numpy as np
def max_min_composition(a, b):
    n = len(a)
    m = len(b[0])
    R = np.zeros((n, m))
    for i in range(n):
        for k in range(m):
            R[i, k] = np.max(np.minimum(a[i, :], b[:, k]))
    return R
def max_dot_composition(a, b):
    n = len(a)
    m = len(b[0])
    R = np.zeros((n, m))
    for i in range(n):
        for k in range(m):
            R[i, k] = np.max(a[i, :] * b[:, k])
    return R
a = np.array([[0.6, 0.6, 0.8, 0.9],
              [0.1, 0.2, 0.9, 0.8],
              [0.9, 0.3, 0.4, 0.8],
              [0.9, 0.8, 0.1, 0.2]])

b = np.array([[0.1, 0.2, 0.7, 0.9],
              [1.1, 0.4, 0.6, 0.0],
              [0.0, 0.5, 0.9, 0.0],
              [0.9, 1.0, 0.8, 0.2]])
# Max-min composition
R_max = max_dot_composition(a, b)
print("Max-dot Composition (R_max):")
print(R_max)
R_max = max_dot_composition(a, b)
print("Max-dot Composition (R_max):")
print(R_max)
