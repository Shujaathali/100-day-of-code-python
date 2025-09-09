# Day 7 of 100 Days of Python
# Topic: len() Function

# 👉 The len() function returns the length (number of items) of an object.
# It works with sequences (string, bytes, tuple, list, range)
# and collections (dictionary, set, frozenset).

# Examples:
a = "GeekyShows"                   # String
b = [10, 20, 30]                   # List
c = (10, 20, 30, 40)               # Tuple
d = {10, 20, 30, 40, 50}           # Set
e = {101: 'Rahul', 102: 'Raj', 103: 'Sonam'}  # Dictionary
f = [[10, 20], [30, 40], [60, 70]] # Nested list
g = [(101, 'Rahul', 102, 'Raj', 103, 'Sonam')] # List of tuple
h = b'hello'                       # Bytes
i = frozenset({1, 2, 3})           # Frozenset
j = range(10)                      # Range

print("String:", a, "👉 Length:", len(a))
print("List:", b, "👉 Length:", len(b))
print("Tuple:", c, "👉 Length:", len(c))
print("Set:", d, "👉 Length:", len(d))
print("Dictionary:", e, "👉 Length:", len(e))
print("Nested List:", f, "👉 Length:", len(f))
print("List of Tuple:", g, "👉 Length:", len(g))
print("Bytes:", h, "👉 Length:", len(h))
print("Frozenset:", i, "👉 Length:", len(i))
print("Range:", j, "👉 Converted:", list(j), "Length:", len(j))