#!/usr/bin/env python
#
# Script description.
#
# Author: First Last <first.last@wandisco.com>

try:
    import sys
    import os
    import getopt
except ImportError as err:
    print >> sys.stderr, "Import Error: %s" % err
    sys.exit(1)


class Main(object):
    app_version = "1.0"
    app_name = os.path.basename(sys.argv[0])

    def __init__(self):
        self.parse_options()

    def parse_options(self):
        try:
            options, args = getopt.getopt(sys.argv[1:], "hv", [
                "help",
                "version"
            ])
        except getopt.GetoptError as err:
            self.die(err)

        for opt, arg in options:
            if opt in ("-h", "--help"):
                self.usage()
                sys.exit()
            if opt in ("-v", "--version"):
                self.version()
                sys.exit()

    def version(self):
        print "%s version %s" % (self.app_name, self.app_version)

    def usage(self):
        self.version()
        print """Usage: %s [OPTIONS]
AVAILABLE OPTIONS:
-h, --help      Print this help summary page
-v, --version   Print version number""" % self.app_name

    def die(self, message=None, code=1):
        if message is not None:
            print >> sys.stderr, message
        sys.exit(code)

    def run(self):
        print "Hello World!"

if __name__ == '__main__':
    app = Main()
    app.run()
