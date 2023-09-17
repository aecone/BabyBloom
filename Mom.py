class Mom:
    def __init__(self, name, id, gender, nursing_tasks):
        self.name = name
        self.id = id
        self.gender = gender
        self.nursing_tasks = nursing_tasks

    def get_id(self):
        return self.id

    def get_nursing_tasks(self):
        return self.nursing_tasks
