def main():
    fn1 = 1
    fn2 = 1
    n = 2
    max = 10 ** (1000 -1)
    while 1:
        n += 1
        fn = fn1 + fn2

        if fn >= max:
            print(f"result: Fn={fn}, index={n}")
            break

        fn2, fn1 = fn1, fn

    print("exit")


if __name__ == '__main__':
    main()
