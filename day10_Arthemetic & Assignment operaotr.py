# Arithmetic Operators Box in Python

# Creating a list of dictionaries for each operator
arithmetic_operators="""
 _____________________________________________
|Name               Symbol   Example          |
|---------------------------------------------|
|Addition           +        5 + 3 = 8        |
|Subtraction        -        5 - 3 = 2        |
|Multiplication     *        5 * 3 = 15       |
|Division           /        5 / 2 = 2.5      |
|Floor Division     //       5 // 2 = 2       |
|Modulus            %        5 % 2 = 1        |
|Exponentiation     **       5 ** 2 = 25      |
 ---------------------------------------------"""
print(arithmetic_operators)

print("More examples")
a=6
b=9
print(a+b)# 15
print(a-b)# -4
print(a*b)# 54
print(b/a)# 1.5
print(a//b)# 1 Floor division is almost same as divide but its always return answer in integer
# Always give output one less than to result eg: 5.67=5, 10.76=10 in minus -4.65=5, -7.78=8, -3.45=4
print(a%b)# 3 Modules  also do divide but its always give reminder.
print(a**b)# 10077696 Exponentiation means square root eg:6*9*9*9*9*9*9*9*9 =10077696


# Assignment Operators Examples
# Assignment operators are assign a values to variables. They can also be used to perform an operation
# and assign the result back to the same variable in a shorter way.

print("""
 ________________________________________________________________________
| Name                   | Symbol | Example             | Output Result  |
|------------------------|--------|---------------------|----------------|
| Assign                 |   =    | x = 5               | x = 5          |
| Add and Assign         |  +=    | x = 5; x += 3       | x = 8          |
| Subtract and Assign    |  -=    | x = 8; x -= 2       | x = 6          |
| Multiply and Assign    |  *=    | x = 6; x *= 4       | x = 24         |
| Divide and Assign      |  /=    | x = 24; x /= 2      | x = 12.0       |
| Floor Divide and Assign|  //=   | x = 12; x //= 5     | x = 2          |
| Modulus and Assign     |  %=    | x = 12; x %= 5      | x = 2          |
| Exponent and Assign    |  **=   | x = 2; x **= 3      | x = 8          |
| Bitwise AND and Assign |  &=    | x = 5; x &= 3       | x = 1          |
| Bitwise OR and Assign  |  |=    | x = 5; x |= 2       | x = 7          |
| Bitwise XOR and Assign |  ^=    | x = 5; x ^= 1       | x = 4          |
| Right Shift and Assign |  >>=   | x = 8; x >>= 2      | x = 2          |
| Left Shift and Assign  |  <<=   | x = 3; x <<= 2      | x = 12         |
 ------------------------------------------------------------------------
""")

print("Assignment Operators in Python")

# = operator
x = 10
print("\n= : x = 10 →", x)

# += operator
x += 5  # x = x + 5
print("+= : x += 5 →", x)

# -= operator
x -= 3  # x = x - 3
print("-= : x -= 3 →", x)

# *= operator
x *= 2  # x = x * 2
print("*= : x *= 2 →", x)

# /= operator
x /= 4  # x = x / 4
print("/= : x /= 4 →", x)

# //= operator
x //= 2  # x = x // 2
print("//= : x //= 2 →", x)

# %= operator
x %= 3  # x = x % 3
print("%= : x %= 3 →", x)

# **= operator
x = 2
x **= 3  # x = x ** 3
print("**= : x **= 3 →", x)

x = 5     # 0b0101
x &= 3    # 0b0011
print("&= : x &= 3 →", x)

# |= operator
x = 5     # 0b0101
x |= 2    # 0b0010
print("|= : x |= 2 →", x)

# ^= operator
x = 5     # 0b0101
x ^= 1    # 0b0001
print("^= : x ^= 1 →", x)

# >>= operator
x = 8     # 0b1000
x >>= 2   # Right shift by 2
print(">>= : x >>= 2 →", x)

# <<= operator
x = 3     # 0b0011
x <<= 2   # Left shift by 2
print("<<= : x <<= 2 →", x)
