import pathlib
import string

DATA_FILE = pathlib.Path(__file__).parent.resolve() / "names.txt"


def char_position(letter):
    return string.ascii_lowercase.index(letter.lower()) + 1


def name_score(name: str, index: int) -> int:
    sum_ = sum((char_position(x) for x in name if x.isalpha()))
    return sum_ * index


def main():
    with open(DATA_FILE, "r") as f:
        src_names = f.readlines()[0].split(",")

    sorted_names = sorted(src_names)

    index = 1
    score_sum = 0
    for name in sorted_names:
        score = name_score(name, index)
        score_sum += score
        index += 1

    print(f"result_score: {score_sum}")
    print("exit")


if __name__ == '__main__':
    main()
