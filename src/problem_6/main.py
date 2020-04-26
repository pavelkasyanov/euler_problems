def main():

    res_1 = 0
    for i in range(1, 101):
        res_1 += i ** 2

    res_2 = 0
    for i in range(1, 101):
        res_2 += i
    res_2 = res_2 ** 2

    print(f"result={res_2 - res_1}")


if __name__ == '__main__':
    main()
