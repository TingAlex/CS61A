"""Environments for Higher Order Functions"""


def apply_twice(f, x):
    return f(f(x))


def square(x):
    return x * x


"""Local Names"""
"""Function Composition"""


def triple(x):
    return 3 * x


def compose1(f, g):

    def h(x):
        return f(g(x))

    return h