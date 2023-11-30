#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    dir_name = dir(hidden_4)

    sort_name = [name for name in dir_name if not name.startswith('__')]

    for name in sort_name:
        print(name)
