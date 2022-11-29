import string


def stringCompression(input: string) -> string:
    compressionList = list()
    currentChar = ""
    charRepetitions = 0
    for c in input:
        if c == currentChar:
            charRepetitions += 1
        else:
            if charRepetitions > 0:
                compressionList.append(currentChar)
                compressionList.append(str(charRepetitions))
            currentChar = c
            charRepetitions = 1
    
    compressionList.append(currentChar)
    compressionList.append(str(charRepetitions))

    newString = "".join(compressionList)
    if len(newString) < len(input):
        return newString
    return input

assert(stringCompression("abc") == "abc")
assert(stringCompression("aaa") == "a3")
assert(stringCompression("aabcccccaaa") == "a2b1c5a3")

print("Success!")