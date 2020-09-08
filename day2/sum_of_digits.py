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