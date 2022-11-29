

import string


def isUnique(s: string) -> bool:
    setOfChars = set()
    for i in range(0, len(s)):
        if s[i] in setOfChars:
            return False
        setOfChars.add(s[i])
    return True

def isUniqueNoDataStructures(s: string) -> bool:
    s = sorted(s)
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True


assert isUnique("abcdefg") == True
assert isUnique("") == True
assert isUnique("abcdefga") == False
assert isUnique("abcdeabcde") == False


assert isUniqueNoDataStructures("abcdefg") == True
assert isUniqueNoDataStructures("") == True
assert isUniqueNoDataStructures("abcdefga") == False
assert isUniqueNoDataStructures("abcdeabcde") == False

print("Success!")