tax_for_one_year = int(input())

shoes = tax_for_one_year * 0.6
clothes = shoes * 0.8
ball = clothes * 0.25
accessories = ball * 0.2

expenses = tax_for_one_year + shoes + clothes + ball + accessories

print(expenses)