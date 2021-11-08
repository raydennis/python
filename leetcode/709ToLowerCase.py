import unittest
# 709. To Lower Case

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Python utilizes the unicode standard algorithm for case as defined in section 3.13: https://www.unicode.org/versions/Unicode11.0.0/ch03.pdf

# Default Case Conversion
# The following rules specify the default case conversion operations for Unicode strings.
# These rules use the full case conversion operations, Uppercase_Mapping(C), Lowercase_-
# Mapping(C), and Titlecase_Mapping(C), as well as the context-dependent mappings
# based on the casing context, as specified in Table 3-17.
# For a string X:
# R1 toUppercase(X): Map each character C in X to Uppercase_Mapping(C).
# R2 toLowercase(X): Map each character C in X to Lowercase_Mapping(C).
# R3 toTitlecase(X): Find the word boundaries in X according to Unicode Standard
# Annex #29, “Unicode Text Segmentation.” For each word boundary, find the first
# cased character F following the word boundary. If F exists, map F to Titlecase_-
# Mapping(F); then map all characters C between F and the following word boundary to Lowercase_Mapping(C).
# More_Above C is followed by a character of combining class 230 (Above) with no intervening character of combining class 0
# or 230 (Above).
# After C [^\p{ccc=230}\p{ccc=0}]*
# [\p{ccc=230}]
# Before_Dot C is followed by combining dot
# above (U+0307). Any sequence of
# characters with a combining class
# that is neither 0 nor 230 may intervene between the current character
# and the combining dot above.
# After C ([^\p{ccc=230} \p{ccc=0}])*
# [\u0307]
# After_I There is an uppercase I before C, and
# there is no intervening combining
# character class 230 (Above) or 0.
# Before C [I] ([^\p{ccc=230} \p{ccc=0}])*
# Table 3-17. Context Specification for Casing (Continued)
# Context Description Regular Expressions
# The default case conversion operations may be tailored for specific requirements. A common variant, for example, is to make use of simple case conversion, rather than full case
# conversion. Language- or locale-specific tailorings of these rules may also be used.

def toLowerCase(inString):
    # iterate through each character in the string, if it is uppercase, make it lowercase
    return(inString.lower())

class TestToLowerCase(unittest.TestCase):
    # Example 1:
    # Input: "Hello"
    # Output: "hello"
    def testToLowerCaseEx1(self):
        self.assertEqual(toLowerCase("Hello"),"hello")

    # Example 2:
    # Input: "here"
    # Output: "here"
    def testToLowerCaseEx2(self):
        self.assertEqual(toLowerCase("here"),"here")

    # Example 3:
    # Input: "LOVELY"
    # Output: "lovely"
    def testToLowerCaseEx3(self):
        self.assertEqual(toLowerCase("LOVELY"),"lovely")

if __name__ == "__main__":
    unittest.main()