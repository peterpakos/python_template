# python_template
Python project template

PyPI package: [python_template](https://pypi.python.org/pypi/python_template)

If you spot any problems or have any improvement ideas then feel free to open
an issue and I will be glad to look into it for you.

## Installation
A recommended way of installing the tool is pip install.

Once installed, a command line tool `python_template` should be available in your
system's PATH.

### pip install
The tool is available in PyPI and can be installed using pip:
```
$ pip install --user python_template
$ python_template
```

## Configuration
By default, the tool reads its configuration from `~/.config/python_template` file (the
location can be overridden by setting environment variable `XDG_CONFIG_HOME`).
If the config file (or directory) does not exist then it will be automatically
created and populated with sample config upon the next run.

## Usage - Help
```
$ python_template --help
usage: python_template [--version] [--help] [--debug] [--verbose] [--quiet]

Python Template

optional arguments:
  --version  show program's version number and exit
  --help     show this help message and exit
  --debug    debugging mode
  --verbose  verbose logging mode
  --quiet    no console output
```