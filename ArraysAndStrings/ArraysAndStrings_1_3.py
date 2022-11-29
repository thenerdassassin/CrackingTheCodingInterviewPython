
import string

def replaceChars(s: string, charToReplace: string, charToInsert: string ) -> string:
    return s.replace(charToReplace, charToInsert)

assert replaceChars("abacdaeldafjdla", " ", "%20") == "abacdaeldafjdla"
assert replaceChars("abacdael  dafjdla", " ", "%20") == "abacdael%20%20dafjdla"
assert replaceChars(" abacdaeldaf jdla ", " ", "%20") == "%20abacdaeldaf%20jdla%20"
assert replaceChars(" ", " ", "%20") == "%20"
assert replaceChars("", " ", "%20") == ""

print("Success!")