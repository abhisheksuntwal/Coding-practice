"""
Check if a given string can form a Palindrome

input: "Tact Coa"
Output: True

Explanation: Tact Coa can be rearrqanged as "taco cat" or "atco cta", etc.

Note: we are not considering spaces and case sensitivity into consideration
"""


def checkPalindrome(string):
    """
    First, building frequency counter for all characters.
    Assumption is that it is case insensitive and whitespaces does not count for palindrome

    Checking all the values in frequency counter:
        if all values are even return True
        else if all except one value is even, return True
        else return False
    :param string:
    :return: boolean
    """

    # edge cases:
    if len(string) == 1: return True
    if string == '': return True

    freq = {}

    for char in string:
        if not char.isalnum():
            continue

        char = char.lower()
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    count = 0
    for i in freq.values():
        if i % 2 != 0:
            if count == 1:
                return False
            count += 1

    return True

print(checkPalindrome("abs. SB"))