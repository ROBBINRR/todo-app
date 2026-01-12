#from functions import get_todos, write_todos
import functions
import time

#todos = []
now = time.strftime("%b-%d-%Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    #match user_action:

        # Check if user action is "Add"
    #if "add" in user_action or "new" in user_action :
    if user_action.startswith("add"):
        # todo = input("Enter a todo:") + "\n"
        todo = user_action[4:]

        """
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        """

        todos = functions.get_todos()
        todos.append(todo + '\n')

        """
        file = open("todos.txt", "w")
        file.writelines(todos)
        file.close()
        """
        functions.write_todos(todos)


    #case "show"  | "display":
    #elif 'show' in user_action:
    elif user_action.startswith("show"):

        """
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        """

        todos = functions.get_todos()

        # Delete el salto de linea
        """ 
        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        """

        # Delete el salto de linea
        # Compression de lista
        # new_todos = [ item.strip('\n') for item in todos ]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)
        print(f"Length  is {index + 1}")

    #elif "edit" in user_action:
    elif user_action.startswith("edit"):
        try:
            #number = int(input("Enter numbr of the todos to edit: "))
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            mew_todo = input("Enter new todo: ")
            todos[number] = mew_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input")
            continue

    #elif "complete" in user_action:
    elif user_action.startswith("complete"):

        try:
            #number = int(input("Enter numbr of the todos to complete:"))
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError or ValueError:
            print("There is item with that index")
            continue

    #elif "exit" in user_action:
    elif user_action.startswith("exit"):
        break

    else:
        print("Comando no valido..")

    #case _:
    #    print("Hey, you entered an unknown command.")

print("By")



