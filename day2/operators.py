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