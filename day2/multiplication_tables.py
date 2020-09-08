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