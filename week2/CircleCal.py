# 3.원의 반지름 입력받아 원의 둘레와 넓이를 구하는 코드를 작성하세요(CircleCal.py)

import math

radius = float(input("원의 반지름: "))

circumference = 2 * math.pi * radius
area = math.pi * radius * radius

print("원의 둘레:", circumference)
print("원의 넓이:", area)
