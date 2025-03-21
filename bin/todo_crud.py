# helper functions add, view and remove in order
def add_item(list_, line_sep):
    print("Be careful here because I'm not gonna hold your hand.")
    todo_item = input('So waddaya wanna add to the To-Do list?\n').strip()
    if not todo_item:
        print("You can't even do Nothing with any amount of precision.")
        print('Are you glad you plan to do nothing?... Try again.\n')
        print(line_sep)
        add_item(list_, line_sep)
    if todo_item.lower() == 'quit':
        print('Fine! You know what? You know what?: It is on your list of things to do now...')
    list_.append(todo_item)
    print('Here is your updated list:')
    print(line_sep)
    view_todos(list_, line_sep)
def view_todos(list_, line_sep):
    if list_ == []:
        print('You have no tasks. You are a taskless wonder.')
        print('What do you even do all day?')
        # substitution of curse words for random symbols is called Grawlix
        print("You know what here's a thing on your list now. F$&%in' this. Here's your list.")
        list_.append("F$&*in' this, and do it better.")
    print('Here are your tasks:')
    for i, task in enumerate(list_, 1):
        print(f'{i}.\t{task}')
    print(line_sep)
    return
        
def remove_item(list_, line_sep):
    if not list_:
        print("You can't get something from nothing. That's why I'm not expecting much from you.")
        print(line_sep)
        return
    
    print("Here's your list:")
    view_todos(list_, line_sep)
    
    try:
        delIndex = int(input('Type the number corresponding to the task you want to remove and press enter.\n'))
        if delIndex not in range(1, len(list_) + 1):
            raise IndexError("I'm calling your guardian. You need help. Try again.")
    except ValueError:
        print('*sighs heavily for loooooooooooooooooooooong enough to make you uncomfortable*')
        print(line_sep)
        remove_item()
    except IndexError as e:
        print(e)
        print(line_sep)
        remove_item()
    else:
        removed_item = list_.pop(delIndex - 1)
        print('I hope this means you finished the task.')
        print(f'"{removed_item}" has been removed.')
    finally:
        print(line_sep)