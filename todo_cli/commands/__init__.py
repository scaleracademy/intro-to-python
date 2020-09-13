import commands.lists
import commands.todos

commands_dict = {
  'show': lists.show_lists,
  'use': lists.use_list,
  'create': lists.create_list,
  'add': todos.add_item,
  'all': todos.show_items,
  'edit': todos.edit_item,
  'remove': todos.remove_item,
  'complete': todos.complete_item,
  'incomplete': todos.incomplete_item
}