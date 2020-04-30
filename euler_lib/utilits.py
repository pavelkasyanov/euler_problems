import array


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def sqrt(x):
    assert x >= 0
    i = 1
    while i * i <= x:
        i *= 2
    y = 0
    while i > 0:
        if (y + i) ** 2 <= x:
            y += i
        i //= 2
    return y


def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, sqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True


def prime_generator(limit):
    if limit >= 2:
        yield 2

    isprime = array.array("B", b"\x01" * ((limit - 1) // 2))
    sieveend = sqrt(limit)
    for i in range(len(isprime)):
        if isprime[i] == 1:
            p = i * 2 + 3
            yield p
            if i <= sieveend:
                for j in range((p * p - 3) >> 1, len(isprime), p):
                    isprime[j] = 0
