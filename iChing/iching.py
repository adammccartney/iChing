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

def setLine(numLine):
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

    def __init__(self, linePositions=(1,2,3,4,5,6), castLines=[], hexImage=[]):
        """Creates empty hexagram"""
        self.linePositions = linePositions
        self.castLines = castLines
        self.hexImage = hexImage
        for linePosition in self.linePositions:
            line = setLine(linePosition)
            self.castLines.append(line)

    def getCastLines(self):
        """Returns the line values"""
        return self.castLines

    def clearLines(self):
        """Clears the line values"""
        self.castLines = []


    def setHexImage(self):
        """Sets a simple 6 line image of hexagram"""

        for line in self.castLines:
            if line.value == 6:
                changingYinLine = "-x-"
                self.hexImage += changingYinLine
            if line.value == 7:
                yangLine = "---"
                self.hexImage += yangLine
            if line.value == 8:
                yinLine = "- -"
                self.hexImage += yinLine
            if line.value == 9:
                changingYangLine = "-o-"
                self.hexImage += changingYangLine

    def printHexImage(self):
        """Returns set hexagram"""
        listToStr = ''.join([str(line) for line in self.hexImage])
        print(listToStr[:3])
        print(listToStr[3:6])
        print(listToStr[6:9])
        print(listToStr[-9:-6])
        print(listToStr[-6:-3])
        print(listToStr[-3:])
            


if __name__ == '__main__':
    test = Hexagram()
    test.setHexImage()
    test.printHexImage()
