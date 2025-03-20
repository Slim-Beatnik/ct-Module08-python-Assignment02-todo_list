# globals
todo_list = []
choice = ''
normal_error = 'whoopsy, can you put in a valid choice and try again?'
berate_error = ["You have to type quit. What're you, some kinda dummy?", 'Are you? Are you some dummy-kinda dummy-faced dummy-butt?', 'Like seriously though, are you iliterate? Can I set up some services for you?', "I wanna help you.  You don't have to be dumb.\n"]
line_separator = '----------------------------------------\n'

# 1 time dialog
print("\n\nHey, you're here to get you $#!~ together, and put it in a bag.")
print('So what need to go in your bag?\n')

# handles choice for add view and remove, also has some funny things if you add quit to the todo list
def handle_choice(choice): #this could be in a different document
    choice = choice.lower()
    if choice == 'quit':
        print('Fine, go away, jerk!')
        quit()
    if choice not in ['1', '2', '3', 'a', 'v', 'r', 'add', 'view', 'remove', 'quit']:
        if choice in ['q', '4']:
            raise ValueError(f'{'\n'.join(berate_error)}')
        raise ValueError(f'{normal_error}')
    if choice in ['1', 'a', 'add']: add_item()
    if choice in ['2', 'v', 'view']: view_todos()
    if choice in ['3', 'r', 'remove']: remove_item()

# helper functions add, view and remove in order
def add_item(): #this could be in a different document
    print("Be careful here because I'm not gonna hold your hand.")
    todo_item = input('So waddaya wanna add to the To-Do list?\n').strip()
    if not todo_item:
        print("You can't even do Nothing with any amount of precision.")
        print('Are you glad you plan to do nothing?... Try again.\n')
        print(line_separator)
        add_item()
    if todo_item.lower() == 'quit':
        print('Fine! You know what, you know what. It is on your list of things to do now...')
    todo_list.append(todo_item)
    print('Here is your updated list:')
    print(line_separator)
    view_todos()
def view_todos(): #this could be in a different document
    if todo_list == []:
        print('You have no tasks. You are a taskless wonder.')
        print('What do you even do all day?')
        print("You know what here's a thing on your list now. F$&%in' this. Here's your list.")
        todo_list.append("F$&*in' this, and do it better.")
    print('Here are your tasks:')
    for i, task in enumerate(todo_list, 1):
        print(f'{i}.\t{task}')
    print(line_separator)
    return
        
def remove_item(): #this could be in a different document
    if not todo_list:
        print("You can't get something from nothing. That's why I'm not expecting much from you.")
        print(line_separator)
        return
    
    print("Here's your list:")
    view_todos()
    
    try:
        delIndex = int(input('Type the number corresponding to the task you want to remove and press enter.\n'))
        if delIndex not in range(1, len(todo_list) + 1):
            raise IndexError("I'm calling your guardian. You need help. Try again.")
    except ValueError:
        print('*sighs heavily for loooooooooooooooooooooong enough to make you uncomfortable*')
        print(line_separator)
        remove_item()
    except IndexError as e:
        print(e)
        print(line_separator)
        remove_item()
    else:
        removed_item = todo_list.pop(delIndex - 1)
        print('I hope this means you finished the task.')
        print(f'"{removed_item}" has been removed.')
    finally:
        print(line_separator)
    

while choice != 'quit':
    print('There are 3 things you can do, and 1 thing you can do to stop doing things:\n')
    print('You can press 1, or a, or add, to add items to your Todo List')
    print('You can press 2, or v, or view, to view your tasks')
    print('You can press 3, or r, or remove, to remove items from your Todo List\n')
    print('You can also quit, you piece of garbage; You can quit and get nothing done.')
    print('Just type quit and press enter. Yeah you have to type that all the way, you gotta do one thing the whole way today.\n\n')
    print("So, what'll it be?")
    print(line_separator)
    try:
        choice = input('Type your choice and press enter.\n')
        handle_choice(choice)
    except ValueError as such_a_human_thing_to_do:
        print(f'{such_a_human_thing_to_do}')