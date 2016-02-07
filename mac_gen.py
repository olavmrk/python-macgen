#!/usr/bin/env python
from __future__ import print_function
import argparse
import random

SEPARATORS = {
    'colon': ':',
    'dash': '-',
    'none': '',
    'space': ' ',
}

def parse_args():
    parser = argparse.ArgumentParser(description='Generate random MAC address')
    parser.add_argument('-s', '--separator',
                        choices=sorted(SEPARATORS.keys()), default='colon',
                        help='What separator to use between the bytes in the output.')
    return parser.parse_args()

def main():
    args = parse_args()
    separator = SEPARATORS[args.separator]

    mac = [ random.randint(0, 255) for x in range(0, 6) ]
    mac[0] = (mac[0] & 0xfc) | 0x02
    mac = separator.join([ '{0:02x}'.format(x) for x in mac ])
    print(mac)

if __name__ == '__main__':
    main()
