def main():
    pow_res = 2 ** 1000
    result_sum = 0
    for it in str(pow_res):
        result_sum += int(it)

    print(f"result: {result_sum}")


if __name__ == '__main__':
    main()
