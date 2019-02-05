"""
This is a Python Doc String. The Doc string should exist to describe the overall goal of this particular file.
"""

# Traditional Lists
list = ["a", "b", "c"]
for i in range(0, len(list)):  # Iterates through the list indexes
    print(list[i])

# Nested Lists
nlist = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
]
for i in range(0, len(nlist)):
    for ii in range(0, len(nlist[i])):
        print(nlist[i][ii])

# Traditional Tuples - An immutable list of things
tup = ("a", "b", "c")
for i in range(0, len(tup)):
    print(tup[i])
