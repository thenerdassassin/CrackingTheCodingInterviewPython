import string

def isOneAway(firstString: string, secondString: string) -> bool:
    if firstString == secondString:
        return True
    lengthDifference = len(firstString) - len(secondString)

    if lengthDifference > 1 or lengthDifference < -1:
        return False
    
    if lengthDifference == 0:
        return isOneCharChangeAway(firstString, secondString)
    elif lengthDifference > 0:
        return isOneDeletionAway(firstString, secondString)
    elif lengthDifference < 0:
        return isOneDeletionAway(secondString, firstString)

def isOneCharChangeAway(first: string, second: string) -> bool:
    if len(first) != len(second):
        return False
    foundChange = False
    for i in range(0, len(first)):
        if first[i] != second[i]:
            if foundChange:
                return False
            else:
                foundChange = True
    return True

def isOneDeletionAway(longerString: string, shorter: string) -> bool:
    # Assume length assertion is true
    firstIndex = 0
    secondIndex = 0
    while(firstIndex < len(longerString) and secondIndex < len(shorter)):
        if(longerString[firstIndex] != shorter[secondIndex]):
            if(firstIndex != secondIndex):
                return False
            firstIndex += 1
        else:
            firstIndex += 1
            secondIndex += 1
    return True

assert(isOneAway("abc", "abc") == True)
assert(isOneAway("abcd", "abc") == True)
assert(isOneAway("abc", "abcd") == True)
assert(isOneAway("a", "") == True)
assert(isOneAway("", "d") == True)
assert(isOneAway("", "d") == True)
assert(isOneAway("ab", "d") == False)
assert(isOneAway("", "da") == False)
assert(isOneAway("dad", "da") == True)
assert(isOneAway("aa", "da") == True)
assert(isOneAway("abcdef", "abdf") == False)

print("Success!")