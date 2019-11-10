#Sort substrings

def sortSubstring(inputString, start, end):
    stringtToSort = ""
    outputString = [None] * len(inputString)
    for strNum in range(0,len(inputString)):
        if strNum >= start and strNum <= end:
            stringtToSort += inputString[strNum]
        else:
            outputString[strNum] = inputString[strNum]

    sortedStringArray = sorted(stringtToSort,reverse=True)

    for str in sortedStringArray:
        outputString[start] = str
        start+=1

    return ''.join(outputString)

print sortSubstring("hlleo",1,3)
