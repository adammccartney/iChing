import iChing

def test_reading():
    test = iChing.Hexagram()
    test.setHexImage()
    reading = test.printHexImage()
    return reading

reading = test_reading()
reading
