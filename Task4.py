# Employee Overtime Calculator

employee_name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate (UGX): "))
hours_worked = float(input("Enter hours worked: "))

# Calculations
if hours_worked <= 40:
    regular_pay = hourly_rate * hours_worked
    overtime_pay = 0
    gross_pay = regular_pay

    print("\n No overtime was accrued.")

else:
    regular_pay = hourly_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

# Output
print(f"\nEmployee: {employee_name}  |  Rate: {hourly_rate:.2f} UGX/hr  |  Hours: {hours_worked}")

print(f"\nRegular : {regular_pay:.2f} UGX  |  Overtime : {overtime_pay:.2f} UGX  |  Gross : {gross_pay:.2f} UGX ")
print(f"\n")
