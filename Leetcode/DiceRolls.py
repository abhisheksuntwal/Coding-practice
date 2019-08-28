"""
1155. Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.
"""

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        matrix = [[0 for i in range(target+1)] for j in range(d+1)]
        print(matrix)
        matrix[0][0] = 1
        # Iterate over dices
        for i in range(1, d + 1):

            # Iterate over sum
            for j in range(1, target + 1):
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j - 1]
                if j - f - 1 >= 0:
                    matrix[i][j] -= matrix[i - 1][j - f - 1]
        return matrix[d][target] % (10^9 + 7)

sol = Solution()
print(sol.numRollsToTarget(30, 30, 500))