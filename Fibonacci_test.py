import math

MOD = 10000007

t = int(input())
while t > 0:
    n = int(input())
    s5 = math.sqrt(5)
    F = (1 / s5) * (((1 + s5) / 2)**n - ((1 - s5) / 2)**n)
    print(int(F) % MOD)
    t -= 1