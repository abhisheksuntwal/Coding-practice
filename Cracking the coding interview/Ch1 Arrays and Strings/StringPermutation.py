import re
"""
Check if the two strings are permutation of each other

"""


class StringPermutation:


    # Function should return False if the lenght of both strings are not same
    def checkPermutationBySorting(self, string1, string2):
        if len(string1) != len(string2):
            return False

        string1 = ''.join(sorted(string1))
        string2 = ''.join(sorted(string2))

        return string1 == string2


    def checkPermutationByCounting(self, string1, string2):
        """
        dictionary implementation which increases the count for each char by 1 for string1
        and then decreases the count of each char by 1 for string2

        if the sum of all values of keys is 0 then the strings are permutation other wise not

        Time Complexity = O(n)
        Space Complexity = O(c) where c is the list of ASCII character
        :return:
        """
        freq = {}

        if len(string1) != len(string2):
            return False

        # incrementing Freq count
        for i in string1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # decrementing Freq count
        for i in string2:
            if i in freq:
                freq[i] -= 1
            else:
                return False    # mismatch at any point returns False


        if sum(freq.values()) == 0:
            return True
        else:
            return False


    # Implementaion, if we are considering that case doesnot matter
    def checkPermutationNeglectingCase(self, string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        return self.checkPermutationBySorting(string1, string2)


    # if we have to trim white spaces and only consider characters for checking permutation
    def checkPermutationExcludingSpaces(self, string1, string2):
        pattern = re.compile(r'\s+')
        string1 = re.sub(pattern, '', string1)
        string2 = re.sub(pattern, '', string2)
        return self.checkPermutationByCounting(string1, string2)

if __name__ == '__main__':

    string1 = 'abCde'
    string2 = 'bcdea'
    sp1 = StringPermutation()

    print(sp1.checkPermutationExcludingSpaces(string1, string2))
    print(sp1.checkPermutationBySorting(string1, string2))
    print(sp1.checkPermutationByCounting(string1, string2))
    print(sp1.checkPermutationNeglectingCase(string1, string2))
