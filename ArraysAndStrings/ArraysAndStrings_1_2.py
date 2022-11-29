import string

def isPermutation(first: string, second: string) -> bool:
    charsFound = {}
    for c in first:
        if not c in charsFound:
            charsFound.update({c: 1})
        else:
            currentCount = charsFound.get(c)
            charsFound.update({c: currentCount+1})
    for d in second:
        if not d in charsFound:
            return False
        currentCount = charsFound.get(d)
        if currentCount == 1:
            charsFound.pop(d)
        else:
            charsFound.update({d: currentCount-1})
    return len(charsFound.keys()) == 0

assert isPermutation("", "") == True
assert isPermutation("abc", "cba") == True
assert isPermutation("aaa", "aaa") == True
assert isPermutation("abcdefg", "cbadefg") == True
assert isPermutation("abcd", "cbadefg") == False
assert isPermutation("cbadefg", "abcd") == False
assert isPermutation("cbadefg", "") == False
assert isPermutation("aaa", "xya") == False

print("Success!")

