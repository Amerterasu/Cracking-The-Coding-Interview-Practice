def countDifference(longerStr, shorterStr):
    differenceCount = 0
    shorterIndex = 0
    longerIndex = 0
    while shorterIndex < len(shorterStr):
        if longerStr[longerIndex] != shorterStr[shorterIndex]:
            longerIndex += 1
            differenceCount += 1
            continue
        longerIndex += 1
        shorterIndex += 1
    return differenceCount
def oneAway(originalStr, editedStr):
    #make this an absolute value
    difference = len(editedStr) - len(originalStr)
    
    if difference > 1:
        return False
    
    if len(originalStr) < len(editedStr):
        longerStr = editedStr
        shorterStr = originalStr
        differenceCount = countDifference(longerStr,shorterStr)
    elif len(originalStr) > len(editedStr):
        longerStr = originalStr
        shorterStr = editedStr
        differenceCount = countDifference(longerStr, shorterStr)
    else:
        differenceCount = 0
        for i in range(len(originalStr)):
            if originalStr[i] != editedStr[i]:
                differenceCount += 1
    
        
    if differenceCount > 1:
        return False
    
    return True 

print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "pales"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))
print(oneAway("pale", "pe"))
print(oneAway("pale", "palest"))