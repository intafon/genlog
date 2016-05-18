#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from time import time

class Genlog(object):

  def __init__(
    self,
  ):

    from fn import Fn

    self.cwd = self.__get_cwd()

    self.fn = Fn()

  def __enter__(self):
    return self

  def __exit__(self ,type, value, traceback):
    return False

  def log(self, d):
    if not d:
      d = '.'
    recent = self.fn.recent(d)
    print(recent)
    print(d)

  def __get_cwd(self):

    from os import getcwd
    return getcwd()

