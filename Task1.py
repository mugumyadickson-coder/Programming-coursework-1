# Welcome & Receipt Generator

print("----------------------------------------")
print("GREENFIELD TRADING COMPANY")
print("----------------------------------------")

customer_name = input("Enter customer name: ")
date = input("Enter today's date: ")

# Item 1
item1 = input("Enter first item name: ")
price1 = float(input("Enter first item price: "))

# Item 2
item2 = input("Enter second item name: ")
price2 = float(input("Enter second item price: "))

# Item 3
item3 = input("Enter third item name: ")
price3 = float(input("Enter third item price: "))

# Calculations
subtotal = price1 + price2 + price3
vat = subtotal * 0.16
total = subtotal + vat

# Receipt Output
print("\n----------------------------------------")
print("GREENFIELD TRADING COMPANY")
print(f"Customer: {customer_name}     Date: {date}")
print("----------------------------------------")

print(f"{item1:<20} {price1:>10.2f}")
print(f"{item2:<20} {price2:>10.2f}")
print(f"{item3:<20} {price3:>10.2f}")

print("----------------------------------------")
print(f"Subtotal:           {subtotal:>10.2f}")
print(f"VAT (16%):          {vat:>10.2f}")
print(f"TOTAL:              {total:>10.2f}")
print("----------------------------------------")