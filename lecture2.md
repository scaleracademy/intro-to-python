# Day 2: Flow Control

## Day 1 Recap
[Basics of Python: Code](day2/recap.py)

```py
# variables
lecture_day = 2
print(lecture_day)
```

```py
# numbers can be int, float or complex
square_area = 36
circle_area = 6.28
iota = (-1) ** (1/2)
print(square_area, circle_area, iota)
```

```py
# basic mathematical operators
print(square_area + circle_area)
print(4 * square_area)
print(iota/square_area)

# type function
print(type(iota))
```

```py
# strings
greeting = "Hello from Scaler!"
print(greeting)

# f-strings
msg = "Hello from"
name = "Scaler"
print(f"{msg} {name}!")
```

```py
# input from user
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```

```py
# none value
x = None
print(x)
```

## Operators
[Code](day2/operators.py)

### Relational Operators
- comparison operators (<, >, <=, >=)
- Equals (==)
- Not equals (!=)

### Logical Operators
- and
- or
- not

```py
# comparison operators
a = 3
less_than_3 = a < 3
print(less_than_3) # False
print(type(less_than_3)) # <class 'bool'>
```

```py
# other relational operators: >, >=, ==, !=
print(a == 3) # True
print(a != 3) # False
```

```py
# logical operators: or, and, not
x = 5
res_one = x < 1 or x > 10
res_two = x >= 1 and x <= 10
print(res_one) # False
print(res_two) # True

user_logged_in = True
print(not user_logged_in)
```

```py
# the integer 0 is always False, and every other number, is True
x = bool(0)
y = bool(-1)
z = bool(1)
print(x, y, z) # False True True
```

```py
# strings are compared lexicographically, i.e. by ASCII value of the characters
# you can remeber that capital letters come before lower case ones
print("Scaler" > "Interviewbit") # True as 'S' comes after 'I'
print('s' > 'S') # True
print("Scaler" == "Interviewbit") # False
```

```py
# Identity comparisons, is keyword is used
# if the compared objects are stored in the same memory location, returns true
a = "Scaler"
b = "Scaler"
print(a is b)
print(id(a))
print(id(b))
```

```py
# bitwise operators
a = 3
b = 5
c = a & b
'''
Bitwise AND (&)
In result, bit is set at those positions where it is set in both the operands
  011
& 101
  ---
  001
  ---
'''
print(c)
```

```py
# Exercise
a = False
b = True
c = True

print (a or b and c)

# Read about operator precedences
```

## Conditionals

### Codes
- [Basic constructs](day2/conditionals.py)
- [Market example for if elif else](day2/market.py)

### Decision making and constructs

- Decision making statements in programming languages decide the direction of flow of program execution.

- There comes situations in real life when we need to make some decisions and based on these decisions, we decide what should we do next. 

- Similar situations arise in programming also where we need to make some decisions and based on these decision we will execute the next block of code.

- Majorly, the following 3 conditional constructs are used in Python:
    - if
    - else
    - elif

```py
'''
This program checks if a message is rude or polite
A message is rude if the parameter x is less than 1 or greater than 10
'''

x = int(input())

if (x < 1):
  print("Rude message")

if (x > 10):
  print("Rude message")
```

```py
'''
The problem with the above code is redundancy!
A principal rule of programming is to never ever have 
two pieces of code to do the same thing.
It can be improved as shown below:
'''
if (x < 1 or x > 10):
  print("Rude message")

if (x >= 1 and x <= 10):
  print("Polite message")
```

```py
'''
The problem with above code is robustness
what if the condition of rudeness changes and we will have to
rewrite both the conditions above,
we can simplify it using an else construct :)
'''

if (x < 1 or x > 10):
  print("Rude message")
else:
  print("Polite message")
```

```py
# if elif
# say if only x < 1 are rude messages
# from 1 to 10 are polite messages
# and after 10 are other types!
if (x < 1):
  print("Rude messsage")
elif (x >= 1 and x <= 10):
  print("Polite message")
else:
  print("Any other message")
```

```py
vegetable_market = ["onion", "tomato", "broccoli", "cabbage"]

if "carret" in vegetable_market:
  print("Bought carret!")
elif "cabbage" in vegetable_market:
  print("Bought cabbage!")
else:
  print("Came back empty handed...")
```

## Loops

### Codes
- [Loop constructs](day2/loops.py)
- [Sum of digits](day2/sum_of_digits.py)
- [Multiplication tables](day2/multiplication_tables.py)

### Why and how of loops?
- Frequently we want a program to keep doing the same thing over and over again until something happens. That’s called looping.
- Let’s say you are playing a game in which you get a score of 2 points every 1 second as long as you are alive in the game. Is that an example of loop?
- Say you need to print numbers from 1 to 10 to the screen, how will you do it?
- We will see the following 2 types of loops:
    - **for**: It is used when we know how many times our loop body will get executed or can decide it before the loop starts.
    - **while**: It is used when the loop will break upon some condition returning false which we might not be sure when exactly that would happen.
- Nested loops (loop inside a loop) are also required at places, for e.g. consider a train it has multiple compartments, and each compartment has multiple seats, so the ticket checker loops over each compartment, and in each compartment, further loops over each of the seats!

### range function

- `range(n)` includes all numbers from 0 to (n - 1)
- `range(1, n)` includes all numbers from 1 to (n - 1)
- `range(1, n, 2)` includes all numbers from 1 to (n - 1) with a step increment of 2
- You can use `list(range(...))` to show the numbers in the range used.

```py
# print numbers from 1 to 10 to the screen
'''
print(1)
print(2)
...
print(10)

The above is not a good practice since our requirement
might change and we might have to print from 1 to n, where n is the input.
Also, the code is repititive, that is why language provides loop constructs!
'''

# for loops in python do not have initialization, condition, update statement like in other langs
# in keyword is used along with for, to iterate over items in a container or sequence

for n in range(10):
  print(n, end=' ')
print() # by default, end = '\n'
```

```py
# the above code prints '0 1 2 ... 9'
# we want to print '1 2 3 ... 10'

for n in range(1, 11):
  print(n, end=' ')
print()
```

```py
# let us say we want to print all even numbers from 1 to 10

for n in range(2, 11, 2):
  print(n, end=' ')
print()
```

```py
# can use list operator before range, to print the items in the range
print(list(range(2, 11, 2)))
```

```py
# doing the same thing using a while loop
counter = 0
while (counter < 10):
  counter += 1
  print(counter, end=' ')
print()

# NOTE: while loops usually have a statement to update the sentinel value (being checked in condition)
# otherwise the loop can run infinitely, use Ctrl-C to exit the infinite loop
# the loop below runs infinitely

'''
  counter = 0
  while (counter < 10):
    print(counter, end=' ')
'''
```

```py
'''
Program to find sum of digits of a number
'''
n = int(input())

# say n = 1234, how do you compute the sum of the digits?
# you see all the digits, 1, 2, 3, 4, and add them up in a go, boom => 10 is the answer

# How do we program the computer to do this for us?
# We should follow the same technique, right?
# Loop through all the digits, and add them up one by one!
# So, our computer will store the result at some place, we need to create a variable
# Say sum = 0
# How to find a particular digit?
# n = 1234, can we say last digit is the one we get after finding remainder when n is divided by 10
# i.e. n % 10 = 4, add this 4 to the sum, now sum = 4
# Now, we can divide n by 10, to get n' = 1234//10 = 123 (integer division!)
# We continue this process, until n becomes zero!!!
# Pseudocode:
'''
  n = input from user
  sum = 0
  while (n > 0)
    d = last digit of n (i.e. n % 10)
    add d to sum
    divide n by 10
  print(sum)
'''
```

```py
sum = 0
while (n > 0):
  d = n % 10
  sum += d # shorthand for sum = sum + d
  n //= 10 # shorthand for n = n//10
print(sum)

# Try yourself:
# 1. Count digits in a number
# 2. Reverse a number
# 3. Find all factors of a number
```

```py
'''
Program to print multiplication tables of numbers from 1 to n
'''
n = int(input())

for multiple in range(1, 11):
  for number in range(1, n + 1):
    print(number*multiple, end=' ')
  print()

# formatted output
for multiple in range(1, 11):
  for number in range(1, n + 1):
    print("%4d"%(number*multiple), end=' ')
  print()
```

## Jump statements
- break
- continue

## Functions
- Defining functions
- Calling functions
- Function scope
- Recursive functions
