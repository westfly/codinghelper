#!/usr/bin/python
# Copyright (c) 2013 Free Inc.  ALL RIGHTS RESERVED.
# Author: yweiyun@gmail.com (Young Ray)
# Create  2013-11-17

import copyright
class ClassBuilder(object):
  def __init__(self, class_name, ns_name, copyright_str):
    """docstring for __init__"""
    super(ClassBuilder, self).__init__()
    self.class_name = class_name
    self.ns_name = ns_name
    self.copyright_str = copyright_str
  def get_cpp_file_str(self, cpp_coding_style, header_file_name):
    content_str = self.get_content_str();
    return cpp_coding_style % (self.copyright_str,
           header_file_name, self.ns_name,
           content_str, self.ns_name)
  def get_content_str(self):
    """docstring for get_content_str"""
    coding_style = "%s::%s() {}\n"\
                   "%s::~%s() {}\n\n"
    return coding_style % (self.class_name, self.class_name,
                           self.class_name, self.class_name)

  def get_header_content(self, header_content_style):
    #print header_content_style
    return header_content_style % (self.ns_name, self.class_name,
                                   self.class_name, self.class_name,
                                   self.class_name, self.ns_name)

  def get_header_file_str(self, common_header_part, header_content_style):
    """docstring for get_header_str"""
    header_coding_style = "%s\n#ifndef %s\n"\
                "#define %s\n%s\n%s\n#endif // %s\n\n"
    header_guard = self.get_header_guard()
    #print header_guard
    header_content = self.get_header_content(header_content_style)
    return header_coding_style % (self.copyright_str, header_guard, header_guard,
                                  common_header_part, header_content, header_guard)


  def get_header_guard(self):
    """docstring for get_header_guard"""
    guard_style = "%s_%s_H"
    return guard_style % (self.ns_name.upper(), self.class_name.upper())
if __name__ == '__main__':
  copyright="get busy living"
  cpp_coding_style = "%s\n#include \"%s\"\n"\
                     "namespace %s\n{\n"\
                     "%s\n"\
                     "} // namespace %s\n"
  header_content_style = "namespace %s \n{\n"\
                         "class %s \n{\n"\
                         " public:\n"\
                         "  %s();\n"\
                         "  ~%s();\n"\
                         " private:\n"\
                         "   DISALLOW_COPY_AND_ASSIGN(%s);\n};\n"\
                         "} // namespace %s\n"
  cb = ClassBuilder("Free", "free", copyright)
  print "%s\n%s\n"%(cb.get_header_file_str("#include <stdio.h>", header_content_style),
                    cb.get_cpp_file_str(cpp_coding_style, "man.h"))
