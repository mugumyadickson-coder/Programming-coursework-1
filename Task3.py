# Simple Currency Converter

# Exchange rates
# 1 USD = 3700 UGX
# 1 EUR = 4400 UGX
# 1 GBP = 5100 UGX

while True:

    print("\nSelect conversion option:")
    print("[1] UGX → USD")
    print("[2] UGX → EUR")
    print("[3] UGX → GBP")

    choice = input("Enter choice: ")

    amount = float(input("Enter amount in UGX: "))

    # Validation
    if amount <= 0:
        print("Amount must be positive.")
        continue

    if choice == "1":
        converted = amount / 3700
        print(f"{amount:.2f} UGX = {converted:.2f} USD")

    elif choice == "2":
        converted = amount / 4400
        print(f"{amount:.2f} UGX = {converted:.2f} EUR")

    elif choice == "3":
        converted = amount / 5100
        print(f"{amount:.2f} UGX = {converted:.2f} GBP")

    else:
        print("Invalid choice.")

    again = input("Do another conversion? (yes/no): ")

    if again != "yes":
        print("Program ended.")
        break