def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s = sorted(set(s))
    t = sorted(set(t))
    print(s)
    print(t)
    if(s == t):
        return(True)
    else:
        return(False)


print(isAnagram(s="test", t="sett"))
print(isAnagram(s="anagram", t="nagaram"))
print(isAnagram(s="rat", t="car"))


