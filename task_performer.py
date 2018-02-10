#!/bin/python


class Task_Performer:

    def __init__(self, name):
        # TODO: Add capacity
        self.name = name
        self.tasks = []
        self.capacity = 0

    def add_task(self, task):
        if task is not None:
            self.tasks.append(task)

    def remove_task(self, task):
        if task is not None and task in self.tasks:
            i = self.tasks.index(task)
            del self.tasks[i]

    def get_tasks(self):
        return self.tasks

    def get_name(self):
        return self.name
