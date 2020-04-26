def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main():
    num = 2
    current_count = 0
    while True:
        if is_prime(num):
            current_count += 1
            print(f"current num:{num} is_prime")

        if current_count >= 10001:
            print(f"result: {num}")
            break

        num = num + 1
    print(num)


if __name__ == '__main__':
    main()
