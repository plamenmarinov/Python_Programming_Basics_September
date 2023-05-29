pencil_pack_count = int(input())
marker_pack_count = int(input())
preparat_clean_board_liter = int(input())
discount_persent = int(input())

total_sum = (pencil_pack_count * 5.8) + (marker_pack_count * 7.20) + (preparat_clean_board_liter * 1.20)

discount = total_sum * (discount_persent / 100)

total_sum_plus_discount = total_sum - discount

print(total_sum_plus_discount)