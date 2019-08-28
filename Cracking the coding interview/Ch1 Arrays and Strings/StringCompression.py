"""

"""

def stringCompression(string):
    """
    :param string:
    :return: new result string with count of each character
    """

    # edge cases
    if len(string) <= 1:
        return string

    result = ''

    i = 0
    j = 1

    while j < len(string):

        if string[i] == string[j]:
            j += 1
        else:
            result += string[i] + str(j-i)
            i = j
            j += 1
    result += string[i] + str(j - i)

    # if string is not compressible
    if len([int(x) for x in result[1::2]]) == len(string):
        return string

    return result



if __name__ == '__main__':
    print(stringCompression("aaabbcccccaa"))
    print(stringCompression("abcad"))
    print(stringCompression(""))
    print(stringCompression("a"))
