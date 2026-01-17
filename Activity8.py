# collect hours and pay
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

#Calculate gross pay
gross_pay = hours_worked * hourly_rate

print(f"Gross Pay: ${gross_pay:.2f}")
