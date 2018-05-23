import math


def add_to_a_list(x, y=[]):
    """
    This is our toy function from the class on functions that we noted had some bugs.
    :param x: the item to append to our list
    :optional y: the list to add to, or return a list of [x] if not passed in

    :return: x appended to y

    >>> x = 2
    >>> list = [1]
    >>> add_to_a_list(x, list)
    [1, 2]
    >>> add_to_a_list(x)
    [2]
    >>> add_to_a_list(x)
    [2]
    """
    y.append(x)
    return y

def get_primes(number):
    '''
    a generator to return primes starting with the given number
    :param number: the number to begin generating primes from
    :return: the next prime

    >>> #We can make any assigments that we could in a normal python interactive session for a doctest!
    >>> gen = get_primes(1)
    >>> next(gen)
    2
    >>> gen = get_primes(2)
    >>> next(gen)
    2
    >>> gen = get_primes(4)
    >>> next(gen)
    5
    >>> next(gen)
    7
    '''
    while True:
        if _is_prime(number):
            yield number
        number += 1

def _is_prime(number):
    '''

    :param number: the number to test
    :return: True if Prime(number) False otherwise

    >>> _is_prime(0)
    False
    >>> _is_prime(-1)
    False
    >>> _is_prime(1)
    False
    >>> _is_prime(2)
    True
    '''
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()