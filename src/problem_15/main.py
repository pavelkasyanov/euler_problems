ROW_COUNT = 21
COL_COUNT = 21


def main():
    matrix = [[0] * COL_COUNT for i in range(ROW_COUNT)]
    for i in range(ROW_COUNT):
        matrix[i][0] = 1
    for j in range(COL_COUNT):
        matrix[0][j] = 1
    for i in range(1, ROW_COUNT):
        for j in range(1, COL_COUNT):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

    print(f"result: {matrix[ROW_COUNT-1][COL_COUNT-1]}")


if __name__ == '__main__':
    main()
