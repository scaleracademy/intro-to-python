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

## Tuples

## Sets

## Dictionaries