# Day11 comparison and logic operators
# What are they?

# 1. Comparison Operator
# Comparison operator are used when you want to compare two things like numbers
# or values to check if they are equal or if one is bigger or smaller than the other

print('Common Comparison Operators')
print('''Important: These operators always give you either True (Yes) or False (No) '
as the answer [true means 1] and [false means 0]''')
print("""
| Operator | Example in Python | What it means                    | Result Type       |
| -------- | ----------------- | -------------------------------- | ----------------- |
| `==`     | `5 == 5`          | Is 5 equal to 5?                 | `True` or `False` |
| `!=`     | `5 != 3`          | Is 5 not equal to 3?             | `True` or `False` |
| `>`      | `7 > 4`           | Is 7 greater than 4?             | `True` or `False` |
| `<`      | `3 < 9`           | Is 3 less than 9?                | `True` or `False` |
| `>=`     | `6 >= 6`          | Is 6 greater than or equal to 6? | `True` or `False` |
| `<=`     | `2 <= 5`          | Is 2 less than or equal to 5?    | `True` or `False` |
""")

#Comparison Operators – Small Code Examples
#1. == (Equal to)
a = 10
b = 10
print(a == b)   # True

#2. != (Not equal to)
a = 5
b = 3
print(a != b)   # True

#3. > (Greater than)
a = 7
b = 2
print(a > b)    # True

#4. < (Less than)
a = 3
b = 10
print(a < b)    # True

#5. >= (Greater than or equal to)
a = 6
b = 6
print(a >= b)   # True

#6. <= (Less than or equal to)
a = 4
b = 9
print(a <= b)   # True


# 2. Logical Operators
# What are they?
# Logical operators help you combine multiple conditions together. For example:
# “Is the person older than 18 and has passed the exam?”
# “Is it raining or snowing?”

print("""
Common Logical Operators in Python:
| Operator | Example         | What it means                         | Result  |
| -------- | --------------- | ------------------------------------- | ------- |
| `and`    | `True and True` | Both conditions must be True          | `True`  |
| `or`     | `True or False` | At least one condition is True        | `True`  |
| `not`    | `not True`      | Reverses the condition (True → False) | `False` |
""")
"""
| Type       | What it does                 | Examples                         |
| ---------- | ---------------------------- | -------------------------------- |
| Comparison | Compares two values          | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical    | Combines multiple conditions | `and`, `or`, `not`               |"""

#Logical Operators – Small Code Examples
#1. and (Both conditions must be True)
age = 20
passed = True
print(age > 18 and passed)   # True

#2. or (At least one condition is True)
rain = False
snow = True
print(rain or snow)          # True

#3. not (Reverses the condition)
is_sunny = True
print(not is_sunny)          # False