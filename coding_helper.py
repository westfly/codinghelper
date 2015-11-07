#!/usr/bin/python
# Copyright (c) 2013 Sogou Inc.  ALL RIGHTS RESERVED.
# Author: liyangrui@sogou-inc.com (Young Ray)
# Create  2013-11-17

import project_builder
import gflags
import sys
FLAGS=gflags.FLAGS
gflags.DEFINE_string('class_name', "","the define class");
gflags.DEFINE_string('space_name', "crawl","the defined namespace");
if __name__ == '__main__':
  try:
      argv = gflags.FLAGS(sys.argv)
  except gflags.FlagsError, e:
      print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], gflags.FLAGS)
      sys.exit(1)
  pb = project_builder.ProjectBuilder()
  if len(FLAGS.class_name) <= 0:
      print "class_name is unvalid"
      sys.exit(-1)
  print "clas_name:%s\tspace_name %s"%(FLAGS.class_name, FLAGS.space_name)
  pb.sogou_build(FLAGS.space_name, FLAGS.class_name)
