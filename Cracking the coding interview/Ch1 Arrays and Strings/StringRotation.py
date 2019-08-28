"""
Assumeyou have a method isSubstringwhich checks if oneword is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Also Availbale on Leetcode: Problem Number 796
"""

def rotateString(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """

    if not len(A) == len(B):
        return False

    #  Using one of the string to concatenate to itself.
    # So now A = "abcdeabcde"
    #        B = "  cdeab   "   -> Excluding the spaces.
    # if B is a rotation of A or vice-versa, then the concatenated string will contain the other string.
    A += A

    if B in A:
        return True

    return False

print(rotateString("waterbottle", "erbottlewat")) # Output True
print(rotateString('abcde', 'abced'))            # Output False
print(rotateString('abcde', 'cdeab'))             # Output True