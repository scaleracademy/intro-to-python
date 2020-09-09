# tuples are used to keep track of related but different items
# they are immutable, you cannot change the items in it once created!
# a use-case could be to store a row in a spreadsheet, given that 
# we need read-only snapshot of data

point = ()
# point = collection of x, y and z coordinates!
point = (3, 4, 5)
print(point)
print(type(point))

# checking for existence of an item
print(3 in point)
print(6 in point)

# access item using index as well
print(f"x = {point[0]}, y = {point[1]}, z = {point[2]}")

# point[0] = 10 # TypeError: 'tuple' object does not support this assignment

# to create single item tuple, we need to give a comma after the item
single_element = (1)
print(type(single_element)) # <class 'int'>

single_element = (1, )
print(single_element)
print(type(single_element)) # <class 'tuple'>

# unpacking tuple data
x, y, z = point
print(x, y, z)

# functions can as well return multiple values with the help of tuples