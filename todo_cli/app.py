from commands import commands_dict

def parse(command):
  """
  Takes the command as input and returns the command name and args
  """
  cmd_list = command.split()
  cmd_type = cmd_list[0]
  if (cmd_type == 'help' or cmd_type == 'quit'):
    return cmd_type, []
  elif (cmd_type == 'list'):
    cmd_name = cmd_list[1]
    if (cmd_name in ['show', 'use', 'create']):
      return cmd_name, cmd_list[2:]
    else:
      return 'invalid', []
  elif (cmd_type == 'todo'):
    cmd_name = cmd_list[1]
    if (cmd_name in ['add', 'all', 'edit', 'remove', 'complete', 'incomplete']):
      return cmd_name, cmd_list[2:]
    else:
      return 'invalid', []
  else:
    return 'invalid', []

def main():
  print('Started the Todo application...')
  current_list = ''
  while(1):
    # take the command as input from the user
    command = input('$ ')
    command_name, command_args = parse(command)
    # print(command_name, command_args)
    if (command_name == 'quit'):
      break
    elif (command_name == 'help'):
      with open('help.txt', 'r') as help_file:
        print(help_file.read())
    elif (command_name == 'invalid'):
      print('Please enter a valid command, use help command to display all!')
    elif (command_name == 'use'):
      file_name = commands_dict[command_name](command_args)
      if (file_name == -1):
        print('This is not a valid list name!')
        current_list = ''
      else:
        print('Successfuly chosen this list...')
        current_list = file_name
    elif (command.split()[0] == 'todo'):
      # todo type of command
      command_args.insert(0, current_list)
      commands_dict[command_name](command_args)
    else:
      commands_dict[command_name](command_args)

if __name__ == '__main__':
  main()