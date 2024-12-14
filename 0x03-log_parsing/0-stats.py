#!/usr/bin/python3
# reads stdin line by line and computes metrics

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
cache = {c: 0 for c in status_codes}

total_size = 0
counter = 0

try:
    for l in sys.stdin:
        l_list = l.split(" ")
        if len(l_list) < 7:
            continue
        size = l_list[-1]
        c = l_list[-2]
        if c in cache:
            cache[c] += 1
            total_size += int(size)
            counter += 1

        if counter == 10:
            print("File size: {}".format(total_size))
            for c in sorted(cache.keys()):
                if cache[c] > 0:
                    print("{}: {}".format(c, cache[c]))
            counter = 0

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for c in sorted(cache.keys()):
        if cache[c] > 0:
            print("{}: {}".format(c, cache[c]))
