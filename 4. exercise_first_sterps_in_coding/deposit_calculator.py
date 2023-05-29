deposit = float(input())
time_of_deposit = int(input())
annual_interest_rate = float(input())

interest = deposit * (annual_interest_rate / 100)
interest_for_one_month = interest / 12
total_income = deposit + time_of_deposit * interest_for_one_month

print(total_income)