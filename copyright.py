#!/usr/bin/python
# Copyright (c) 2013 Free Inc.  ALL RIGHTS RESERVED.
# Author: yweiyun@gmail.com (Young Ray)
# Create  2013-11-17

import gflags
import sys
import time
FLAGS=gflags.FLAGS
gflags.DEFINE_string('company', 'Free', 'the author company')
gflags.DEFINE_string('author_nickname', 'Young Ray', 'nick name')
gflags.DEFINE_string('author_email', 'yweiyun@gmail.com', 'email address')

class CopyRight:
  """docstring for CopyRight"""
  copy_right_style = "%s Copyright (c) %d\t%s Inc.  ALL RIGHTS RESERVED.\n"
  author_name_style = "%s Author: %s (%s)\n"
  create_day_style = "%s Create  %s\n"
  def __init__(self, seperator):
    self.copyright_str = self.join_copyright(seperator)

  def join_copyright(self, seperator):
   """docstring for fname"""
   current_time = time.localtime(time.time())
   copyright_lines = []
   copyright_lines.append(self.copy_right_style%(seperator,
     current_time.tm_year, FLAGS.company))
   copyright_lines.append(self.author_name_style%(seperator, FLAGS.author_email,
     FLAGS.author_nickname))
   create_day = time.strftime('%Y-%m-%d', current_time)
   copyright_lines.append(self.create_day_style%(seperator, create_day))
   return "".join(copyright_lines)

  def get_copy_right_str(self):
    """docstring for get_copy_right_str"""
    return self.copyright_str;
    pass
def main(argv):
  """docstring for ma"""
  try:
    argv = gflags.FLAGS(argv) 
  except gflags.FlagsError, e:
    print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS)
    sys.exit(1)
  coding_copyright = CopyRight('//')
  print (coding_copyright.get_copy_right_str())
  pass
if __name__ == '__main__':
  main(sys.argv)
