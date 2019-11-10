#Given an array of characters, compress it in-place.

#The length after compression must always be smaller than or equal to the original array.

#Every element of the array should be a character (not int) of length 1.

#After you are done modifying the input array in-place, return the new length of the array.

def stringCompression(strInput):
    outputStr=[]
    count =1
    for index in range(len(strInput)):
        if index < len(strInput) - 1 and strInput[index] == (strInput[index + 1]):
            count+=1
        else:
            outputStr.append(strInput[index])
            outputStr.append(str(count))
            count = 1
    return strInput if len(outputStr) > len(strInput) else "".join(outputStr)

print stringCompression('aabcccccaa')
