import time

from euler_lib.utilits import prime_generator, is_prime


def is_truncatable(n: str)-> bool:
    n = str(n)

    for i in range(1, len(n)):
        t = int(n[i:])
        if not is_prime(t):
            return False

        t = int(n[:i])
        if not is_prime(t):
            return False

    return True

def main():
    print("start")
    start = time.clock()

    res_list = []

    for prime in prime_generator(999999):
        if prime < 20:
            continue

        if is_truncatable(prime):
            res_list.append(prime)

        if len(res_list) >= 11:
            break

    print(f"result: {sum(res_list)}")
    print(f"exit, time: {time.clock() - start}")


if __name__ == '__main__':
    main()
