# Day 8 of 100 Days of Python
# Topic: string indexing and slicing


""" In python indexing is an operator/syntax it provides the index numbers to access
items/sequence using their index"""

# the index value of an object is always one less than to its length.
# example
name = 'Shujaath'
print('Length of name is', len(name))
ni= ('S=0', 'h=1', 'u=2', 'j=3', 'a=4', 'a=5', 't=6', 'h=7')
print(name,ni)
print("reverse",('S=-8', 'h=-7', 'u=-6', 'j=-5', 'a=4', 'a=-3', 't=-2', 'h=-1'),"[Because reverse index number on minus one-1.]")
print("[THIS IS INDEXING IN INDEXING ONLY GET ONE VALUE ]")
print(ni[0])
print(ni[1])
print(ni[2])
print(ni[3])
print(ni[4])
print(ni[5])
print(ni[6])
print(ni[7])
print('name[4]',name[7])
print("[THIS IS SLICING SIMPLE TRICK TO LEARN ONE VALUE IS INDEXING AND TWO OR ABOVE IS SLICING]")
print("name[0:4]",name[0:4],"(start 0 and end always one less than to condition 4 is condition")
print('name[1:7:2]',name[1:7:2])
print('(Using reverse indexing)',name[7:-9:-1],"[ this is normal👉",name[0:8:1],']')


