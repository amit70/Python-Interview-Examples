#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

def setZeroes(A):
    rowZeros = [False] * len(A)
    colZeros = [False] * len(A[0])

    for i in range(0,len(A)):
        for j in range(0,len(A[0])):
            if A[i][j] == 0:
                rowZeros[i] = True
                colZeros[j] = True

    for rowIndex in range(0,len(rowZeros)):
        if rowZeros[rowIndex]:
            for x in range(0,len(A[0])):
                A[rowIndex][x] = 0

    for colIndex in range(0,len(colZeros)):
        if colZeros[colIndex]:
            for y in range(0,len(A)):
                A[y][colIndex] = 0

    # for index in range(0,len(rowZeros)):
    #
    #     for rowIndex in range(0,len(A[0])):
    #         A[rowZeros[index]][rowIndex] = 0
    #
    #     for colIndex in range(0,len(A)):
    #         A[colIndex][colZeros[index]] = 0

    return A

print setZeroes([[1,0,1,1],[1,1,1,1],[1,1,0,1]])
