class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def is_completed(self):
        return self.completed

    def mark_as_completed(self):
        self.completed = True

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class ToDoList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def mark_task_as_completed(self, title):
        current = self.head
        while current:
            if current.task.get_title() == title:
                current.task.mark_as_completed()
                return
            current = current.next

    def view_todo_list(self):
        current = self.head
        while current:
            print(f"{current.task.get_title()} - {current.task.get_description()} {'✓' if current.task.is_completed() else ''}")
            current = current.next

# Example usage
todo_list = ToDoList()

task1 = Task("Finish assignment", "Complete the LinkedList implementation")
task2 = Task("Grocery shopping", "Buy milk, eggs, and bread")
task3 = Task("Clean room", "Vacuum and organize the room")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

todo_list.mark_task_as_completed("Grocery shopping")

todo_list.view_todo_list()