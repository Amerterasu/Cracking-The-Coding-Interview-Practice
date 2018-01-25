def printEquality(a,b, permutation):
    if permutation:
        print("{:s} EQUALS {:s}".format(a, b))
    else:
        print("{:s} DOES NOT EQUAL {:s}".format(a, b))

def isPermutation(a,b):
    if len(a) != len(b):
        printEquality(a,b, False)
        return
    letterCount = {}
    
    for letter in a:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    
    for letter in b:
        if letter not in letterCount or letterCount[letter] == 0:
            printEquality(a,b, False)
            return
    
    printEquality(a,b, True)

def sortCheck(a,b):
    if len(a) != len(b):
        printEquality(a,b, False)
        return False
    sortedA = sorted(a)
    sortedB = sorted(b)
    
    n = len(a)
    for i in range(n):
        if sortedA[i] != sortedB[i]:
            printEquality(a,b,False)
            return False
    
    printEquality(a,b, True)
    
print("============== HASHMAP VERSION ======================")
isPermutation("hello", "olleh")
isPermutation("hella", "olleh")
isPermutation("hello", "")
isPermutation("hello world", "dlrow olleh")

print("============== SORTING VERSION ======================")
sortCheck("hello", "olleh")
sortCheck("hella", "olleh")
sortCheck("hello", "")
sortCheck("hello world", "dlrow olleh")

