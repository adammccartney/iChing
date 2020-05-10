import random
from enum import Enum

"""
iChing.py calculates a hexagram based on coin flips
"""


def flip(numFlips):
    """Assums numFlips is a positive int"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads


"""
Enum class for the different line types 
"""

class Line(Enum):
    yinChange = 6
    yangUnchange = 7
    yinUnchange = 8 
    yangChange = 9

def generateLineValue(numLine):
    """
    Generates a hexagram line
    """
    lineValue = 0
    flipsPerLine = 3
    numHeads = flip(flipsPerLine)
    
    if 4 <= numHeads <= 0:
        return 'Error: lineValue outside range '
    elif numHeads == 0:
        return Line.yinChange
    elif numHeads == 1: 
        return Line.yangUnchange
    elif numHeads == 2:
        return Line.yinUnchange
    elif numHeads == 3:
        return Line.yangChange

class Hexagram(object):

    def __init__(self, linePositions=(1,2,3,4,5,6), lineValues=[]):
        """Creates empty hexagram"""
        self.linePositions = linePositions
        self.lineValues = lineValues
        for linePosition in self.linePositions:
            lineValue = generateLineValue(linePosition)
            self.lineValues.append(lineValue)

    def getLineValues(self):
        return self.lineValues

    def clearLineValues(self):
        self.lineValues = []



