import pathlib
import string
import time

DATA_FILE = pathlib.Path(__file__).parent.resolve() / "names.txt"


def char_position(letter):
    return string.ascii_lowercase.index(letter.lower()) + 1


def main():
    print("start")
    start = time.time()

    with open(DATA_FILE, "r") as f:
        src_names = f.readlines()[0].split(",")

    triangle_numbers_sum = 0

    coded_triangle_numbers = [int(0.5 * n * (n + 1)) for n in range(1, 1001)]

    for name in src_names:
        score = sum((char_position(x) for x in name if x.isalpha()))

        if score in coded_triangle_numbers:
            triangle_numbers_sum += 1

    print(f"result_score: {triangle_numbers_sum}")

    print(f"exit, time: {time.time() - start}")


if __name__ == '__main__':
    main()
