# Description
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Note:
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

import unittest

def numJewelsInStones(J, S):
    count = 0
    for i in range(0, len(J)):
        for j in range(0, len(S)):
            if J[i] == S[j]:
                count += 1
    return count

class TestNumJewelsInStones(unittest.TestCase):
    # Example 1:
        # Input: J = "aA", S = "aAAbbbb"
        # Output: 3
    def testNumJewelsInStones1(self):
        self.failUnlessEqual(numJewelsInStones("aA","aAAbbb"),3)
    # Example 2:
        # Input: J = "z", S = "ZZ"
        # Output: 0
    def testNumJewelsInStones2(self):
        self.failUnlessEqual(numJewelsInStones("z","ZZ"),0)

if __name__ == '__main__':
    unittest.main()