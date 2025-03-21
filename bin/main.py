import todo_crud as crud

# globals
todo_list = []
choice = ''
normal_error = 'whoopsy, can you put in a valid choice and try again?'
berate_error = ["You have to type quit. What're you, some kinda dummy?", 'Are you? Are you some dummy-kinda dummy-faced dummy-butt?', 'Like seriously though, are you iliterate? Can I set up some services for you?', "I wanna help you.  You don't have to be dumb.\n"]
line_separator = '----------------------------------------\n'

# 1 time dialog
print("\n\nHey, you're here to get you $#!~ together, and put it in a bag.")
print('So what need to go in your bag?\n')

""" handles choice for add view and remove, also has some funny things if you add quit to the todo list
    left in main to show the equivalent of printed input options, and how they're being handled.
    additional refactorings for scaling could be input_list_options which would be an array of subarrays
    where each subarray would have a string for the option and a corresponding function to call."""
def handle_choice(choice, list_, line_sep):
    choice = choice.lower()
    if choice == 'quit':
        print('Fine, go away, jerk!')
        quit()
    if choice not in ['1', '2', '3', 'a', 'v', 'r', 'add', 'view', 'remove', 'quit']:
        if choice in ['q', '4']:
            raise ValueError(f'{'\n'.join(berate_error)}')
        raise ValueError(f'{normal_error}')
    if choice in ['1', 'a', 'add']: crud.add_item(list_, line_sep)
    if choice in ['2', 'v', 'view']: crud.view_todos(list_, line_sep)
    if choice in ['3', 'r', 'remove']: crud.remove_item(list_, line_sep)

while choice != 'quit':
    print('There are 3 things you can do, and 1 thing you can do to stop doing things:\n')
    print('You can press 1, or a, or add, to add items to your Todo List')
    print('You can press 2, or v, or view, to view your tasks')
    print('You can press 3, or r, or remove, to remove items from your Todo List\n')
    print('You can also quit, you piece of garbage; You can quit and get nothing done.')
    print('Just type quit and press enter. Yeah, you have to type that all the way, you gotta do one thing the whole way today.\n\n')
    print("So, what'll it be?")
    print(line_separator)
    try:
        choice = input('Type your choice and press enter.\n')
        handle_choice(choice, todo_list, line_separator)
    except ValueError as such_a_human_thing_to_do:
        print(f'{such_a_human_thing_to_do}')