class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title: str, description: str):
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id: int):
        return self.tasks.get(task_id)

    def list_tasks(self):
        return list(self.tasks.values())

    def update_task_status(self, task_id: int, completed: bool):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = completed
            return True
        return False

    def delete_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
