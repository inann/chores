#!/bin/python

from enum import Enum

class Frequency(Enum):
    DAILY = auto()
    WEEKLY = auto()
    MONTHLY = auto()

    def get_members(self):
        return self.__members__
