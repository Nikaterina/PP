#Задача 2. Средний размер файла.
import sys


def get_main_size(ls_output):
    sum_size_file = 0
    count = 0
    for line in ls_output:
        count += 1
        sum_size_file += int(line.split()[4])
    return round(sum_size_file / count / 1024, 2)


def main():
    data = sys.stdin.readlines()[1:]
    if not data:
        print('There is no data')
    else:
        print(f"Average file size: {get_main_size(data)} KiB")


if __name__ == "__main__":
    main()
