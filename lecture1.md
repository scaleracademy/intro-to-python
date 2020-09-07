
Installation
------------

- download from https://www.python.org/
- instructions https://realpython.com/installing-python/
- linux:
	```bash
	sudo apt-get update
	sudo apt-get install python3.8 python3-pip
	sudo apt-get install python3-virtualenv
	```
- for now, use repl.it

Python
---------

- Programming language
- General purpose
- Very high level
- Simple, easy to learn, but powerful
- Dynamically typed, but strongly typed (has static type checkers)
- Multi paradigm - supports OOP, functional, procedural, Async
- Excellent tooling - Pycharm, extensions for all major editors, flake8, pylint, black, mypy
- Mature and extensive ecosystem
- Seen mostly in
	- Web Development - django, flask
	- Data Analytics and Machine Learning - numpy, scipy, matplotlib, sklearn, ternsorflow, torch, pandas
	- DevOps & Scripting
	- Distributed Computing - pyspark, dask
- Awesome-Python: [https://github.com/vinta/awesome-python](https://github.com/vinta/awesome-python)

# Basics
```py
2 + 2 * 2 - 2 / 2 // 2 ** 2
10 / 3
10 // 3
5 ** 5
(-1) ** (1/2)
```

```py
width = 20
height = 50
area = width * height
_
x
```

```py
'hello, world'
# escaping special chars, triple quoted, double quoted, f-strings, byte-strings
# comments
```

```py
print('Hello, World!')
x = int(input('Enter number'))
```


```py
x = int(input('Enter number'))
y = int(input('Enter number'))
operator = input('Enter operator')
operator = operator.strip().lower()
if operator == 'add':
    print(f'{x} + {y} = {x+y}')
elif operator == 'power':
    print(f'{x} ^ {y} = {x ** y}')
else:
    print('I don\'t know what to do')
```

```py
classes = ['ds-algo', 'python', 'machine-learning', 'ama']
for c in classes:
	print(c, len(c), c.upper(), c.lower())

# can't use class as a variable name, because it is a keyword
import keyword
keyword.kwlist
```

```py
for i in range(10):
	print(f'Square of {i} is {i**2}')
```

```py
range(10)
range(1, 10)
range(1, 10, -1)
```

```py
classes = ['ds-algo', 'python', 'machine-learning', 'ama']
for index, c in enumerate(classes):
	print(index, c, len(c), c.upper(), c.lower())
```

```py
sum(range(1000))
list(range(1000))
```

```py
while True:
	pass

i = 0
while i < 10:
	print(i)
	i += 1
```

```py
def foo():
	pass

def fib(n):
	if n <= 1: return n
	return fib(n-1) + fib(n-2)

from functools import lru_cache

help()
dir()
a, b = b, a
snake_case
collections.Counter
import math
math.pi
math.e
```

