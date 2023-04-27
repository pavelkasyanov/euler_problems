import time

MIN_A = 2
MAX_A = 101

MIN_B = 2
MAX_B = 101


def main():
    print("start")

    start = time.time()

    lst = set(a ** b for a in range(MIN_A, MAX_A) for b in range(MIN_B, MAX_B))

    print(f"result: {len(lst)}, time: {time.time() - start}")

    print("exit")


if __name__ == '__main__':
    main()
