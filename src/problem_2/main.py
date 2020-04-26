MAX_FIB_NUMBER = 4 * 1000000


def main():
    result_sum = 2

    n1 = 1
    n2 = 2

    while True:
        print("===   start iteration   ===")
        print("n1={}, n2={}".format(n1, n2))

        n = n1 + n2
        print("n={}".format(n))

        if n > MAX_FIB_NUMBER:
            print("result sum={}".format(result_sum))
            return

        if n % 2 == 0:
            result_sum += n

        n1 = n2
        n2 = n


if __name__ == '__main__':
    main()
