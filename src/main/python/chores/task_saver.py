#!/bin/python


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
