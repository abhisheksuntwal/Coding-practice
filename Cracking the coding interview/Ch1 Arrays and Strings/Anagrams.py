"""
Rotate a given N*N
"""


def anagrams(str1, str2):

    if not len(str1) == len(str2):
        return False

    d1 = {x:str1.count(x) for x in str1}
    d2 = {y:str2.count(y) for y in str2}

    for key, value in d1.items():

        if not key in d2.keys():
            if not d2[key] == d1[key]:
                return False

            return False

    return True



print(anagrams("abbd", "badb"))
print(anagrams("abbd", "bad"))
