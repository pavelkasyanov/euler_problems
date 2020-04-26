import math


def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_c_for_a_and_b(a: int, b: int) -> int:
    cc = a ** 2 + b ** 2
    return math.sqrt(cc)


def main():
    for a in range(3, 1000):
        for b in range(4, 1000):
            c = get_c_for_a_and_b(a, b)
            if isInt(c):
                if c + b + a == 1000:
                    print(f"result: {a*b*c}")
                    return


if __name__ == '__main__':
    main()
