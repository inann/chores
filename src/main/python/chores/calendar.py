#!/bin/python

from task import Task
from task_performer import Task_Performer
from task_saver import Task_Saver
import sys

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


class Task_Saver:

    def __init__(self, method):
        if method == 'db':
            # TODO database methods
            self.method = 'db'
            # initialize new db connection

        # Expand and add more abstractions as necessary
        else:
            # Default: writes to file
            self.method = 'file'
            self.FILE_NAME = 'saved_tasks.txt'

    def db_save(self, data):
        return 'stub'

    def file_save(self, data):
        return 'stub'

    def save(self, data):
        if self.method == 'db':
            self.db_save(data)
        else:
            # file method
            self.file_save(data)


class Task_Handler:

    def __init__(self):
        self.task_count = 0
        self.task_performer_count = 0
        self.task_list = []
        self.task_performer_list = []
        self.task_performer_to_task_map = {}

    def add_task(self, new_task):
        self.task_count += 1
        self.task_list.append(new_task)

    def add_task_performer(self, person):
        self.task_performer_count += 1
        self.task_performer_list.append(person)

    def assign_tasks(self):
        '''
        Simple round robin styled assignment. This will be run on demand and
        naively assigns tasks to all the users. It does not take into account
        existing tasks and does not take into account task duration.
        '''
        if len(self.task_performer_list) == 0:
            print('Need at least one user.')
            sys.exit(1)
        elif len(self.task_performer_list) == 1:
            for task in self.task_list:
                self.task_performer_list[0].add_task(task)
        else:
            for task in self.task_list:
                cur_user = self.task_list.index(
                    task) % self.task_performer_count
                self.task_performer_list[cur_user].add_task(task)

    def save_tasks(self, method):
        '''
        Save tasks; want to be able to support multiple formats, so should be
        abstracted
        '''
        ts = Task_Saver(method)
        ts.save(self.task_performer_to_task_map)

