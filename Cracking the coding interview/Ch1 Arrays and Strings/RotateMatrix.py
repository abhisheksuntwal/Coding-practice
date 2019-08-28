"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

For example:
Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

Same problem also available on Leetcode: Problem number 48[Rotate  Image]
"""


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return matrix

    for layer in range(len(matrix)//2):

        first = layer
        last = len(matrix) - 1 - layer

        for i in range(first, last):
            offset = i - first

            temp = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last - offset][first] = matrix[last][last-offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = temp

    print(matrix)

rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])