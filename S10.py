k = int(input())
s = input()

print(s[k-1::-1] + s[:k-1:-1])