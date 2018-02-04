#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python Template

Author: Peter Pakos <peter.pakos@wandisco.com>

Copyright (C) 2017 WANdisco

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
import os
import argparse
from pplogger import get_logger
from . import VERSION

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


class Main(object):
    def __init__(self):
        self._app_name = os.path.splitext(__name__)[0].lower()
        self._args = self._parse_args()
        self._log = get_logger(debug=self._args.debug, quiet=self._args.quiet, verbose=self._args.verbose)
        self._log.debug(self._args)
        self._log.debug('Initialising...')
        self._config_dir = os.path.expanduser(os.environ.get('XDG_CONFIG_HOME', '~/.config'))
        self._config_path = os.path.join(
            self._config_dir,
            self._app_name
        )
        self._load_config()

    def _parse_args(self):
        parser = argparse.ArgumentParser(description='Python Template', add_help=False)
        parser.add_argument('--version', action='version',
                            version='%s %s' % (self._app_name, VERSION))
        parser.add_argument('--help', action='help', help='show this help message and exit')
        parser.add_argument('--debug', action='store_true', dest='debug', help='debugging mode')
        parser.add_argument('--verbose', action='store_true', dest='verbose', help='verbose logging mode')
        parser.add_argument('--quiet', action='store_true', dest='quiet', help="don't log to console")

        return parser.parse_args()

    def _load_config(self):
        config = configparser.ConfigParser()

        if not os.path.exists(self._config_dir):
            self._log.debug('Config directory %s does not exist, creating' % self._config_dir)
            os.makedirs(self._config_dir)

        if not os.path.isfile(self._config_path):
            self._log.debug('Config file not found at %s' % self._config_path)
            config.add_section('SECTION')
            config.set('SECTION', 'SOME_VAR', 'changeme')

            with open(self._config_path, 'w') as cfgfile:
                config.write(cfgfile)
            self._log.info('Initial config saved to %s - PLEASE EDIT IT!' % self._config_path)
            return

        self._log.debug('Loading configuration file %s' % self._config_path)

        if 'changeme' in open(self._config_path).read():
            self._log.debug('Initial config found in %s - PLEASE EDIT IT!' % self._config_path)
            return

        config.read(self._config_path)

        if not config.has_section('SECTION'):
            self._log.debug('Config file has no SECTION section')
            return

        if config.has_option('SECTION', 'SOME_VAR'):
            self._some_var = config.get('SECTION', 'SOME_VAR')
            self._log.debug('SOME_VAR = %s' % self._some_var)
        else:
            self._log.debug('SECTION.SOME_VAR not set')

    def run(self):
        self._log.debug('Starting...')
        self._log.info('I am just a template, edit me!')
        self._log.debug('Finishing...')


def main():
    try:
        Main().run()
    except KeyboardInterrupt:
        print('\nTerminating...')
        exit(130)
