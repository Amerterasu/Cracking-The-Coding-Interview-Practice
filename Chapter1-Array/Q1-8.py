def zeroMatrix (matrix):
    rowSize = len(matrix)
    colSize = len(matrix[0])
    zeroRows = set()
    zeroCols = set()
    for i in range(2):
        for x in range(rowSize):
            for y in range(colSize):
                if matrix[x][y] != 0:
                    if x in zeroRows or y in zeroCols:
                        matrix[x][y] = 0
                else:
                    zeroRows.add(x)
                    zeroCols.add(y)
                    matrix[x][y] = 0
    return matrix

TESTMATRIX = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
print TESTMATRIX
print zeroMatrix(TESTMATRIX)
