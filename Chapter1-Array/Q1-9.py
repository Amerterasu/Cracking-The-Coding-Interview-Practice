def isSubstring(s1, s2):
    if s2 in s1:
        return True
    return False
#should name it isStringRotation because stringRotation doesn't imply a boolean return
def isStringRotation(s1, s2):
    #s1 & s2 are strings
    if len(s1) == len(s2) and len(s1) > 0:
        s1Concat = s1 + s1
        return isSubstring(s1Concat, s2)
    return False

originalString = "waterbottle"
rotatedString = "erbottlewat"
rotatedString2 = "erbottlawat"

result = isStringRotation(originalString, rotatedString)
result2 = isStringRotation(originalString, rotatedString2)
print(result)
print(result2)
    
    