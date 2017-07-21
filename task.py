#!/bin/python
from frequency import Frequency

class Task:
    '''
    Simple class to keep all of the data regarding a specific task together
    Currently only contains the name of the chore and the frequency. See
    frequency.py for the possible values of the enumeration.
    '''
    def __init__(self, title, frequency):
        self.chore = title
        if self.check_frequency(frequency):
            self.frequency = frequency
        else:
            self.frequency = Frequency.DAILY
        self.finished = False

    def check_frequency(self, frequency):
        return frequency in Frequency

    def finish_task(self):
        self.finished = True

    def is_finished(self):
        return self.finished
