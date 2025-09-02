# Day 4 - Type Casting

# Type casting = converting one data type into another using built-in functions.

# Example 1: String concatenation
a = "4"
b = "6"
print(a + b)  # Output: "46" (string concatenation)

# Example 2: Integer addition
print(int(a) + int(b))  # Output: 10

# Example 3: Multiple operations
num1 = 12
num2 = 100
print("Concatenation:", a + b)
print("Addition:", num1 + num2)

# Common Type Casting Functions
x = int("123")        # str → int
y = float("3.14")     # str → float
z = str(42)           # int → str

my_list = list("hello")       # str → list
my_tuple = tuple([1, 2, 3])   # list → tuple
my_set = set([1, 1, 2, 3])    # list → set {1, 2, 3}

print("Casted values:", x, y, z, my_list, my_tuple, my_set)
