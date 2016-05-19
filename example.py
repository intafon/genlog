#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def copy_file(ffrom, to):
  from shutil import copyfile
  copyfile(ffrom, to)

def main():
  from fn import Fn
  fn = Fn(prefix='./res/').name() + '.png'
  copy_file('./res/sample.png', fn)



if __name__ == '__main__':
  main()

