def fib(n):
    """compute the nth Fibonacci number, for N >= 1. 0 1 1 2 3 5
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    """
    prev, curr = 0, 1  # 0th and 1st
    i = 1
    while i < n:
        prev, curr = curr, prev + curr
        i += 1
    return curr


"""Generalizing Patterns with Arguments"""
from math import pi, sqrt


def area(r, shape_constant):
    assert r > 0, "A length must be positive"
    return r * r * shape_constant


def area_square(r):
    return area(r, 1)


def area_circle(r):
    return area(r, pi)


def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)


"""Generalization"""


def identity(n):
    return n


def cube(n):
    return pow(n, 3)


from operator import mul


def pi(n):
    return 8 / mul(4 * n - 1, 4 * n - 3)


def summation(n, term):
    """sum the first n terms of a sequences
    >>> summation(3,identity)
    6
    >>> summation(3,cube)
    36
    """
    sum, k = 0, 1
    while k <= n:
        sum, k = sum + term(k), k + 1
    return sum


def sum_naturals(n):
    return summation(n, identity)


def sum_cubes(n):
    return summation(n, cube)


"""Functions as return values"""


def make_adder(n):
    """return a function that takes one argument k and return k + n
    >>> addThree=make_adder(3)
    >>> addThree(4)
    7
    """

    def adder(k):
        return k + n

    return adder


"""lambda expressions"""
square = lambda x: x * x

(lambda x: x * x)(4)

"""lambda expressions versus def statements"""

""" return statements"""


def end(n, d):
    """print the final digits of n in reverse order until d is found.
    >>> end(34567,5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if last == d:
            return None


def search(f):
    x = 0
    while not f(x):
        x += 1
    return x


def is_three(x):
    return x == 3


def inverse(f):
    """return g(y) such that g(f(x))=x
    sqrt(16), hope to get 4,
    how so?
    try square(0) == 16, square(1) == 16
    so we use search() to try.
    then search needs a function to judge:
    lambda x: f(x) == y
    this function need the original function: square as f(x)
    for example, x = 0, f(0) = square(0) != 16,
    so x++, x = 1, try f(1), until x = 4,
    return 4, this is what we need
    """
    return lambda y: search(lambda x: f(x) == y)


sqrt = inverse(square)
sqrt(16)

"""Control"""
x = 0
abs(1 / x if x != 0 else 0)

"""detail of function inverse"""


def x_is_sqrt_of_16(x):
    return square(x) == 16


"""
>>> search(x_is_sqrt_of_16)
4
"""


def sqrt(y):
    def x_is_sqrt_of_y(x):
        return square(x) == y

    search(x_is_sqrt_of_y)


"""as you can see, sqrt and square is a pair of inverse functions,
f(x)=y, find function g, g(y)=x.
"""
def inverse_detail(f):
    def g(y):
        def x_satisfy_fx_equals_y(x):
            return f(x) == y
        """ search will try 0,1,2,3 and use function x_satisfy_fx_equals_y to get the target x"""
        return search(x_satisfy_fx_equals_y)
    return g


sqrt_detail = inverse_detail(square)
"""
>>>
sqrt_detail(16)
4
"""
