def all_even(lst):
    return [num for num in lst if num % 2 == 0]


def all_not_multiple(lst, n):
    return [num for num in lst if (num % n) != 0]


def max_from_2_tuples(tuples):
    if tuples == []:
        return
    pointalist = []
    pointblist = []
    pointalist += (x[0] for x in tuples)
    pointblist += (x[1] for x in tuples)
    maxa = max(pointalist)
    maxb = max(pointblist)
    return (maxa, maxb)


def lower_case_words(sentence):
    if sentence == '':
        return []
    word = ''
    lower = []
    sentence = " ".join(sentence.split())
    for x in sentence:
        if x != ' ':
            word += x.lower()
        else:
            lower += [word]
            word = ''
    lower += [word]
    return lower


def baby_names(names, last_name):
    return [first + ' ' + middle + ' ' + last_name for first in names for middle in names if first != middle]


if __name__ == "__main__":
    print(max_from_2_tuples([(-1, 5), (13, 2)]))
