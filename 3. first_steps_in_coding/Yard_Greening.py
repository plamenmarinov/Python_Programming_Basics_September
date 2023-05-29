square_meter_for_landscaping = float(input())
price_for_hole_landscaping = square_meter_for_landscaping * 7.61
discount = 0.18
discount_price = price_for_hole_landscaping * discount
total_price_with_discount = price_for_hole_landscaping - discount_price

print(f"The final price is: {total_price_with_discount} lv.")
print(f"The discount is: {discount_price} lv.")