# Day 5: File I/O: Reading and Writing Text, CSV, JSON files

## Working with Text Files

- Used to store data such that it can be retrieved any time
- To read or write from a file, the following operations take place:
1. Open a file
2. Perform Read or write operations
3. Close the file

### Open a file

```py
f = open('hello.txt', 'r')
```

- First argument is the string containing file name
- Second argument is the file opening mode. (`r`, `w`, `a`, etc.)
- Default, files are opened in text mode.

### Reading from file

```py
f.read(5) # read next 5 bytes
f.readline() # read the entire line
f.readlines() # read the entire file and return list of lines
f.tell() # get the current file position
f.seek(0) # bring file cursor to initial position
```
### Writing to file

```py
f.write("hello world\n")
```

### Closing a file

- Frees up the resources tied with the file

```py
f.close()
```

- Need to worry about exceptions if any operation on file is running
- Use a `try...finally` block of code

## Open file using context manager

- Need not close the file explicitly

```py
with open('hello.txt') as f:
  # perform file operations
```

## Working with CSV Files

- CSV (Comma Separated Values) format is one of the most simplest ways to store tabular data.
- Elements are separated by a delimiter, generally, a comma `,`.
- The python's `csv` module makes it easier to operate on such files.

### Reading CSV File

```py
import csv
with open('marks.csv', 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)
```

- Explore `skipinitialspace` attribute in the reader function.
- There can be many other attributes specified and can make code difficult to maintain, so to solve this `dialect` is provided as another optional parameter, which groups together many formatting patterns.

### Writing to CSV File

```py
import csv
with open('marks.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(["Roll No.", "Name", "Marks"])
  writer.writerow([1, "abc", 95])
  writer.writerow([2, "def", 97])
```

- You can also try creating rowlist as list of lists and use the `writer.writerows` function.

### Read file as a dictionary

```py
import csv
with open('marks.csv', 'r') as file:
  csv_dict = csv.DictReader(file)
  for row in csv_dict:
    print(row)
```

- Similarly, can try exploring `DictWriter`.
- Also try to explore the `Pandas` library which is a popular library for data manipulation and analysis.

## Working with JSON Files

- Saving more complex data types like nested lists and dictionaries, parsing and serializing becomes complicated.
- Python allows us to use the popular data interchange format JSON (JavaScript Object Notation) through a module `json`.
- Converting python data to string is known as *serializing*.
- Reconstructing the data from the string representation is called *deserializing*.

### Reading json from file

```py
import json
with open('marks.json') as file:
  data = json.load(file)
  print(data) # dict
```

- `json.loads` can be used to convert string to dict.

### Writing json to file

```py
import json

marks_dict = {
  "roll_no": 12,
  "name": "abc",
  "marks": 99
}
with open('marks.json', 'w') as json_file:
  json.dump(marks_dict, json_file)
```

- `json.dumps` can be used to convert dict to string.
- Can pass `indent` and `sort_keys` properties to pretty print the json data.

[Example code](day5/todos.py)

## Other libraries and documentation

- For manipulating path: [pathlib](https://docs.python.org/3/library/pathlib.html) and [os.path](https://docs.python.org/3/library/os.path.html)
- For copying, moving files and other file operations: [shutil](https://docs.python.org/3/library/shutil.html)
- Serializing python objects to disk: [pickle](https://docs.python.org/3/library/pickle.html)
- [Data compression and archiving](https://docs.python.org/3/library/archiving.html)
- [File formats](https://docs.python.org/3/library/fileformats.html)
- [Logging](https://docs.python.org/3/library/logging.html)