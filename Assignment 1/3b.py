n = int(input("How many numbers do you want to enter? ")) # Number of values

sum_numbers = 0

for i in range(n):
    value = float(input(f"Enter number {i + 1}: ")) # Input n numbers
    sum_numbers += value

average = sum_numbers / n

print("Average =", average)