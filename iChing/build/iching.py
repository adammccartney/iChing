import random
from enum import Enum

"""iChing.py calculates a hexagram based on coin flips

"""


def flip(numFlips):
    """Assums numFlips is a positive int
    
    """
    
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads


class Line(Enum):
    """Enum class for the different line types
     
    """
    yinChange = 6
    yangUnchange = 7
    yinUnchange = 8 
    yangChange = 9

def setLine(numLine):
    """Generates a hexagram line
    
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
        """Creates a hexagram reading

        
        """
        
        self.linePositions = linePositions
        self.castLines = castLines
        self.hexImage = hexImage
        for linePosition in self.linePositions:
            line = setLine(linePosition)
            self.castLines.append(line)

    def getCastLines(self):
        """Returns a list of six Lines

        A Line is an enum class, so has a name and number.
        
        """
        
        return self.castLines

    def clearLines(self):
        """Resets castLines to an empty list
        
        """
        
        self.castLines = []

    def setHexImage(self):
        """Make simple image of hexagram

        Increments the hexImage list with 6 lines
        A line contains 3 chars
        
        """

        for line in self.castLines:
            if line.value == 6:
                changingYinLine = "-o-"
                self.hexImage += changingYinLine
            if line.value == 7:
                yangLine = "---"
                self.hexImage += yangLine
            if line.value == 8:
                yinLine = "- -"
                self.hexImage += yinLine
            if line.value == 9:
                changingYangLine = "-x-"
                self.hexImage += changingYangLine

    def printHexImage(self):
        """Returns set hexagram
        
        """
        
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
