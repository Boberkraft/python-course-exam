# Create a Car class with an x property. Return an object of class Car with x=1


def make_object():
    """
    >>> c=make_object()
    >>> c.x == 1
    True
    >>> c.__class__.__name__ == 'Car'
    True
    """
    class Car:
        x = 1
    return Car()
