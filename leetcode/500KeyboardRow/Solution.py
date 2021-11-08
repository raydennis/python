# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

import unittest

def findWords(words):
    """
    :type words: List[str]
    """
    firstRow = "qwertyuiop"
    secondRow = "asdfghjkl"
    thirdRow = "zxcvbnm" 

    found = []
    
    for word in words:
        # search first row
        for i in range(0, len(word)):
            if word[i].lower() not in firstRow:
                break
            elif i == len(word) - 1:
                found.append(word)
        # search second row
        for i in range(0, len(word)):
            if word[i].lower() not in secondRow:
                break
            elif i == len(word) - 1:
                found.append(word)
        # search third row
        for i in range(0, len(word)):
            if word[i].lower() not in thirdRow:
                break
            elif i == len(word) - 1:
                found.append(word)

    return ( found )


class TestFindWords(unittest.TestCase):
    def testFindWordsFirstRow(self):
        self.failUnlessEqual(findWords(["Tot"]), (["Tot"]))
    def testFindWordsSecondRow(self):
        self.failUnlessEqual(findWords(["Alaska"]), (["Alaska"]))
    def testFindWordsThirdRow(self):
        self.failUnlessEqual(findWords(["BC"]), (["BC"]))
    def testFindWordsAllRows(self):
        self.failUnlessEqual(findWords(["BC", "Hello", "Tot", "Alaska", "Dad", "Peace"]), (["BC", "Tot", "Alaska", "Dad"]))
    # Example:
    # Input: ["Hello", "Alaska", "Dad", "Peace"]
    # Output: ["Alaska", "Dad"]
    def testFindWordsEx1(self):
        self.failUnlessEqual(findWords(["Hello", "Alaska", "Dad", "Peace"]), (["Alaska", "Dad"]))

if __name__ == '__main__':
    unittest.main()