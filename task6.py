# You are given a list of integers. Sort them in reverse order (largest to smallest)


def sort_reverse(list_of_integers):
    """
    >>> sort_reverse([5,1,2,8])
    [8, 5, 2, 1]
    >>> sort_reverse([7,1,3,10])
    [10, 7, 3, 1]
    """
    return sorted(list_of_integers, reverse=True)

