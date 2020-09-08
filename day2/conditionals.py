'''
This program checks if a message is rude or polite
A message is rude if the parameter x is less than 1 or greater than 10
'''

x = int(input())

if (x < 1):
  print("Rude message")

if (x > 10):
  print("Rude message")

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