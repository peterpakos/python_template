#!/usr/bin/env python
#
# Script description.
#
# Author: First Last <first.last@wandisco.com>

from __future__ import print_function
from sys import stderr, argv
from os import path
from argparse import ArgumentParser


class Main(object):
    __version = '1.0'
    __name = path.basename(argv[0])

    def __init__(self):
        self.parse_args()
        print('Hello World!')

    def __del__(self):
        return True

    def parse_args(self):
        parser = ArgumentParser()
        parser.add_argument('-v', '--version',
                            help='show version', action="store_true")
        args = parser.parse_args()
        if args.version:
            self.display_version()
            exit()

    def display_version(self):
        print('%s version %s' % (self.__name, self.__version))

    @staticmethod
    def die(message=None, code=1):
        if message is not None:
            print(message, file=stderr)
        exit(code)


if __name__ == '__main__':
    app = Main()
