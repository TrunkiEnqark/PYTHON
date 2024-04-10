import numpy as np

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = np.array(a)
b = np.array(b)

print("[" + str(np.add(a, b)) + "]")
print("[" + str(np.subtract(a, b)) + "]")
print("[" + str(np.multiply(a, b)) + "]")
print("[" + str(a//b) + "]")
print("[" + str(np.mod(a, b)) + "]")
print("[" + str(np.power(a, b)) + "]")