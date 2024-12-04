from src.model.task import Task
from src.view.main_view import MainView

# class TaskController:
#     def __init__(self):
#         self.tasks = []
#         self.tasks.append(Task(1, "Task 1", "This is task 1", "Pending"))
#         self.tasks.append(Task(2, "Task 2", "This is task 2", "Pending"))
#         self.tasks.append(Task(3, "Task 3", "This is task 3", "Pending"))

#     def get_tasks(self):
#         return self.tasks

#     def toggle_task(self, task_id):
#         for task in self.tasks:
#             if task.task_id == task_id:
#                 task.toggle()
#                 break

class MainController:
    def __init__(self, root):
        self.model = Task(1, "Task 1", "This is task 1", "Pending")
        self.view = MainView(root, self)

    def get_data(self):
        data = self.model.get_data()
        self.view.show_data(data)

    def add_task(self):
        print("Adding task...")