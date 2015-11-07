#!/usr/bin/python
# Copyright (c) 2013 Free Inc.  ALL RIGHTS RESERVED.
# Author: yweiyun@gmail.com (Young Ray)
# Create  2013-11-17

import gflags
import sys
gflags.DEFINE_string('name', 'Mr. President', 'your name')
def main(argv):
  """docstring for main"""
  try:
    argv = gflags.FLAGS(argv) 
  except gflags.FlagsError, e:
    print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS)
    sys.exit(1)
  print gflags.FLAGS.name;
  pass
if __name__ == '__main__':
  main(sys.argv)
