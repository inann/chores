#!/bin/python
from task import Task
from task_performer import Task_Performer
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
        Simple round robin styled assignment. This will be run on demand and naively assigns tasks to all the users. It does not take into account existing tasks and does not take into account task duration.
        '''
        if len(self.task_performer_list) == 0:
            print('Need at least one user.')
            sys.exit(1)
        elif len(self.task_performer_list) == 1:
            self.task_performer_to_task_map[self.task_performer_list[0]] = self.task_list
        else:
            current_tp_index = 0
            tp_max_index = len(self.task_performer_list)
            for task in self.task_list:
                current_tp_user = self.task_performer_list[current_tp_index]

                # New Mapping
                if current_tp_user not in self.task_performer_to_task_map:
                    self.task_performer_to_task_map[current_tp_user] = [task]
                else:
                    self.task_performer_to_task_map[current_tp_user].append(task)

                # Handle the Task Performer index, make sure it wraps around
                current_tp_index += 1
                if current_tp_index == tp_max_index:
                    current_tp_index = 0
        for key in self.task_performer_to_task_map.keys():
            for item in self.task_performer_to_task_map[key]:
                print("KEY: " + key.name + ", VALUE: " + item.chore + " " + str(item.frequency))



if __name__ == "__main__":

    th = Task_Handler()

    receiving_tasks = True
    receiving_users = True
    print('Task Handler v 0.00')
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
