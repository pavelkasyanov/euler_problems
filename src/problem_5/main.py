def ifDividesAll(num):
    for i in (3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19):
        if num % i != 0:
            return False
    return True


def main():
    num = 20
    while True:
        if ifDividesAll(num):
            break
        else:
            num = num + 10
    print(num)


if __name__ == '__main__':
    main()
