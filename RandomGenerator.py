from sys import *
from random import *

class RandomGenerator:

    def __init__(self):
        return

    @staticmethod
    def GetRandomFloat(lowBound, topBound):
        local = uniform(0, 1)
        result = local * (topBound - lowBound) + lowBound
        return result
    @staticmethod
    def GetRandomInt(lowBound, topBound):
        local = uniform(0, 1)
        result = int(local * (topBound - lowBound) + lowBound)
        return result
