import iching 

def test_reading():
    test = iching.Hexagram()
    test.setHexImage()
    reading = test.printHexImage()
    return reading

reading = test_reading()
reading
