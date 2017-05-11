#!/usr/bin/env python

import re, sys, optparse, read_files
from ebcdic2ascii_encoder import *

# takes in a file list and parameters for unicode encoding and skipping print strings
# intended for use by other python programs, not for scripts for commandline
def open_files(file_list, unicode_encode=False, skip_print_strings=False, include_paths=[], include_paths_names=[]):

   # error-check: need exactly two file paths in file_list
   if len(file_list) != 2:
      print("ERROR: Source and target file path required.")
      return 1

   convert_to_ascii(file_list, unicode_encode, skip_print_strings, include_paths, include_paths_names)

   # resets the global blacklist contained in read_files.py for header files
   read_files.reset_blacklist()
   return 0

def make_delimiters(tokens_of_interest, skip_print_strings):
   delimiters = []
   delete = False
   open_paren = 0
   start_index = 0
   stop_index  = 0

   for index in range(len(tokens_of_interest)):
      token = tokens_of_interest[index]
      if USTR_MACRO_RE.match(token):
         start_index = index
         delete = True
      if skip_print_strings and PRINT_FUNCTIONS_RE.match(token):
         start_index = index
         delete = True
      if delete and OPEN_PAREN_RE.match(token):
         open_paren = open_paren + 1;
      if delete and (CLOSE_PAREN_RE.match(token) or NEWLINE_RE.match(token)):
         open_paren = open_paren - 1;
         if open_paren == 0:
            stop_index = index
            delimiters.append((start_index, stop_index))

   return delimiters

# main function to convert from ebcdic to ascii
def convert_to_ascii(filenames, unicode_encode, skip_print_strings, include_paths, include_paths_names):
   Source          = open(filenames[0], "rt")
   Target          = open(filenames[1], "at+")

   # flags to determine exactly what the line of code in the source contains
   ebcdic_encoding = False
   convert_start = False
   convert_end = False

   multiline_comment = False
   comment_start = False
   comment_end = False

   skip_line = False
   include_line = False

   # main loop which identifies and encodes literals with hex escape sequences
   for line in Source:

      # check if the line is a comment
      comment_start = MULTILINE_COMMENT_START.match(line)
      multiline_comment = (multiline_comment or comment_start)\
       and (not comment_end)

      # check if conversion is requested
      convert_start = EBCDIC_PRAGMA_START.match(line)
      ebcdic_encoding = (ebcdic_encoding or convert_start)\
       and (not convert_end)

      # check if the line should be ignored
      skip_line = IGNORE_RE.match(line)\
       or multiline_comment or ebcdic_encoding
      include_line = INCLUDE_RE.match(line)

      if not skip_line and not include_line:
         tokens_of_interest = re.split(SPLIT_RE, line)
         tokens_of_interest = filter(None, tokens_of_interest)

         # mark strings inside functions and between outstream_op which we do not want to be modified
         delimiters = make_delimiters(tokens_of_interest, skip_print_strings)

         index = 0;
         newline = ""
         delimiters.reverse()
         start_index = -1;
         stop_index  = -1;
         ostream_string = False

         while index < (len(tokens_of_interest)):
            token = tokens_of_interest[index];

            if USTR_MACRO_RE.match(token) or (skip_print_strings and PRINT_FUNCTIONS_RE.match(token)):
               if len(delimiters) > 0:
                  (start_index, stop_index) = delimiters.pop();
               token = token
               newline = newline + token
               index = index +1
               continue

            if index >= start_index and index <= stop_index:
               token = token
               newline = newline + token
               index = index + 1
               continue

            if skip_print_strings and OUTSTREAM_OP_RE.match(token):
               if not ostream_string:
                  ostream_string = True;
               else:
                  ostream_string = False;

            if NEWLINE_RE.match(token):
               if ostream_string:
                  ostream_string = False;

            if STRING_RE.match(token):
               if not ostream_string:
                  literal = token
                  if unicode_encode:
                     if not HEX_ENCODED_STRING_RE.match(literal):
                        unicode_literal = "u8" + literal
                        token = unicode_literal
                  else:
                     encoded_literal = literal[1:len(literal)-1]
                     encoded_literal = re.sub(ESCAPE_RE, EncodeEscapeSeq,encoded_literal)
                     encoded_literal = re.sub(PRINTF_RE, EncodePrintF, encoded_literal)
                     token_list = re.split(HEX_RE, encoded_literal)
                     encoded_literal = reduce(lambda x,y: x+y, map(ConvertTokens, token_list))
                     encoded_literal = "\"" + encoded_literal + "\""
                     token = encoded_literal
            if CHAR_RE.match(token):
               if not ostream_string:
                  char = token[1:len(token)-1]
                  encoded_char = ''
                  escape_seq = ESCAPE_RE.match(char)
                  if escape_seq:
                     encoded_char = EncodeEscapeSeq(escape_seq)
                  else:
                     encoded_char = ConvertTokens(char)
                  char = "'" + char + "'"
                  encoded_char = "'" + encoded_char + "'"
                  token =  encoded_char
            if STRINGIFY_RE.match(token):
               converted_token = ConvertMacroArgs(token)
               token = converted_token
            newline = newline + token
            index = index + 1;
         line = newline;

      # if the line is an #include statement
      if include_line:
         target_header = 0
         quotes = True

         # check if its an absolute path, as those take priority
         ABSOLUTE_RE = re.compile('#\s*include\s*"(/.*)"')
         a = ABSOLUTE_RE.search(line)
         if a is not None:
            absolute_path = a.group(1)
            target_header = read_files.main([absolute_path, '', include_paths, include_paths_names])
            Target.write('#include "' + target_header + '"\n')

         else:
            FILE_QUOTES_RE = re.compile('#\s*include\s*"(.*)"')
            FILE_BRACKETS_RE = re.compile('#\s*include\s*<(.*)>')

            include_file = FILE_QUOTES_RE.match(line)
            if include_file is None:
                quotes = False
                include_file = FILE_BRACKETS_RE.match(line).group(1)
            else:
                include_file = include_file.group(1)

            FILE_END_ONLY = re.compile('.*/(.*)')
            include_end = FILE_END_ONLY.search(include_file)
            if include_end is not None:
                include_end = include_end.group(1)
            else:
                include_end = include_file

            if include_end in include_paths_names:
                full_path = include_paths[include_paths_names.index(include_end)]
                target_header = read_files.main([full_path, include_file, include_paths, include_paths_names])
            else:
                target_header = include_file

            if quotes:
                Target.write('#include "' + target_header + '"\n')
            else:
                Target.write('#include <' + target_header + '>\n')

      else:
         comment_end = MULTILINE_COMMENT_END.match(line)
         convert_end = EBCDIC_PRAGMA_END.match(line)
         line = line
         Target.write(line)

   Source.close()
   Target.close()

# parses the arguments given from command line or os process in order to determine
# the filenames, unicode encoding, and skip print strings options
def parse_arguments():

   # parse the command line arguments, looking for potential flags -u and --skip_print
   # along with two file paths, input and output
   parser = optparse.OptionParser()
   parser.set_usage("""ebcdic2ascii.py [options] input.cc output.cc include_paths
   input.cc: File to be converted
   output.cc: Converted File.""")
   parser.add_option("-u", action="store_true", dest="unicode_support", default = False, help="convert strings using u8 prefix")
   parser.add_option("--skip_print", action="store_true", dest="skip_print_strings", default = False, help="skip strings going to snprtinf,printf,output stream")
   parser.add_option("-I", action="append", dest="include_paths", default=[], help="provide another root path to look at for #include statements")
   parser.add_option("-H", action="store", dest="headers", default=[], help="provide a file that contains all the dependencies")

   (options, args) = parser.parse_args()

   # error-check: two arguments from command-line expected
   if len(args) < 2:
      print("ERROR: Source and target file path required.")
      return 1

   unicode_encode             = options.unicode_support;
   skip_print_strings         = options.skip_print_strings;

   includes = []
   files = []
   header_file = open(options.headers, 'rt')
   for line in header_file:
       ABSOLUTE_RE = re.compile('/.*')
       absolute_match = ABSOLUTE_RE.match(line)
       if absolute_match is None:
           includes.append(line.rstrip())
           FILE_RE = re.compile('.*/(.*)')
           files.append(FILE_RE.search(line).group(1))

   if options.include_paths != []:
       includes = includes + options.include_paths
   convert_to_ascii(args, unicode_encode, skip_print_strings, includes, files)

   # resets the global blacklist contained in read_files.py for header files
   read_files.reset_blacklist()
   return 0

if __name__ == "__main__":
   sys.exit(parse_arguments())
