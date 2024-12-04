import tkinter as tk
from tkinter import messagebox

# Model
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def toggle(self):
        self.completed = not self.completed


# View
class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        self.root.title("TODO App")
        self.task_label = tk.Label(self.root, text="No tasks yet!")
        self.task_label.pack()

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.controller.add_task)
        self.add_task_button.pack()

    def update_task_label(self, task_title):
        self.task_label.config(text=task_title)


class MessageBox:
    @staticmethod
    def show_info(title, message):
        messagebox.showinfo(title, message)


# Controller
class Controller:
    def __init__(self, root):
        self.model = Task("Sample Task")
        self.view = MainView(root, self)

    def add_task(self):
        self.model.toggle()
        new_status = "Completed" if self.model.completed else "Not Completed"
        self.view.update_task_label(f"{self.model.title}: {new_status}")
        MessageBox.show_info("Task Updated", f"Task is now {new_status}")


# Main
if __name__ == "__main__":
    root = tk.Tk()
    controller = Controller(root)
    root.mainloop()
