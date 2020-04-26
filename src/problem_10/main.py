def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main():
    num = 2
    result_sum = 0
    while True:
        if is_prime(num):
            print(f"current prime num is {num}")
            result_sum += num

        if num >= 2000000:
            print(f"result sum: {result_sum}")
            break

        num = num + 1


if __name__ == '__main__':
    main()