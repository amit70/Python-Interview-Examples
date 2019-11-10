#Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(A):
    strNum=''
    output = []
    for n in A:
        strNum+=str(n)
    newNum = int(strNum) + 1

    for x in str(newNum):
        output.append(int(x))

    return output

print plusOne([1,2,3])
