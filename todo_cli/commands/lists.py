import os.path
import json
from datetime import datetime

FILE_NAME = 'lists.json'

def show_lists(args):
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      for index, todo_list in enumerate(data.keys()):
        print(index + 1, data[todo_list]['title'])
    except:
      print('Some error occurred!')

def use_list(args):
  list_name = args[0]
  with open(FILE_NAME, 'r') as lists_json:
    try:
      data = json.load(lists_json)
      if (data.get(list_name)):
        return f'{list_name}.json'
      else:
        return -1
    except:
      print('Some error occurred!')

def create_list(args):
  list_name = args[0]
  # print(os.path.abspath('.'))
  new_list = {}
  with open(FILE_NAME, 'r+') as lists_json:
    try:
      data = json.load(lists_json)
      # print(data)
      # check if file already exists
      if (data.get(list_name)):
        print('List already exists! Try a different name...')
      else:
        # update the new_list dict
        new_list = {
        'title': list_name,
        'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        data[list_name] = new_list
        with open(f'lists/{list_name}.json', 'w') as new_list:
          # empty list
          new_list.write('[\n]')
          print('Successfully created the new list!')
        # add to the lists.json
        lists_json.seek(0)
        json.dump(data, lists_json, sort_keys=True, indent=True)
    except:
      print('Some error occurred!')