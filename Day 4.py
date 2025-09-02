#now today is day 4 of 100 day of python coding today we are learning about type casting so what is type casting?
#type casting is a built in function in python and it's help to convert values type 
a="4"
b="6"
print(a+b)#Output is 46

#because we are write 4 and 6 in string so python do concatenate means write 2 strings without any space eg:-
y=12
z=100
print(a+b,y+z)
#When integer your value come's in  string now you use type casating to conver it's type 

print(int(a)+int(b))

'''Primary Type Casting Functions

Numeric types:int() - converts to integer
float() - converts to floating-point numbercomplex() - converts to complex number

Text and sequences:
 str() - converts to strin
 glist() - converts to list
 tuple() - converts to tuple
 set() - converts to set
 frozenset() - converts to frozen set
 
 Other common types:
 bool() - converts to boolean
 dict() - converts to dictionary (from compatible iterables)
 bytes() - converts to bytes object
 bytearray() - converts to bytearray
 
Examples# Numeric conversions
x = int("123")        # "123" → 123
y = float("3.14")     # "3.14" → 3.14
z = str(42)           # 42 → "42"

# Collection conversions
my_list = list("hello")     # "hello" → ['h', 'e', 'l', 'l', 'o']
my_tuple = tuple([1,2,3])   # [1,2,3] → (1, 2, 3)
my_set = set([1,1,2,3])     # [1,1,2,3] → {1, 2, 3}

So there are approximately 10-12 primary type casting functions in Python's built-in functions, though the exact count depends on how you categorize them (some like bytes() and bytearray() are more specialized).'''