import math

angle = int(input())
angle_radians = math.radians(angle)
cotangent = math.cos(angle_radians) / math.sin(angle_radians)
print(round(cotangent, 10))
