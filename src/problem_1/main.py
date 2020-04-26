def main():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            print("{} is valid number: add to sum".format(i))
            sum += i
            print("current sum: {}".format(sum))
    print("result sum: {}".format(sum))


if __name__ == '__main__':
    main()
