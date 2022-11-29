import string

from numpy import char


def isPalindromePermutation(stringInput: string) -> bool:
    characterCount = {}
    for c in stringInput:
        currentCount = characterCount.get(c)
        if currentCount:
            characterCount.update({c: currentCount+1})
        else:
            characterCount.update({c: 1})
    foundOddChar = False
    for key in characterCount:
        if characterCount[key] % 2 == 0:
            continue
        else:
            if foundOddChar:
                return False
            else:
                foundOddChar = True
    return True

assert(isPalindromePermutation("abb") == True)
assert(isPalindromePermutation("a") == True)
assert(isPalindromePermutation("b") == True)
assert(isPalindromePermutation("abbc") == False)
assert(isPalindromePermutation("aaaaa") == True)
assert(isPalindromePermutation("hhhhhhhhhh") == True)

print("Success!")

