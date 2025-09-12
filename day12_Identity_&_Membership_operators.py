# Day12 in 100 days of code python
# Topic: Identity and membership operators
# What are they?

# 1. Identity Operators
# Identity operators check whether two objects are the same in memory.
# They do not check values, they check object identity.
# Python has two identity operators:

# Operator	Meaning
# is	Returns True if both objects refer to the same memory location
# is not	Returns True if both objects refer to different memory locations
# Example:
print("1. Identity Operators")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("""a = [1, 2, 3]
b = [1, 2, 3]
c = a""")
print("a is b",a is b)      # False, because they are different objects in memory
print("a is c",a is c)      # True, because both refer to the same object
print("a is not b",a is not b)  # True

print("""Explanation:
a and b have the same values, but are stored in different memory locations → a is b is False
a and c point to the same object in memory → a is c is True
""")


# 2. Membership Operators
# Membership operators check whether an element exists in a sequence (like list, tuple, string, etc.).
# Python has two membership operators:
# Operator	Meaning
# in	Returns True if the element exists in the sequence
# not in	Returns True if the element does not exist in the sequence

# Example:
print('2. Membership Operators')
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)      # True
print("grapes" in fruits)     # False
print("grapes" not in fruits) # True

print("""Explanation:
fruits = ["apple", "banana", "mango"]
"apple" is in the list → in is True
"grapes" is not in the list → in is False, not in is True
Quick Tip to Remember:
Identity (is, is not) → “Are they the same object?”
Membership (in, not in) → “Does this element exist?”""")
