# You are given a string input. Split it into two. If string is uneven make the left part smaller.


def split_string(string_to_split):
    """
    >>> split_string("This python course was awesome")
    ('This python cou', 'rse was awesome')
    >>> split_string("Charlie bit me!")
    ('Charlie', ' bit me!')
    """
    s = string_to_split
    return s[:len(s)//2],  s[len(s)//2:]
