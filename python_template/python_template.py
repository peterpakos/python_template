# -*- coding: utf-8 -*-
"""Python project template

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

from __future__ import print_function
from . import __version__

import os
import argparse
from pplogger import get_logger
from ppconfig import Config

__app_name__ = os.path.splitext(__name__)[0].lower()

parser = argparse.ArgumentParser(description='Python project template', add_help=False)
parser.add_argument('--version', action='version', version='%s %s' % (__app_name__, __version__))
parser.add_argument('--help', action='help', help='show this help message and exit')
parser.add_argument('--debug', action='store_true', dest='debug', help='debugging mode')
parser.add_argument('--quiet', action='store_true', dest='quiet', help='no console output')
args = parser.parse_args()

log = get_logger(name=__name__, debug=args.debug, quiet=args.quiet)


def main():
    log.debug(args)

    var = None

    try:
        config = Config(config_file=__app_name__)
        var = config.get('var')
    except (IOError, NameError) as e:
        log.critical(e)
        exit(1)

    log.info(var)
