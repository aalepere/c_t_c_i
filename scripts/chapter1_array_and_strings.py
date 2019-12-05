"""
Implement an algorithm to determine if a string has all unique characters. What if you
can not use additional data structures?
"""


def check_all_charac_unique(string):
    """ Determine if a string str has all unique characters """
    len_unique_list = len(list(set(string)))
    if len(string) == len_unique_list:
        return True
    else:
        return False


def check_all_charac_unique_no_set(string):
    """ Determine if a string str has all unique characters without using set"""
    test_list = []

    for s in string:
        if s in test_list:
            return False
        else:
            test_list.append(s)
    return True
