from argparse import ArgumentParser
import os
import random
import re


def random_name(le_set):
    while True:
        s = ''

        for i in range(32):
            r = random.randint(0, 61)

            if r < 10:
                r += 48
            elif r < 36:
                r += 55
            else:
                r += 61

            s += chr(r)

        if s not in le_set:
            return s


def rename(le_set, path, r, a):
    files = os.scandir(path)

    for entry in files:
        if entry.is_dir():
            if r:
                rename(le_set, entry.path, r, a)

            if a:
                old = entry.name

                if not re.match('^[0-9A-Za-z]{32}$', old):
                    new = random_name(le_set)
                    os.rename(entry.path, path + '/' + new)
                    print(old + ' -> ' + new)
                    le_set.remove(old)
                    le_set.add(new)
        else:
            old = entry.name

            if not re.match('^[0-9A-Za-z]{32}(\\..+)?$', old):
                index = old.rfind('.')
                extension = '' if index == -1 else old[index:]
                new = random_name(le_set)
                os.rename(entry.path, path + '/' + new + extension)
                print(old + ' -> ' + new + extension)
                le_set.remove(old[0:index])
                le_set.add(new)


def get_all_names(le_set, path, r, a):
    files = os.scandir(path)

    for entry in files:
        if entry.is_dir():
            if r:
                get_all_names(le_set, entry.path, r, a)

            if a:
                le_set.add(entry.name)
        else:
            index = entry.name.rfind('.')

            if index == -1:
                le_set.add(entry.name)
            else:
                le_set.add(entry.name[0:index])


def main():
    parser = ArgumentParser(description='File name obfuscator')
    parser.add_argument('-a', action='store_true', help='include directories')
    parser.add_argument('-r', action='store_true', help='recursive')
    parser.add_argument('-d', help='directory')
    args = parser.parse_args()
    le_set = set()
    get_all_names(le_set, args.d, args.r, args.a)
    rename(le_set, args.d, args.r, args.a)


if __name__ == '__main__':
    main()
