import tkinter as tk
from src.controller.main_controller import MainController

if __name__ == '__main__':
    root = tk.Tk()
    controller = MainController(root)
    root.mainloop()
