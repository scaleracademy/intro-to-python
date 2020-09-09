# Day 3: Basic Data Structures

## Day 2 Recap
[Control Flow: Conditionals, Loops, Jump statements, functions](day3/recap.py)

### Check if given number is a prime

<details>
<summary>
Code
</summary>

```py
"""
program to check if the number (say 'n') given as input is a prime
a prime no. is the one which has only 1 and the numbers itself as its divisors
1 is not a prime no.
eg. n = 2, 3, 5, 7, ...

idea: start a loop from 2 to n/2, if n is divisble by the divisor => not prime
because a no. cannot be divided by a no. > n/2 except n
"""

n = int(input())
checked = 0
for divisor in range(2, n//2 + 1):
  if (n % divisor == 0):
    print("No is not prime!")
    checked = 1
    # no need checking further, can break the loop here itself
    break

# the above code doesn't say that 1 is not a prime because loop won't run even once
# to handle that case, we can add the extra condition:
if (n == 1):
  print("No is not prime!")
  checked = 1

# in cases where checked is false or equal to 0, can say it is prime!
if (not checked):
  print("No is prime!")
```

</details>

### Printing star pattern

<details>
<summary>
Code
</summary>

```py
"""
program to print the following pattern:

*
* *
* * *
* * * *
...

idea: As you can observer, we are looping in two directions, row wise and column wise
1st row has 1 star
2nd row has 2 stars
3rd row has 3 stars and so on...

the outer loop would represent looping over the rows
and in the inner loop, we will loop over the elements in the rows, i.e. columns

Always better to use loop variable 'r' or 'row' for looping on rows
and the loop variable 'c' or 'col' to loop on columns
for easy understanding and debugging of your code !
"""

num_rows = n
for row in range(1, num_rows + 1):
  # r_th row will have r stars
  for col in range(1, row + 1):
    print('*', end=' ')
  # endline
  print('')

# is it possible to do the same thing using one loop, think?

# idea is the same: print 1 char in 1st row, 2 chars in 2nd row, ...
line_num = 1
printed_on_cur_row = 0
while (line_num <= num_rows):
  if (printed_on_cur_row < line_num):
    print('*', end=' ')
    printed_on_cur_row += 1
  else:
    print('')
    # reset count of stars on cur_row to be zero
    printed_on_cur_row = 0
    # increment the line_num, i.e. move to next row
    line_num += 1
```

</details>

### Find max of three numbers

<details>
<summary>
Function 1
</summary>

```py
"""
function to return maximum of three numbers

idea: let numbers be a, b, c
when can a be the max? when a >= b and a >= c
similarly for b and c
so, write three conditions, and return the answer if that condition is true
also, you can use if elif else as well!
"""

def maximum_of_three(num_one, num_two, num_three):
  if (num_one >= num_two and num_one >= num_three):
    return num_one
  if (num_two >= num_one and num_two >= num_three):
    return num_two
  if (num_three >= num_one and num_three >= num_two):
    return num_three
  return -1

n1 = 3
n2 = 7
n3 = 1

res = maximum_of_three(n1, n2, n3)
print(res)
```

</details>

<details>
<summary>
Function 2
</summary>

```py
# idea: assign max = a, now check if b >= max, max = b, again if c >= max, max = c
def maximum_of_three_simple(n1, n2, n3):
  maxi = n1
  if (n2 >= maxi):
    maxi = n2
  if (n3 >= maxi):
    maxi = n3
  return maxi

res = maximum_of_three(n1, n2, n3)
print(res)
```

</details>

## More on Functions
[Code](day3/functions.py)

### Keyword Arguments and Positional Arguments
- A function can have two types of arguments: ones with default values and those without it.
- The arguments which have a default value are termed as `keyword arguments` and required ones are `positional arguments`.
- These arguments should always be the last ones, i.e. All the *required (positional) arguments go first*. They are then *followed by the optional keyword arguments*.
- Arguments without defaults are required otherwise you get a syntax error.
- You can pass in none, some or all of the keyword arguments.
- You can pass in parameters by keyword (name defined for argument).

<details>
<summary>
Function with keyword arguments (code)
</summary>

```py
# for eg the print function we use has 'sep' as a keyword argument which is '\n' by default

# below is also a way you can document your function using docstrings
def distance_travelled(t, u = 0, g = 9.81):
  """
  Function distance_travelled calculates the distance travelled by an object
  with initial speed u, in a time interval of t, where acceleration due to gravity is g

  input: t (time taken), u (initial speed) g (acceleration due to gravity)
  output: distance travelled

  Example: 
      >>> distance_travelled(1.0)

          4.905
  """
  d = u*t + 0.5 * g * t**2
  return d

print(distance_travelled(2.0))
print(distance_travelled(2.0, u = 1.0))
print(distance_travelled(2.0, g = 9.7))
print(distance_travelled(g = 9.7, t = 2.0))
```

</details>

### Function scope

```py
# scope inside a function is different than the one outside it
# inside function scope, you can access the outer scope variables but cannot change them

def set_name(input_name):
  name = input_name
  print(f"Name inside the function: {name}")

set_name("Scaler")
# print(name) # NameError: this variable is not defined
```

### Exercise

<details>
<summary>
Guess output of the code
</summary>

```py
# Exercise: What should be the output for this piece of code?
# NEVER USE ARGUMENTS WITH LISTS AS DEFAULT VALUES!!!
def add_char_to_list(char, lst = []):
  lst.append(char)
  return lst
add_char_to_list('s')
add_char_to_list('c')
add_char_to_list('a')
add_char_to_list('l')
add_char_to_list('e')
print(''.join(add_char_to_list('r')))
```

</details>

## Containers

- [Lists](day3/lists.py)
- [Tuples](day3/tuples.py)
- [Sets](day3/sets.py)
- [Dictionaries](day3/dictionaries.py)

## Lists

```py
# lists: container objects used to store related items together
# let us say you were to input n numbers from user and find their sum, average, etc.
# also you need the ability to sort the numbers etc
# so you need some data type to store them easily, take input and print some required data

number_list = []
number_list = [10, 4, 1, 5]
print(type(number_list))
```

```py
# 0-based indexing to access elements in the list
# order is retained in the list!
first_num = number_list[0]
last_num = number_list[-1]
print(f"First: {first_num}, Last: {last_num}")
```

```py
# common methods on lists
print(f"Number list: {number_list}")

num_count = len(number_list)
print(f"Count: {num_count}")

number_list.append(7)
print(f"Appended 7: {number_list}")

number_list.insert(1, 6)
print(f"Insert 6 at index 1: {number_list}")

number_list.pop()
print(f"Removed the last element: {number_list}")
```

```py
# lists are mutable, can change the elements in-place
# sorting lists, sorted method returns a new list
ordered_num_list = sorted(number_list)
print(f"Ordered number list: {ordered_num_list}")
print(f"Original number list: {number_list}")

# sorting in place, descending order
number_list.sort(reverse=True)
print(f"Original number list: {number_list}")
# reversing a list in-place
number_list.reverse()
print(f"Reversed number list: {number_list}")
```

```py
# extending one list into another
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 10]
l1.extend(l2)
print(l1)
print(l2)
```

```py
# checking if an item is present in a list (in keyword)
print(5 in l1)
print(8 in l2)
```

```py
# split and join
input_str = "1 2 3 4 5 6"
input_list = input_str.split()
print(input_list)

print(','.join(input_list))
```

## Tuples

```py
# tuples are used to keep track of related but different items
# they are immutable, you cannot change the items in it once created!
# a use-case could be to store a row in a spreadsheet, given that 
# we need read-only snapshot of data

point = ()
# point = collection of x, y and z coordinates!
point = (3, 4, 5)
print(point)
print(type(point))
```

```py
# checking for existence of an item
print(3 in point)
print(6 in point)
```

```py

# access item using index as well
print(f"x = {point[0]}, y = {point[1]}, z = {point[2]}")

# point[0] = 10 # TypeError: 'tuple' object does not support this assignment
```

```py
# to create single item tuple, we need to give a comma after the item
single_element = (1)
print(type(single_element)) # <class 'int'>

single_element = (1, )
print(single_element)
print(type(single_element)) # <class 'tuple'>
```

```py
# unpacking tuple data
x, y, z = point
print(x, y, z)

# functions can as well return multiple values with the help of tuples
```

## Sets

```py
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
```

```py
# remove an item from a set
prime_set.discard(1)
print(f"Prime set: {prime_set}")
```

```py
# x = prime_set[0] # cannot access set items using an index
# prime_set.sort() # cannot sort items in a set
# sorted method can still be used as that will convert set to a list
```

```py
# single element set
s = {1}
print(s)
print(type(s))

s = {}
print(type(s)) # <class 'dict'>
# to create empty set, rather use set constructor
s = set()
print(type(s)) # <class 'set'>
```

```py
prime_set = {2, 3, 5, 5, 3, 7}
print(prime_set) # duplicate values not present
```

```py
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
```

```py
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
```

## Dictionaries

- Let us say we need to store names, courses and grade details for students
- Storing separate lists for each of them would become difficult to keep track of
- Also retrieving data will also be not that efficient
- It is always better to use a single data structure to store similar data
- We can use a dictionary here, which has the student name as the key!
- Lists have an order based on the index but dict doesn't guarantee any order.
- You could write a program to find the most frequent word in a huge text file very easily using dict!

```py
# dict allows us to store data in (key, value) pairs
# themselves are mutable but can contain only immutable types as keys, like sets
# very useful for accessing data based on a key, quickly

# creating empty dict
day_mapping = {}
day_mapping = dict()
```

```py
# dict with items (key, value) pairs
day_mapping = {
  "Monday": 1,
  "Tuesday": 2,
  "Wednesday": 3,
  "Thursday": 4,
  "Friday": 5,
  "Saturday": 6,
  "Sunday": 0
}
print(len(day_mapping)) # 7
```

```py
# items can be accessed based on the key, not the index
print(day_mapping["Wednesday"]) # 3
print(day_mapping.get("Sunday"))
print(day_mapping.get("sunday")) # None, because the key is not present
```

```py
# updating value for a particular key
day_mapping["Sunday"] = 7
# adding another key
day_mapping["Default"] = 0
```

```py
# keys, values and items
print(day_mapping.keys())
print(day_mapping.values())
print(day_mapping.items())

# removing a particular key
del(day_mapping["Default"])
print(day_mapping.keys())
```

## Mutability Summary
- Basic Types: `int`, `float`, `decimal`, `str`, `bool` all are immutable
- Container Types: `list`, `set` and `dict` are mutable while `tuple` is not