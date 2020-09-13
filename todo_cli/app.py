from commands import commands_dict

def parse(command):
  """
  Takes the command as input and returns the command name and args
  """
  cmd_list = command.split()
  cmd_type = cmd_list[0]
  if (cmd_type == 'help' or cmd_type == 'quit'):
    return cmd_type, []
  elif (cmd_type == 'list' or cmd_type == 'todo'):
    return cmd_list[1], cmd_list[2:]
  else:
    return 'invalid', []

def main():
  print('Started the Todo application...')

  while(1):
    # take the command as input from the user
    command = input()
    command_name, command_args = parse(command)
    print(command_name, command_args)

if __name__ == '__main__':
  main()