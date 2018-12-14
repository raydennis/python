import unittest

def romanToInt(numeral):
    """
    :type s: str
    :rtype: int
    """
    tempSum = 0
    total = 0

    i = 0
    while i < len(numeral):
        # if we're looking at the last character
        if(int(i)+1 == len(numeral)):
            if(numeral[i] == 'I'):
                tempSum += 1
            elif(numeral[i] == 'V'):
                tempSum += 5
            elif(numeral[i] == 'X'):
                tempSum += 10
            elif(numeral[i] == 'L'):
                tempSum += 50
            elif(numeral[i] == 'C'):
                tempSum += 100
            elif(numeral[i] == 'D'):
                tempSum += 500
            elif(numeral[i] == 'M'):
                tempSum += 1000
        # I, IV, or IX 
        elif(numeral[i] == 'I'):
            if(numeral[i+1] == 'I'):
                tempSum += 1
            elif(numeral[i+1] == 'V'):
                tempSum += 4
                i+=1
            elif(numeral[i+1] == 'X'):
                tempSum += 9
                i+=1
        # V
        elif(numeral[i] == 'V'):
            tempSum += 5
        # X, XL, or XC
        elif(numeral[i] == 'X'):
            if(numeral[i+1] == 'L'):
                tempSum += 40
                i+=1
            if(numeral[i+1] == 'C'):
                tempSum += 90
                i+=1
        # L
        elif(numeral[i] == 'L'):
            tempSum += 50
        # C, CD, or CM
        elif(numeral[i] == 'C'):
            if(numeral[i+1] == 'D'):
                tempSum += 400
                i+=1
            if(numeral[i+1] == 'M'):
                tempSum += 900
                i+=1
            else:
                tempSum += 100
        # D
        elif(numeral[i] == 'D'):
            tempSum += 500
        # M
        elif(numeral[i] == 'M'):
            tempSum += 1000
        i+=1
    total = tempSum
    tempSum = 0
    return(total)

class TestRomanToInt(unittest.TestCase):
    def testRomanToIntIII(self):
        self.failUnlessEqual(romanToInt('III'),3)
    def testRomanToIntIV(self):
        self.failUnlessEqual(romanToInt('IV'),4)
    def testRomanToIntIX(self):
        self.failUnlessEqual(romanToInt('IX'),9)
    def testRomanToIntLVIII(self):
        self.failUnlessEqual(romanToInt('LVIII'),58)
    def testRomanToIntMCMXCIV(self):
        self.failUnlessEqual(romanToInt('MCMXCIV'),1994)

if __name__ == '__main__':
    unittest.main()
    
# numeral = input("Input a Roman Numeral between the range 1 and 3999: ")
# romanToInt(numeral)