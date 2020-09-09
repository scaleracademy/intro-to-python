# dict allows us to store data in (key, value) pairs
# themselves are mutable but can contain only immutable types as keys, like sets
# very useful for accessing data based on a key, quickly

# creating empty dict
day_mapping = {}
day_mapping = dict()

# dict with items (key, value) pairs
day_mapping = {
  "Monday": 1,
  "Tuesday": 2,
  "Wednesday": 3,
  "Thursday": 4,
  "Friday": 5,
  "Saturday": 6,
  "Sunday": 0
}
print(len(day_mapping)) # 7

# items can be accessed based on the key, not the index
print(day_mapping["Wednesday"]) # 3
print(day_mapping.get("Sunday"))
print(day_mapping.get("sunday")) # None, because the key is not present

# updating value for a particular key
day_mapping["Sunday"] = 7
# adding another key
day_mapping["Default"] = 0

# keys, values and items
print(day_mapping.keys())
print(day_mapping.values())
print(day_mapping.items())

# removing a particular key
del(day_mapping["Default"])
print(day_mapping.keys())