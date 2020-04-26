NUMBER = 600851475143


def get_factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans


def main():
    factors = get_factor(NUMBER)
    print(f"result: {max(factors)}")


if __name__ == '__main__':
    main()
