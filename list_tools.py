def all_even(lst):
    return [num for num in lst if num % 2 == 0]

def all_not_multiple(lst, n): 
    return [num for num in lst if num % 2 != 0]

def max_from_2_tuples(tuples): 
    return [max(num) for num in tuples]

def lower_case_words(sentence):
    return str([x.lower() for x in sentence])

def baby_names(names, last_name):
    return str([x + ' ' + last_name for x in names])

if __name__ == "__main__":
    print(baby_names(["Fred", "James"], "Smith"))