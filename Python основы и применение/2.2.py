from datetime import date, timedelta
inp1 = list(map(int, input().split()))
inp2 = int(input())

date = date(*inp1)
days = timedelta(days=inp2)
result = date + days

print(result.year, result.month, result.day)