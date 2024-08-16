#Q1. Print "Hello, World!" to the console

# This line prints "Hello, World!" to the console
print("Hello, World!")


#Q2. Create variables to store your name, age, and favorite hobby, then print these variables

# Define variables
name = "Prakhar"  # Your name
age = 23          # Your age
favorite_hobby = "Video Editing"  # Your favorite hobby

# Print the variables
print("Name:", name)
print("Age:", age)
print("Favorite Hobby:", favorite_hobby)

#Q3. Add comments to the code
#(Comments are already added in the previous answers.)

#Q4. Program to check if an integer is positive, negative, or zero

# Take integer input from the user
number = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Q5. Program to check if a given year is a leap year

# Function to check if a year is a leap year
def is_leap_year(year):
    # Check if the year is divisible by 4 but not 100, or divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Take year input from the user
year = int(input("Enter a year: "))

# Print if the year is a leap year or not
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Q6. Print the first 10 natural numbers using a for loop

# Loop through numbers from 1 to 10 and print each one
for i in range(1, 11):
    print(i)

#Q7. Print the multiplication table of a given number using a while loop

# Take number input from the user
number = int(input("Enter a number for the multiplication table: "))

# Initialize the multiplier
multiplier = 1

# Loop to print the multiplication table
while multiplier <= 10:
    print(f"{number} x {multiplier} = {number * multiplier}")
    multiplier += 1

#Q8. Print numbers 1 to 10, skipping numbers divisible by 3 using the continue statement

# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Skip numbers divisible by 3
    if i % 3 == 0:
        continue
    print(i)

#Q9. Stop printing numbers when encountering a number greater than 5 using the break statement

# Loop through numbers from 1 to 10
for i in range(1, 11):
    # Break the loop if the number is greater than 5
    if i > 5:
        break
    print(i)

#Q10. Define a function called greet that takes a name as an argument and prints "Hello, [name]!"

# Define the greet function
def greet(name):
    print(f"Hello, {name}!")

# Call the function with a name
greet("Prakhar")

#Q11. Create a function that takes two numbers as arguments and returns their sum

# Define the function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Example usage of the function
result = add_numbers(5, 7)
print("The sum is:", result)
