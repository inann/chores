#!/bin/python

class Task:
    '''
    Simple class to keep all of the data regarding a specific task together
    Currently only contains the name of the chore and the frequency. Work
    remains to be done in order to create a set number of possible frequency
    values.
    '''
    # Note; There's no need for the extra classes, as tasks should not be
    # executed external to themselves. That is, a task should be able to
    # agnostically execute itself if we're going to treat it as a base
    # class/interface, not only serve to provide information. We don't
    # need beans.
    def __init__(self, chore_name: str):
        self.chore = chore_name
        self.frequency = 'Daily'
        self.finished = False

    def get_frequency(self) -> str:
        return self.frequency
    
    def finish_task(self) -> None:
        self.finished = True

    def is_finished(self) -> bool:
        return self.finished

    def get_chore(self) -> str:
        return self.chore
