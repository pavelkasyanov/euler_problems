import time


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def int_2_bin(n: int) -> str:
    return "{0:b}".format(n)


def is_valid(n: int) -> bool:
    if not is_palindrome(str(n)):
        return False

    b = int_2_bin(n)
    if b[0] == 0:
        return False

    return is_palindrome(b)


def main():
    print("start")
    start = time.clock()

    res = sum(x for x in range(1, 1000000) if is_valid(x))
    print(f"result: {res}")

    print(f"exit, time: {time.clock() - start}")


if __name__ == '__main__':
    main()
