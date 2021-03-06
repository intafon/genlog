#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Genlog(object):

  def __init__(
    self,
  ):
    from fn import Fn
    from os import sep

    self.fn = Fn()
    self.repo = self.fn.repo
    self._store = self.fn.top_level + sep + '.genlog'
    self.__ensure_store()

    self.size = 1024

  def __enter__(self):
    return self

  def __exit__(self ,type, value, traceback):
    return False

  def __ensure_store(self):
    from os import stat
    from os import mkdir

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

  def __thumbnail(self, recent):
    try:
      from PIL import Image
    except Exception:
      import Image

    thumb = self.__copy_file(recent)
    if thumb:
      n = self.size
      img = Image.open(thumb)
      img.thumbnail((n, n))
      img.save(thumb)

    return thumb

  def __get_author(self):
    from os import getenv
    email = getenv('GENLOG_USER_EMAIL', '')
    if len(email)>0:
      return email
    return None

  def __commit_all(self, thumb, m):
    from os import sep
    from git import Actor

    info_file = thumb.split(sep)[-1]
    self.repo.git.add('-A')
    self.repo.git.add(thumb, '-f')

    email = self.__get_author()
    a = None
    if email:
      a = Actor('genlog', email)

    if m:
      s = m
    else:
      s = ':genlog:'

    s += '\n\n:thumb:{:s}'.format(info_file)
    self.repo.index.commit(s, committer=a, author=a)

  def log(self, d, m):

    if not d:
      d = '.'
    recent = self.fn.recent(d)
    if not recent:
      return None

    thumb = self.__thumbnail(recent)
    self.__commit_all(thumb, m)

