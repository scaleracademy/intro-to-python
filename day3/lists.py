# lists: container objects used to store related items together
# let us say you were to input n numbers from user and find their sum, average, etc.
# also you need the ability to sort the numbers etc
# so you need some data type to store them easily, take input and print some required data

number_list = []
number_list = [10, 4, 1, 5]
print(type(number_list))

# 0-based indexing to access elements in the list
# order is retained in the list!
first_num = number_list[0]
last_num = number_list[-1]
print(f"First: {first_num}, Last: {last_num}")

# common methods on lists
print(f"Number list: {number_list}")

num_count = len(number_list)
print(f"Count: {num_count}")

number_list.append(7)
print(f"Appended 7: {number_list}")

number_list.insert(1, 6)
print(f"Insert 6 at index 1: {number_list}")

number_list.pop()
print(f"Removed the last element: {number_list}")

# lists are mutable, can change the elements in-place
# sorting lists, sorted method returns a new list
ordered_num_list = sorted(number_list)
print(f"Ordered number list: {ordered_num_list}")
print(f"Original number list: {number_list}")

# sorting in place, descending order
number_list.sort(reverse=True)
print(f"Original number list: {number_list}")
# reversing a list in-place
number_list.reverse()
print(f"Reversed number list: {number_list}")

# extending one list into another
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 10]
l1.extend(l2)
print(l1)
print(l2)

# checking if an item is present in a list (in keyword)
print(5 in l1)
print(8 in l2)

# split and join
input_str = "1 2 3 4 5 6"
input_list = input_str.split()
print(input_list)

print(','.join(input_list))