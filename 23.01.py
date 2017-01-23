'''
dct = {"one": 1}
try:
    dct[1]
except KeyError:
    try:
        dct[2]
    except KeyError:
        print("Error")
finally:
    print("Kruto")

'''


def get_by_key_perm(dictinary, k):
    if k in dictinary:
        return dictinary[k]
    else:
        print("No key[{}] in dictinary".format(k))


def get_by_key_forg(dictionary, k):
    try:
        return dictinary[k]
    except KeyError:
        print(print("No key[{}] in dictinary".format(k)))
    except IndexError:
        print("dictionary")

