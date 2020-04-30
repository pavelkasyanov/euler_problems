def is_palindrome(number: int) -> bool:
    str_number = str(number)
    if len(str_number) % 2 != 0:
        return False

    for i in range(0, len(str_number) // 2):
        if str_number[i] != str_number[len(str_number) - i - 1]:
            return False
    return True


def main():
    n1_max = 999
    n2_max = 999
    result = 0

    for n1 in range(1, n1_max):
        for n2 in range(1, n2_max):
            t = n1 * n2
            if is_palindrome(t):
                print(f"t={t} is palindrome for {n1}*{n2}, next")
                if t > result:
                    result = t

    print(f"result: {result}")

    print("exit...")


if __name__ == '__main__':
    main()
