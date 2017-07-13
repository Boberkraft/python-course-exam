# You are given two lists. Join them to have a list containing elements from both.


def join_two_lists(first_list=[], second_list=[]):
    """
    >>> join_two_lists(['Apple', 2, 1.29], ['orange', 'orange'])
    ['Apple', 2, 1.29, 'orange', 'orange']
    """
    return [el for el in first_list + second_list]


