import math

def optional_params(x, y=0):
    return x + y

def optional_params_pitfalls(x, y=[]):
    y.append(x)
    return y


def optional_params_pitfalls_alternate(x, y=None):
    if y is None: y = []
    y.append(x)
    return y

def using_args(*numbers_to_sum):
    return sum(numbers_to_sum)

def using_kwargs(**keywords):
    if "hello" in keywords:
        print("hello {}".format(keywords["hello"]))
    if"goodbye" in keywords:
        print("goodbye {}".format(keywords["goodbye"]))

def get_primes(number):
    while True:
        if _is_prime(number):
            yield number
        number += 1

def _is_prime(number):
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