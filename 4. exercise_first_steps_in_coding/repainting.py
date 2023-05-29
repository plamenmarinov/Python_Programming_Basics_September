naylon = int(input())
paint = int(input())
razreditel = int(input())
work_hours = int(input())

naylon_price = 1.5
paint_price = 14.50
razreditel_price = 5

total_naylon_price = (naylon + 2) * naylon_price
total_paint_price = (paint + (paint * 0.1)) * paint_price
total_razreditel_price = razreditel * razreditel_price

total_materials = total_naylon_price + total_paint_price + total_razreditel_price + 0.40

total_work_hour_price = (total_materials * 0.3) * work_hours

total_price = total_materials + total_work_hour_price

print(total_price)