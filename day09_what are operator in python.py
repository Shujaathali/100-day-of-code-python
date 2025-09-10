# Topic :  What are operators in python???
# Operators in python basically are special symbols or keyword
# that are used to perform operations on variables and values

# There are seven types of operators in python.

# 1. Arithmetic Operators → Used for mathematical calculations [ +  -  *  /  %  **  // ]
print('Arithmetic Operators')
print('5 + 2 ',5 + 2 )  # 7
print('5 - 2 ',5 - 2 )  # 3
print('5 * 2 ',5 * 2 )  # 10
print('5 / 2 ',5 / 2 )  # 2.5
print('5 % 2 ',5 % 2 )  # 1 (remainder)
print('5 ** 2',5 ** 2 )  # 25 (power)
print('5 // 2',5 // 2 )  # 2 (floor division)
print()

# 2. Assignment Operators → Assign values to variables [ =  +=  -=  *=  /=  %=  **=  //= ]
print('Assignment Operators')
x = 5
x += 3   # x = 5 + 3 → 8
x *= 2   # x = 8 * 2 → 16
print("""x = 5
x += 3   # x = 5 + 3 → 8
x *= 2   # x = 8 * 2 → 16""")
print()


# 3. Comparison (Relational) Operators → Compare two values (result: True/False) [ ==  !=  >  <  >=  <= ]
print('Comparison Operators ')
print(5 == 5  , '5 == 5') # True
print(5 != 3  , '5 != 3') # True
print(5 > 3   , '5 > 3 ') # True
print(5 < 3   , '5 < 3 ') # False
print(5 <= 3  , '5 <= 3') # False
print(5 >= 3  , '5 >= 3') # True
print()


# 4. Logical Operators → Combine conditions[ and,  or,  not ]
print('Logical Operators ')
a = 5
b = 10
print(a > 2 and b > 5)  # True
print(a > 10 or b > 5)  # True
print(not(a > 2))       # False
print()


# 5. Identity Operators → Compare memory locations (whether two objects are same) [ is,  is not ]
print('Identity Operators ')
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)     # True (same object)
print(x is z)     # False (same content, different object)
print(x is not z) # True
print()


# 6. Membership Operators → Check if a value exists in a sequence [ in  not in ]
print('Membership Operators')
nums = [1, 2, 3, 4]
print(2 in nums)      # True
print(5 not in nums)  # True
print()


# 7. Bitwise Operators → Work at binary (bit) level [ &  |  ^  ~  <<  >> ]
print('Bitwise Operators')
a = 6   # 110
b = 3   # 011
print(a & b)   # 2 (010)
print(a | b)   # 7 (111)
print(a ^ b)   # 5 (101)
print(~a)      # -7 (2’s complement)
print(a << 1)  # 12 (1100)
print(a >> 1)  # 3 (011)

'''In short:
Operators = tools
Operands = data values on which operators work
👉 Example: 10 + 5 → here + is operator, 10 and 5 are operands.'''