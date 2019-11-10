#Given a matrix, return all elements of the matrix in antidiagonal order

#Input:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# Output:
# [
# [1],
# [2, 4],
# [3, 5, 7],
# [6, 8],
# [9]
# ]

def diagonal(A):
    output = []
    noOfArr = len(A) + len(A[0]) - 1
    for x in range(0, noOfArr):
        outputTemp = []
        output.append(outputTemp)
    startIndex = 0
    for i in range(0,len(A)):
        tempIndex = startIndex
        for j in range(0,len(A[0])):
            output[tempIndex].append(A[i][j])
            tempIndex+=1
        startIndex+=1

    return output

print diagonal([[12, 7, 21, 31, 11],
 [45, -2, 14, 27, 19],
 [-3, 15, 36, 71, 26],
 [4, -13, 55, 34, 15]])
