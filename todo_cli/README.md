# Todo Command Line Application

## Create a virtual environment (optional)

Python 3:
```
$ pip3 install virtualenv
$ virtualenv -p python3 venv
```

Activate the environment:

```
source venv/bin/activate
```

## Use cases

- Create a todo list
- Add, Edit and Delete todo items in a todo list
- Mark todo items as complete and incomplete
- Show all todo items in a todo list

## Commands

1. `list show`
2. `list use list_name`
3. `list create list_name`
3. `todo add item_names`
4. `todo all`
5. `todo edit item_id new_item_name`
6. `todo remove item_id`
7. `todo complete item_id`
8. `todo incomplete item_id`
9. `help`
10. `quit`

## JSON Files

### lists.json

- stores a list of todo lists
- a todo list is a dict having title and created_at field

OR

- stores a dict of todo lists having title as key and file name and time of creation as nested dict

### list.json

- list refers to the todo list name
- stores a list of todo item
- each todo item is a dict having title, created_at, and completed field.