import math


edge_length = int(input())
area = 2 * math.sqrt(3) * math.pow(edge_length, 2)
volume = 1 / 3 * math.sqrt(2) * math.pow(edge_length, 3)
print(f'{round(area, 2)} {round(volume, 2)}')
