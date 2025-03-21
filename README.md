This is a borderline abusive To-Do List cli program.
It's mostly just for fun.
This was a relatively straightforward assignment.

I haven't worked with too many exceptions specifically in python, so getting the handle on it was useful.

**UPDATE** - 3.21.25
Got some feedback to make it more modular, while not quite necessary for a small project, it is good practice.
Further, this could be scaled with a dictionary with input options array and correlating function:

so this portion of handle_choices ---- 
    if choice in ['1', 'a', 'add']: crud.add_item(list_, line_sep)
    if choice in ['2', 'v', 'view']: crud.view_todos(list_, line_sep)
    if choice in ['3', 'r', 'remove']: crud.remove_item(list_, line_sep)

could look something like this:
    options = [ {arr: ['1', 'a', 'add'], func: crud.add_item(), args: [list_, line_sep] }, ETC ]

    for option in options:
        if choice in option[arr]: option[func](**option[args])
    this is pseudocode for sure, but something like this

this could look

Here's the assignment:

In this project, you will build a functional To-Do List Application using Python from scratch. This assignment will help you strengthen your understanding of Python concepts such as syntax, data types, control structures, functions, and error handling, all while creating a practical, interactive command-line application.

Project

In VS Code, create a .py file and complete the following requirements:

User Interface (UI) and Storage Method
Build a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
The tasks should be stored in a Python list
Core Features
Add tasks
View tasks
Delete tasks
Quit the application
User Interaction
Use input() to capture user selections and ensure proper input validation to handle invalid choices.
Error Handling
Implement error handling using try, except, else, and finally blocks to catch errors
Alert the user if they provide invalid input
Alert the user if there are no tasks to view
Alert the user if they try to delete a task that doesn't exist
Alert the user if they select an option on the main menu that doesn't exist
Code Organization
Organize your code into functions to improve clarity and maintainability. 
Use descriptive function names and add comments/docstrings where necessary.
Testing and Debugging
Thoroughly test your application, considering edge cases such as empty lists and invalid input.
Submission Guidelines:
Ensure the code is ready to run and that all functionality, such as loops, conditionals, and functions, works as expected when executed. The goal is to have fully tested and functional code.
Create a GitHub repository to host your project. Add, commit, and push your code to it
Create a README.md on the repository that gives information about your project and how to run/use it
Submit the repository link in Google Classroom.