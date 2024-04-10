import numpy as np

np.set_printoptions(formatter={'all': lambda x: " {:.0f}.".format(x)})
n, m = map(int, input().split())

if n == m:
    print(np.identity(n))
else:
    print(np.eye(n, m, k = 0))