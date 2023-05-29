sheets_count = int(input())
sheets_read_for_one_hour = int(input())
days_count_for_reading = int(input())

total_days_for_reading = sheets_count / sheets_read_for_one_hour
hours_needed_for_one_day = total_days_for_reading / days_count_for_reading

print(f"{hours_needed_for_one_day:.0f}")
