#!/usr/bin/env python
#
# Script description.
#
# Author: First Last <first.last@wandisco.com>

from __future__ import print_function
from sys import stderr, argv
from os import path
from getopt import getopt, GetoptError


class Main(object):
    __version = "1.0"
    __name = path.basename(argv[0])

    def __init__(self):
        self.parse_options()
        print("Hello World!")

    def __del__(self):
        return True

    def parse_options(self):
        options = None

        try:
            options, args = getopt(argv[1:], "hv", [
                "help",
                "version"
            ])
        except GetoptError as err:
            self.die(err)

        for opt, arg in options:
            if opt in ("-v", "--version"):
                self.display_version()
                exit()
            if opt in ("-h", "--help"):
                self.display_usage()
                exit()

    def display_version(self):
        print("%s version %s" % (self.__name, self.__version))

    def display_usage(self):
        self.display_version()
        print("""Usage: %s [OPTIONS]
AVAILABLE OPTIONS:
-h, --help      Print this help summary page
-v, --version   Print version number""" % self.__name)

    @staticmethod
    def die(message=None, code=1):
        if message is not None:
            print(message, file=stderr)
        exit(code)


if __name__ == '__main__':
    app = Main()
