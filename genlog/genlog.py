#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from git.repo import Repo

class Genlog(object):

  def __init__(
    self,
  ):

    from fn import Fn

    self.cwd = self.__get_cwd()
    self._store = self.cwd + '/.genlog'
    self.__ensure_dir()

    self.fn = Fn()
    self.repo = self.fn.repo
    self.size = 800

  def __enter__(self):
    return self

  def __exit__(self ,type, value, traceback):
    return False

  def __ensure_dir(self):
    from os import stat, mkdir

    try:
        stat(self._store)
    except Exception:
      mkdir(self._store)

  def __copy_file(self, recent):
    from shutil import copyfile
    from os import sep
    for t in recent:
      if t.endswith('.png'):
        target = t.split(sep)[-1]
        full_target = self._store+sep+target
        copyfile(t, full_target)
        return full_target
    return False

  def __resize_png(self, fn):

    try:
      from PIL import Image
    except Exception:
      import Image

    n = self.size
    img = Image.open(fn)
    img.thumbnail((n, n))
    img.save(fn)

  def log(self, d):

    if not d:
      d = '.'
    recent = self.fn.recent(d)
    if not recent:
      return None

    new_file = self.__copy_file(recent)
    if new_file:
      self.__resize_png(new_file)
      return True

    return None

  def __get_cwd(self):

    from os import getcwd
    return getcwd()

