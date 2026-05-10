#  Body Mass Index (BMI) Advisor

name = input("Enter your name: ")
weight = float(input("Enter weight (in kilograms): "))
height = float(input("Enter height (in meters): "))

# Validation
if weight <= 0 or height <= 0:
    print("Error: Weight and height must be greater than zero.")

else:
    # BMI Calculation
    bmi = weight / (height ** 2)

    # Classification
    if bmi < 18.5:
        category = "Underweight"
        advice = "Eat a balanced nutritious diet."

    elif bmi < 25:
        category = "Normal"
        advice = "Maintain a balanced diet."

    elif bmi < 30:
        category = "Overweight"
        advice = "Exercise regularly and eat healthy."

    else:
        category = "Obese"
        advice = "Consult a healthcare professional."

    # Output
    print(f"\nName: {name}")
    print(f"BMI: {bmi:.1f}")
    print(f"Category: {category}")
    print(f"Advisory: {advice}")