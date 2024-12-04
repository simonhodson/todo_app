class Task:
    def __init__(self, task_id, task_name, task_description, task_status):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = task_status

    def __str__(self):
        return f"Task ID: {self.task_id}, Task Name: {self.task_name}, Task Description: {self.task_description}, Task Status: {self.task_status}"
    
    def toggle(self):
        if self.task_status == "Pending":
            self.task_status = "Done"
        else:
            self.task_status = "Pending"