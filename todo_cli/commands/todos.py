def set_list(list_name):
  if (list_name == ''):
    print('Please select a given list before this action')
    return

def add_item(args):
  set_list(args[0])

def show_items(args):
  set_list(args[0])

def edit_item(args):
  set_list(args[0])

def remove_item(args):
  set_list(args[0])

def complete_item(args):
  set_list(args[0])

def incomplete_item(args):
  set_list(args[0])
