#Find all the occurence of pattern string in an input string

def zArray(inputString,patterlength):
    outputArr = [0] * len(inputString)
    inputStringPointer = 1

    while inputStringPointer <= len(inputString) - 1:
        leftpointer = 0
        rightpointer = inputStringPointer
        currentcount = 0
        while rightpointer <= len(inputString) - 1:
            if inputString[leftpointer] == inputString[rightpointer]:
                currentcount+=1
                leftpointer+=1
                rightpointer+=1
            else:
                outputArr[inputStringPointer] = currentcount
                if currentcount == patterlength:
                    print "Found at", inputStringPointer - patterlength - 1
                inputStringPointer += 1
                break
        else:
            outputArr[inputStringPointer] = currentcount
            if currentcount == patterlength:
                print "Found at", inputStringPointer - patterlength - 1
            inputStringPointer += 1
    return outputArr


inputstring = "baabaa"
pattern = "aa"

newString = pattern + "$" + inputstring
zArray(newString,len(pattern))
