# sets help to store data in an unsorted way
# an item can only be present once in a set, i.e. no duplicates
# membership test is very fast
# other powerful operations provided are: union, difference and intersection

prime_set = set()
prime_set.add(1)
prime_set.add(2)
prime_set.add(3)
prime_set.add(11)
# order is not preserved in a set
print(f"Prime set: {prime_set}")

# remove an item from a set
prime_set.discard(1)
print(f"Prime set: {prime_set}")

# x = prime_set[0] # cannot access set items using an index
# prime_set.sort() # cannot sort items in a set
# sorted method can still be used as that will convert set to a list

# single element set
s = {1}
print(s)
print(type(s))

s = {}
print(type(s)) # <class 'dict'>
# to create empty set, rather use set constructor
s = set()
print(type(s)) # <class 'set'>

prime_set = {2, 3, 5, 5, 3, 7}
print(prime_set) # duplicate values not present

# sets internally use hashing to store the elements and check if it is present or not
# a numerical value is associated with any item in the set, try using hash() method
# hash() function works only on immutable data types, so you cannot create a set of mutable types

names = {"scaler", "interviewbit", "scaler"}
print(names)
# both the following hash values will come out to be same! although values can change
# depending on when the program is run
print(hash("scaler"))
print(hash("scaler"))

# set_of_lists = {[1, 2, 3], [1, 2, 3, 4]} # TypeError: unhashable type: 'list'

# we can convert a list into a set using the set constructor
names = ["scaler", "interviewbit", "scaler"]
names_set = set(names)
print(names_set)

# update is used to update set with another sequence
prime_set.update(names_set)
print(prime_set)
prime_set.update("scaler")
# since string is a sequence, each of its characters will get added to the set!
print(prime_set)

# union (|), intesection (&), difference (^)