def palindromePermutation(str):
    charCount = {}
    numOdd = 0
    
    for char in str:
        if char != ' ':
            if char.lower() in charCount:
                charCount[char.lower()] += 1
            else:
                charCount[char.lower()] = 1
    print(charCount)
    for char in charCount:
        if charCount[char] % 2 != 0:
            numOdd += 1
    
    if numOdd > 1:
        return False
    else:
        return True

print(palindromePermutation("Tact Coa"))