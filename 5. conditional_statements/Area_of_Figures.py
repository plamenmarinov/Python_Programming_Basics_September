import math

figure = str(input())

if figure == "square":
    side_lengh = float(input())
    area = side_lengh * side_lengh
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    area = math.pi * (radius * radius)
    print(f"{area:.3f}")
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2
    print(f"{area:.3f}")
