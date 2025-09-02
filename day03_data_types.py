# Day 3 - Python Built-in Data Types

# In Python, data types are divided into categories.
# Some are mutable (can change), others are immutable (cannot change).

# 1. Numeric Types
integer_example = 123456        # int (immutable)
float_example = 8.6             # float (immutable)
complex_example = 4 + 6j        # complex (immutable)

# 2. Text Type
string_example = "Hello World"  # str (immutable)

# 3. Sequence Types
list_example = [3, 4, 5, 6, 7]        # list (mutable)
tuple_example = (2, 3, 4, 5)          # tuple (immutable)
range_example = range(5)              # range (immutable)

# 4. Set Types
set_example = {2, 3, 4, 5}            # set (mutable)
frozenset_example = frozenset({1, 2, 3})  # frozenset (immutable)

# 5. Mapping Type
dict_example = {"a": 1, "b": 2}       # dict (mutable)

# 6. Boolean Type
boolean_example = True                # bool (immutable)

# 7. Binary Types
bytes_example = b"abc"                # bytes (immutable)
bytearray_example = bytearray(5)      # bytearray (mutable)
memoryview_example = memoryview(b"abc")  # memoryview (mutable)

print("Examples of Python Data Types")
print(type(integer_example), type(string_example), type(list_example))
