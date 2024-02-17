def prime_factors(n):
    """print all the prime factors of n in non-decreasing order
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(858)
    2
    3
    11
    13
    """
    while n > 1:
        smallestPrime = smallestPrimeFactor(n)
        n = n // smallestPrime
        print(smallestPrime)
    # This is the all in one version
    # while n > 1:
    #     k = 2
    #     while n % k != 0:
    #         k += 1
    #     n = n // k
    #     print(k)


def smallestPrimeFactor(n):
    """get the smallest prime Factor.
    >>> smallestPrimeFactor(5)
    5
    >>> smallestPrimeFactor(8)
    2
    """
    i = 2
    while n % i != 0:
        i += 1
    return i
