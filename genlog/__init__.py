#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""genlog

Usage:
  genlog [<dir>]
  genlog -h

Examples:

  -h            Show this screen.
  --version     Show version.
"""

__ALL__ = ['Genlog']

from genlog.genlog import Genlog


def run():

  from docopt import docopt
  args = docopt(__doc__, version='genlog 0.0.1')
  main(args)

def main(args):

  from sys import stderr
  from sys import exit

  # print(args)
  try:
    with Genlog() as genlog:
      genlog.log(d=args['<dir>'])

  except Exception as e:
    print(e, file=stderr)
    exit(1)


if __name__ == '__main__':
  run()

