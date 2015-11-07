#!/usr/bin/env python
# -*- coding: utf-8 -*-
class BuilderWrapper(object):
  @staticmethod
  def dump_file(full_file_name, content):
     """docstring for dump_file"""
     # overwrite method
     fp = open(full_file_name, "w")
     fp.write(content)
     fp.close()
