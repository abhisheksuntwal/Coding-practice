"""
Modify the strings (str1 and str2) to check if they are one edit or zero edits away

Examlpe:
pale, ple     -> True       (adding 'a' in str2 is required)
pales, pale   -> True       (deleting 's' in str1 is required)
pale, bale    -> True       (replace 'b' in str2 is required or 'p' in str1)
pale, bake    -> False      (Atleast two changes in str2 is required)
"""

def functionWithSorting(str1, str2):
    """
    Implementation is basically a merge sort where strings are not merged but
    kept track of how many characters are different

    Time Complexity: O(N LogN) due to soring of strings
    Space Complexity: O(1)
    :param str1:
    :param str2:
    :return: boolean
    """

    if abs(len(str1)-len(str2)) > 1:
        return False

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    i = 0
    j = 0
    count = 0

    while (i < len(str1) and j < len(str2)):
        if str1[i] < str2[j]:
            i += 1
            count += 1
        elif str1[i] > str2[j]:
            j += 1
            count += 1
        else:
            i += 1
            j += 1

    if i < len(str1):
        count += len(str1[i:])
    else:
        count += len(str2[j:])

    # count denote number of characters different in two strings.
    # if count == 1 then adding/deleting 1 character to/from a shorter/longer string would make both strings match
    # if count == 2 then replacing one character in either string will make both strings match
    return True if count <= 2 else False

def functionWithDictionary(str1, str2):
    """
    Pass over each string and create a dictionary
    :param str1:
    :param str2:
    :return: boolean
    """

    pass


# print(functionWithDictionary('pale', 'ple'))
# print(functionWithDictionary('pales', 'pale'))
# print(functionWithDictionary('pale', 'bale'))
# print(functionWithDictionary('pale', 'bake'))

print(functionWithSorting('pale', 'ple'))
print(functionWithSorting('paless', 'pale'))
print(functionWithSorting('pale', 'bale'))
print(functionWithSorting('pale', 'bake'))