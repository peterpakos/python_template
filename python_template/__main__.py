#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python Template

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2018 WANdisco

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import, print_function
from python_template.__version__ import __version__

import os
import argparse
from pplogger import get_logger
from ppconfig import Config

__app_name__ = os.path.splitext(__name__)[0].lower()


def parse_args():
    parser = argparse.ArgumentParser(description='Python Template', add_help=False)
    parser.add_argument('--version', action='version', version='%s %s' % (__app_name__, __version__))
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('--debug', action='store_true', dest='debug', help='debugging mode')
    parser.add_argument('--quiet', action='store_true', dest='quiet', help="no console output")
    return parser.parse_args()


def main():
    args = parse_args()
    log = get_logger(debug=args.debug, quiet=args.quiet)
    log.debug(args)

    try:
        config = Config(config_file=__app_name__)
    except IOError as e:
        log.critical(e)
        exit(1)

    log.info('I am just a template, edit me!')


if __name__ == '__main__':
    main()
