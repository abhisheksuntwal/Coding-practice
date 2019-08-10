"""
Given two strings, write a algorithm to check if the strings are anagrams.

Input: string1 = "anagram", string2 = "nagaram"
Output: true

Input: string1 = "rat", string2 = "car"
Output: false

Input: string1 = "ccaa", string2 = "ccac"
Output: false
"""


class Solution(object):
    def isAnagram(self, string1, string2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(string1) != len(string2):
            return False

        string1 = ''.join(sorted(string1))
        string2 = ''.join(sorted(string2))

        return string1 == string2


