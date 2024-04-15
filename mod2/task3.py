#Задача 3. Дешифратор.
# изображение t3.1
import sys
import re


def decrypt(line):
    pat = '\S\.{2}'
    while re.search(pat, line):
        line = re.sub(pat, '', line)
        if line == '':
            return 'Note is empty'
    line = line.split('.')
    return ''.join(line)


def main():
    print(decrypt(sys.stdin.read()))


if __name__ == "__main__":
    main()
