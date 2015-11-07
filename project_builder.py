#!/usr/bin/python
# Copyright (c) 2013 Free Inc.  ALL RIGHTS RESERVED.
# Author: yweiyun@gmail.com (Young Ray)
# Create  2013-11-17

import class_builder
import copyright
class ProjectBuilder(object):
  """docstring for ProjectBuilder"""
  def __init__(self):
    super(ProjectBuilder, self).__init__()
  def gen_header_filename(self, class_name):
    return "%s.h"%class_name
  def gen_cpp_filename(self, class_name):
    """docstring for gen_cpp_filename"""
    cpp_file_style = "%s.cpp"
    return cpp_file_style%(class_name)
  def build_internal(self, space_name, class_name, copyright_str, common_header_part,
                     header_content_style, cpp_coding_style):
    header_file = self.gen_header_filename(class_name)
    class_file = self.gen_cpp_filename(class_name)
    cb = class_builder.ClassBuilder(class_name, space_name, copyright_str)
    self.dump_file(header_file, cb.get_header_file_str(common_header_part, header_content_style))
    self.dump_file(class_file, cb.get_cpp_file_str(cpp_coding_style, header_file))
    pass
  def sogou_build(self, space_name, class_name):
    common_header_part="#include \"gsl/NonCopyable.h\""
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
    copyright_str = copyright.CopyRight("// ").get_copy_right_str()
    return self.build_internal(space_name, class_name, copyright_str, common_header_part,
                               header_content_style, cpp_coding_style)
  def google_build(self, space, class_name):
    common_header_part="#include \"base/basictypes.h\""
    cpp_coding_style = "%s\n#include \"%s\"\n"\
                       "namespace %s{\n"\
                       "%s\n"\
                       "} // namespace %s\n"
    header_content_style = "namespace %s {\n"\
                           "class %s {\n"\
                           " public:\n"\
                           "  %s();\n"\
                           "  ~%s();\n"\
                           " private:\n"\
                           "   DISALLOW_COPY_AND_ASSIGN(%s);\n};\n"\
                           "} // namespace %s\n"
    copyright_str = copyright.CopyRight("// ").get_copy_right_str()
    return self.build_internal(space_name, class_name, copyright_str, common_header_part,
                               header_content_style, cpp_coding_style)
  @staticmethod
  def dump_file(full_file_name, content):
     """docstring for dump_file"""
     fp = open(full_file_name, "w")
     fp.write(content)
     fp.close()
if __name__ == '__main__':
  pb = ProjectBuilder()
  pb.sogou_build("crawl", "TestCast")
