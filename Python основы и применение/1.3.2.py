import math

n, k = map(int, input().split())

c = math.factorial(n) / (math.factorial(k) * (math.factorial(n - k)))
print(int(c))