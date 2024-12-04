import tkinter as tk

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