# comparison operators
a = 3
less_than_3 = a < 3
print(less_than_3) # False
print(type(less_than_3)) # <class 'bool'>

# other relational operators: >, >=, ==, !=
print(a == 3) # True
print(a != 3) # False

# logical operators: or, and, not
x = 5
res_one = x < 1 or x > 10
res_two = x >= 1 and x <= 10
print(res_one) # False
print(res_two) # True

user_logged_in = True
print(not user_logged_in)

# the integer 0 is always False, and every other number, is True
x = bool(0)
y = bool(-1)
z = bool(1)
print(x, y, z) # False True True

# strings are compared lexicographically, i.e. by ASCII value of the characters
# you can remeber that capital letters come before lower case ones
print("Scaler" > "Interviewbit") # True as 'S' comes after 'I'
print('s' > 'S') # True
print("Scaler" == "Interviewbit") # False

# Identity comparisons, is keyword is used
# if the compared objects are stored in the same memory location, returns true
a = "Scaler"
b = "Scaler"
print(a is b)
print(id(a))
print(id(b))

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

# Exercise
a = False
b = True
c = True

print (a or b and c)

# Read about operator precedences