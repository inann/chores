#!/bin/python


class Task_Performer:

    def __init__(self, name):
        # TODO: Add capacity
        self.name = name
        self.tasks = []
        self.capacity = 0

    def __repr__(self):
        output = self.name
        task_str = ','.join([task.get_chore() for task in self.tasks])
        output = output + ': ' + task_str
        return output

    def __str__(self):
        output = self.name
        task_str = ','.join([task.get_chore() for task in self.tasks])
        output = output + ': ' + task_str
        return output

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
