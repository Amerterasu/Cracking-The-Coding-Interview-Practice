def urlify(url, trueLen):
    print("ORIGINAL: {:s}".format(str(url)))
    replaceIndex = len(url) - 1
    originalIndex = trueLen - 1
    
    while originalIndex >= 0:
        if url[originalIndex] != ' ':
            url[replaceIndex] = url[originalIndex]
            replaceIndex -= 1
        elif url[originalIndex] == ' ':
            url[replaceIndex] = '0'
            url[replaceIndex - 1] = '2'
            url[replaceIndex - 2] = '%'
            replaceIndex -= 3
        originalIndex -= 1 
    print("URLIFY:   {:s}".format(str(url)))


urlify(list("ab cd  "), 5)
urlify(list("abc de  "), 6)
urlify(list("a b c    "), 5)
urlify(list(" abc  "), 4)