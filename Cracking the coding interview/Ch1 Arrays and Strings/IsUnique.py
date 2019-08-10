"""
Determine if the given string has repeating characters or not

"""

# Implementation 1: Brute Force

def bruteForce(string):
    """
    Time Complexity: O(n^2)
    Space complexity: O(1)
    :param string:
    :return: boolean
    """
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return True

    return False

print(bruteForce("absjd1244"))
print(bruteForce("qwerty"))


def dictionaryMethod(string):
    """
    Time Complexity: O(n)
    Space complexity: O(c) # Since there a limited set of Characters (like for ASCII it is 256) - c here will be in this range
    :param string:
    :return: boolean
    """
    freq = {}

    for char in string:
        if char in freq:
            return True
        else:
            freq[char] = 1

    # print(freq)
    return False

print(dictionaryMethod("qwerty"))
print(dictionaryMethod("absjd1244"))