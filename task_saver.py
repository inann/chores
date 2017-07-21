#!/bin/python

class Task_Saver:

    def __init__(self, method):
        if method == 'db':
            #TODO database methods
            self.method = 'db'
            #initialize new db connection

        #Expand and add more abstractions as necessary
        else:
            #Default: writes to file
            self.method = 'file'
            self.FILE_NAME = 'saved_tasks.txt'

    def save(data):
        if method == 'db':
            #db_save(data)
            continue()
        else:
            # file method
            file_save(data)

    def file_save(data):
        
