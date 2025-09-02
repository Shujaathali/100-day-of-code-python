# Day 5 of 100 Days of Code - Python
# Topic: input() function

# The input() function takes input from the user as a string.
# Example:
# If we give a=4 and b=6, input() will store them as strings.
# So, a+b will perform string concatenation and result in "46".

# If we want to perform arithmetic operations, 
# we need to convert input values to integers (or floats).

a = input("Enter first number: ")
b = input("Enter second number: ")

print("String concatenation:", a + b)
print("Integer addition:", int(a) + int(b))