#!/usr/bin/env python
from __future__ import print_function
import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser(description='Generate random MAC address')
    return parser.parse_args()

def main():
    args = parse_args()
    mac = [ random.randint(0, 255) for x in range(0, 6) ]
    mac[0] = (mac[0] & 0xfc) | 0x02
    mac = ':'.join([ '{0:02x}'.format(x) for x in mac ])
    print(mac)

if __name__ == '__main__':
    main()
