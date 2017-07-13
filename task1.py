# You get a price (a number). Add 22% tax to it and round it off to 2 decimal places.
from decimal import Decimal

def add_tax(price):
    """
    >>> add_tax(100)
    122.0
    >>> add_tax(6.53)
    7.97
    """
    return round(float(Decimal(str(price)) * Decimal('1.22')), 2)
