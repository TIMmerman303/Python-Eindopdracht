# --- Assignment 4: Loops ---

# 1. Print numbers 1 to 10 using a loop
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n-----------------------------------")

# 2. Loop through a countdown from 5 to 1 (Bonus logic)
print("Countdown:")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1
print("Blast off! 🚀")
print("-----------------------------------")

# 3. Calculate the sum of numbers from 1 to 100
total_sum = 0
for number in range(1, 101):
    total_sum += number

print(f"The total sum of all numbers from 1 to 100 is: {total_sum}")
    