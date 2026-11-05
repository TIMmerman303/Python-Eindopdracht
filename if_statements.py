# 1. Create three variables with grades for different subjects
wiskunde_grade = 6.5
engels_grade = 7.0
nederlands_grade = 5.0

# 2. Calculate the average of these grades
average_grade = (wiskunde_grade + engels_grade + nederlands_grade) / 3

print(f"Grades: Wiskunde ({wiskunde_grade}), Engels ({engels_grade}), Nederlands ({nederlands_grade})")
print(f"Average Grade: {average_grade:.1f}")
print("-----------------------------------")

# 3 & Bonus Check: Determine if the student passed or failed
# Bonus Rule: If ANY individual grade is lower than a 4, the student is always failed.
if wiskunde_grade < 4 or engels_grade < 4 or nederlands_grade < 4:
    print("Result: Gezakt! (One or more grades are below a 4.0)")

# Main Rule: If the average is 5.5 or higher, they pass.
elif average_grade >= 5.5:
    print("Result: Geslaagd!")

# Otherwise, they fail.
else:
    print("Result: Gezakt!")
