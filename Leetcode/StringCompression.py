"""
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Input: ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3"

Input: ["a"]
Output: Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation: Nothing is replaced.

Input: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""

def stringCompression(chars):
    """

    :param chars:
    :return: lenght of modified array
    """

    if len(chars) <= 1:
        return chars

    i = len(chars)-1
    j = i - 1
    counter = 0
    while j >= 0:
        if chars[i] == chars[j]:
            j -= 1
        else:
            counter += 1
            if not i - j == 1:
                temp = j+2
                for x in list(str(i-j)):
                    chars[temp] = str(x)
                    temp += 1
                    counter += 1
                i = j
                j -= 1
            else:
                i = j
                j -= 1

    if not i - j == 1:
        # if len(list(str(i - j))) == 1:
        #     chars[j+2] = str(i-j)
        temp = j + 2
        for x in list(str(i - j)):
            chars[temp] = str(x)
            temp += 1
            counter += 1
    print(chars)
    print(counter+1)
    # for i in chars:




print(stringCompression(["a","a","b","b","c","c","c"]))
print(stringCompression(["a"]))
print(stringCompression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(stringCompression(["a","b","b","b","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","a","b"]))