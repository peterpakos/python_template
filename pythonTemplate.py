#!/usr/bin/python
#
# Python template
#
# Author: Peter Pakos
# Copyright (C) 2015

# Import modules
try:
    import sys
    import getopt
    import os
except ImportError as err:
    print "Import Error: %s" % err
    sys.exit(3)


# Global config class (uninstantiated)
class config:
    app_version = "1.0"
    app_name = os.path.basename(sys.argv[0])


# Main class
class Main(object):

    # Constructor method
    def __init__(self):
        self.test = self.parse_options()

    # Parse arguments
    def parse_options(self):
        try:
            options, args = getopt.getopt(sys.argv[1:], "hV", [
                'help',
                'version'
            ])
        except getopt.GetoptError:
            self.usage()
            self.die(1)

        for opt, arg in options:
            if opt in ('-h', '--help'):
                self.usage()
                self.die(0)
            if opt in ('-V', '--version'):
                self.version()
                self.die(0)

    # Display version
    def version(self):
        print "%s version %s" % (config.app_name, config.app_version)

    # Display help page
    def usage(self):
        self.version()
        print "Usage: %s [OPTIONS]" % config.app_name
        print "AVAILABLE OPTIONS:"
        print "-h\t\tPrint this help summary page"
        print "-V\t\tPrint version number"

    # App code to be run
    def run(self):
        self.die

    # Exit app with code and optional message
    def die(self, code=0, message=None):
        if message is not None:
            print message
        sys.exit(code)

# Instantiate main class and run it
if __name__ == '__main__':
    app = Main()
    app.run()
