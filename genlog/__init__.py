#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""genlog

Usage:
  genlog [<dir>] [-m <message>]
  genlog -h

Examples:

  genlog        Store most recent image in current directory.
  genlog dir    Store most recent image in directory 'dir'.
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
      # print(args)
      genlog.log(d=args['<dir>'], m=args['<message>'])

  except Exception as e:
    print(e, file=stderr)
    exit(1)


if __name__ == '__main__':
  run()

