import re
"""
Replace all spaces in a given string by '%20'

example:
Input:   "Mr John Smith    ", 13
Output:  "Mr%20John%20Smith"

Input contains string and length of the string.
Note: Trailing spaces are not considered in the given length=13
"""

# Assumption: If there are multiple spaces between two characters,
# then replace all spaces by just "%20" once

def urlifyViaOnePass(inputStr, length):
    """
    This solution creates a new_string and does one pass over input_string

    Time Complexity: O(n)
    Space Complexity: O(k) where k = n + numberOfSpaces * 2

    :param inputStr:
    :return: resultString
    """
    prev = ''
    curr = ''
    resultStr = ''

    for curr in range(length):
        if inputStr[curr] != ' ':
            resultStr += inputStr[curr]
        else:
            if prev != ' ' and prev != '':
                resultStr += "%20"

        prev = inputStr[curr]

    print(resultStr)



def urlifyViaRegularExp(inputStr, length):
    """
    This solution first stripes the input string of any preceding and trailing spaces
    initialize the "pattern"
    and substitute the pattern with "%20"

    Time Complexity: O(n)
    Space Complexity: O(k) where k = n + numberOfSpaces * 2

    :param inputStr:
    :return: resultString
    """
    inputStr = inputStr.strip()
    pattern = re.compile(r'\s+')
    # print(pattern)
    resultString = re.sub(pattern, '%20', inputStr)

    print(resultString)

urlifyViaOnePass("Mr John Smith     ", 13)
urlifyViaRegularExp("   Mr John   Smith         ", 13)