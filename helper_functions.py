from random import randrange, getrandbits
def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# print(generate_prime_number(100))

# def modInverse(a, m) :
#     a = a % m;
#     for x in range(1, m) :
#         if ((a * x) % m == 1) :
#             return x
#     return 1

def modInverse(a, m):  # modular inverse of e modulo phi
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0

    return x


# euler's totient

import numpy as np


# *********************************************************
def phi(n):
    result = n
    p = 2
    while (p * p <= n):

        # Check if prime factor.
        if (n % p == 0):
            # update n
            while (n % p == 0):
                n = n // p
            # result
            result = result * (1.0 - (1.0 / (float)(p)))
        p += 1

    if (n > 1):
        result = result * (1.0 - (1.0 / (float)(n)))

    return (int)(result)

######################## convert to ascii and int

def convert_to_int(text):
    converted = []
    for letter in text:
        converted.append(ord(letter) - 96)
    # print("converted to int: ",converted,len(converted))
    return converted


def convert_to_ascii(text):
    converted = ''
    for number in text:
        converted = converted + chr(number + 96)
    print(converted)
    return converted



