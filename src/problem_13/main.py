def main():
    res_sum = 0
    with open("src.data", "r") as file:
          for line in file:
              number = int(line.replace("\n", ""))
              res_sum += number

    print(f"result: {str(res_sum)[:10]}")
    print("exit...")


if __name__ == '__main__':
    main()
