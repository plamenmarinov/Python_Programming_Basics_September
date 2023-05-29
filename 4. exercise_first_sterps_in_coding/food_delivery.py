chicken_menu = int(input())
fish_menu = int(input())
vege_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vege_menu_price = 8.15
menu_price = (chicken_menu * chicken_menu_price) + (fish_menu * fish_menu_price) + (vege_menu * vege_menu_price)
desert = menu_price * 0.2
delivery = 2.50
total_price = menu_price + desert + delivery

print(f"{total_price:.2f}")