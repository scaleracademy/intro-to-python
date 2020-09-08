def print_function():
  print("This function just prints to the screen!")
  
x = print_function() # Function which does not return anything, returns 'None'
print(x)
'''
Output:
This function just prints to the screen!
None
'''

def sum_of_two(num_1, num_2):
  return num_1 + num_2

res = sum_of_two(1, 100)
print(res)

# functions can accept arguments with default values (called as keyword arguments)
def greetings(name="Scaler"):
  print(f"Hello from {name}")

greetings()
greetings("InterviewBit")

# Exercise, complete the following function that returns maximum of three numbers
# def max_of_three(num_1, num_2, num_3)