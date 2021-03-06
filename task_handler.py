#!/bin/python
from task import Task
from task_performer import Task_Performer
from task_saver import Task_Saver
import sys


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

    def get_users(self):
        '''
        Return a list of all available users.
        '''
        return self.task_performer_list


if __name__ == "__main__":

    th = Task_Handler()

    receiving_tasks = True
    receiving_users = True
    print('Task Handler v 0.01')
    while(receiving_tasks):
        print('Please enter a task.')
        task_name = input('$: ')
        print('Please enter a frequency.')
        frequency = input('$: ')

        task_to_add = Task(task_name, frequency)
        th.add_task(task_to_add)

        print('Received! Would you like to enter another task? (Y/N)')
        repeat = input('$: ')

        if repeat == 'N' or repeat == 'n':
            receiving_tasks = False

    while(receiving_users):
        print('Please enter a user name')
        user_name = input('$: ')
        print('Entered! Would you like to enter another user? (Y/N)')
        repeat = input('$: ')

        if repeat == 'N' or repeat == 'n':
            receiving_users = False

        user_to_add = Task_Performer(user_name)
        th.add_task_performer(user_to_add)

    th.assign_tasks()

    print('Assigned!')
    for user in th.get_users():
        for task in user.get_tasks():
            print('User: ' + user.get_name())
            print('Task: ' + task.get_chore())
