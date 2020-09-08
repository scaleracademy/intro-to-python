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

# the above code prints '0 1 2 ... 9'
# we want to print '1 2 3 ... 10'

for n in range(1, 11):
  print(n, end=' ')
print()

# let us say we want to print all even numbers from 1 to 10

for n in range(2, 11, 2):
  print(n, end=' ')
print()

# can use list operator before range, to print the items in the range
print(list(range(2, 11, 2)))

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