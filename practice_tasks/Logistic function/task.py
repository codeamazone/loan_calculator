import math

number = int(input())
result = math.pow(math.e, number) / (math.pow(math.e, number) + 1)
print(round(result, 2))
