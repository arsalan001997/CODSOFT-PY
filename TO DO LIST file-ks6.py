class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return self.name


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.complete()
                break

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                break

    def list_tasks(self):
        for task in self.tasks:
            if task.completed:
                print(f"{task.name} (completed)")
            else:
                print(task.name)


def add_task_to_list():
    print("Add a task to the list.")
    task_name = input("Task name: ")
    task = Task(task_name)
    todo_list.add_task(task)


def complete_task():
    print("Complete a task on the list.")
    task_name = input("Task name: ")
    todo_list.complete_task(task_name)


def remove_task():
    print("Remove a task from the list.")
    task_name = input("Task name: ")
    todo_list.remove_task(task_name)


def list_tasks():
    print("Tasks in the list:")
    todo_list.list_tasks()


def menu():
    print("""
    Welcome to the "TO DO LIST"!
    Please choose an option:

    1. Add a task to the list.
    2. Complete a task.
    3. Remove a task.
    4. List tasks.
    5. Exit the program.
    """)

    while True:
        try:
            option = int(input("Option: "))
            if option == 1:
                add_task_to_list()
            elif option == 2:
                complete_task()
            elif option == 3:
                remove_task()
            elif option == 4:
                list_tasks()
            elif option == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")


todo_list = ToDoList()
menu()