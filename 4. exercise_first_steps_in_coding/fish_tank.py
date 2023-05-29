lenght = int(input())
width = int(input())
height = int(input())
persent = float(input())

volume = lenght * width * height
volume_liters = volume / 1000

needed_liters = volume_liters * (1 - (persent / 100))

print(needed_liters)






