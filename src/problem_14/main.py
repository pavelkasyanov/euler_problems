def get_next_collatz_sequence(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def get_collatz_sequence_length(start_value: int) -> int:
    current_collats_seq_val = start_value
    current_len = 1
    while True:
        current_collats_seq_val = get_next_collatz_sequence(current_collats_seq_val)
        current_len += 1

        if current_collats_seq_val == 1:
            return current_len


def main():
    start_val = 1000000 - 1
    max_len = 0
    max_start_value = 0
    while True:
        current_sec_length = get_collatz_sequence_length(start_val)
        if current_sec_length > max_len:
            max_len = current_sec_length
            max_start_value = start_val
        print(f"start value: {start_val}, len: {current_sec_length}")
        start_val -= 1

        if start_val <= 1:
            break
    print(f"max length: {max_len}, start value: {max_start_value}")


if __name__ == '__main__':
    main()
