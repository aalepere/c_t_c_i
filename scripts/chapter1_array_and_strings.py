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
