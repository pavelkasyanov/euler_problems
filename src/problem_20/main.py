def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    factorial_res = factorial(100)

    sum = 0
    for it in str(factorial_res):
        sum += int(it)

    print(f"result: {sum}")


if __name__ == '__main__':
    main()
