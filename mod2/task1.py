# Задача 1. Список процессов.
import sys

way = 'output_file.txt'


def get_summary_rss(str_way):
    with open(str_way, 'r', encoding='UTF8') as f:
        rss = 0
        for i in f.readlines()[1:]:
            rss += int(i.split()[5])
        return round(rss / 1048576, 1)


def main():
    print(get_summary_rss(way))


if __name__ == "__main__":
    main()
