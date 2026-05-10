# Student Grade Classifier

student_name = input("Enter student name: ")
score = int(input("Enter score (0 - 100): "))

# Validation
if score < 0 or score > 100:
    print("Error!! Score must be between 0 and 100.")
else:
    if score >= 75:
        grade = "Distinction"
        result = "PASS"
    elif score >= 60:
        grade = "Merit"
        result = "PASS"
    elif score >= 50:
        grade = "Pass"
        result = "PASS"
    else:
        grade = "Fail"
        result = "FAIL"

    print(f"\nStudent: {student_name} | Score: {score} | Grade: {grade} | Result: {result}")