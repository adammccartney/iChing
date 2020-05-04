import random

def flip(numFlips):
    """Assums numFlips is a positive int"""
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads

def genLine(numLine):
    """
    Generates a hexagram line
    H = 3
    T = 2
    HHH = 9
    HHT = 8
    HTT = 7
    TTT = 6:
    """
    lineValue = 0
    flipsPerLine = 3
    numHeads = flip(flipsPerLine)
    
    if 4 <= numHeads <= 0:
        return 'Error: lineValue outside range '
    elif numHeads == 0:
        lineValue = 6
    elif numHeads == 1: 
        lineValue = 7
    elif numHeads == 2:
        lineValue = 8
    elif numHeads == 3:
        lineValue = 9

    return lineValue

class Hexagram(object):

    def __init__(self, lines=(1,2,3,4,5,6), lineValues=[]):
        """Creates empty hexagram"""
        self.lines = lines
        self.lineValues = lineValues
        for line in self.lines:
            self.lineValues.append(genLine(line))

    def getLineValues(self):
        return self.lineValues

    def printReading(self):
        """ returns a six line string 
            that graphs the line values of the hex
            """ 
        #print(self.lineValues)
        hexCopy = self.lineValues[:]
        hexCopy.reverse()
        #print(hexCopy)
        hexImage = ""
        for lineValue in hexCopy:
            if lineValue == 6:
                line = "-x-\n"
                hexImage += line
            elif lineValue == 7:
                line = "---\n"
                hexImage += line
            elif lineValue == 8:
                line = "- -\n"
                hexImage += line
            elif lineValue == 9:
                line = "-o-\n"
                hexImage += line
        return print(hexImage)
    hexagram.getLineValues(self)



