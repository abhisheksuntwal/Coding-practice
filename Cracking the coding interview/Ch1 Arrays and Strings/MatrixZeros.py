"""
Go over a n*n matrix. if a zero is encountered then set row and column to which this element belong to zeors

For example:
Example 1:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Example 2:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

The problem is also available on leetcode: Problem number 73
"""

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modifying matrix in-place instead.
    """
    dummy = 'a'

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for x in range(len(matrix)):
                    if not matrix[x][j] == 0:
                        matrix[x][j] = dummy
                for y in range(len(matrix[0])):
                    if not matrix[i][y] == 0:
                        matrix[i][y] = dummy


    # Replacing "dummy" with the zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == dummy:
                matrix[i][j] = 0

    print(matrix)

setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])
