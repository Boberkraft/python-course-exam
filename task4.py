# You are given a list of elements. Pick only elements that are integers and put them in the list.


def pick_integer_numbers_only(my_elements):
    """
    >>> pick_integer_numbers_only(['elephant', 'one', 128, 'even', 256, 1.337, 2, 'spacebook'])
    [128, 256, 2]
    """
    return [el for el in my_elements if isinstance(el, int)]
