#!/bin/python

class Task:
    '''
    Simple class to keep all of the data regarding a specific task together
    Currently only contains the name of the chore and the frequency. See
    frequency.py for the possible values of the enumeration.
    '''
    def __init__(self, title, frequency):
        self.chore = title
        if checkFrequency(frequency):
            self.frequency = frequency
        else:
            self.frequency = Frequency.DAILY
        self.finished = False

    def checkFrequency(self, frequency):
        member_dict = Frequency.get_members()
        return frequency in member_dict

    def finish_task(self):
        self.finished = True

    
