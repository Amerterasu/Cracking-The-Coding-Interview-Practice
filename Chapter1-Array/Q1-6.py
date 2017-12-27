def stringCompression(originalStr):
    compressedStr = ""
    frequency = 1
    #assuming we don't get empty stirngs
    currentChar = originalStr[0]
    
    for i in range(1, len(originalStr)):
        if originalStr[i] != currentChar:
            compressedStr += currentChar + str(frequency)
            frequency = 0
            currentChar = originalStr[i]
        frequency += 1
    
    compressedStr += currentChar + str(frequency)
    if len(compressedStr) < len(originalStr):
        return compressedStr
    else:
        return originalStr
    
print(stringCompression("aabbbccccc"))
print(stringCompression("aabbcc"))
print(stringCompression("aaaaaaaaabbbbbbbbbccccccccc"))