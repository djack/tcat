tcat
====

Transpose delimited lines of text to nicely readable labeled and aligned rows at the CLI.

usage: tcat.py [-h] [-i FILE] [-v] [-d DELIM] [-n NUMLINES] [-s START]

tcat a delimited file

optional arguments:
  -h, --help            show this help message and exit
  -i FILE, --infile FILE
                        the delimited file to read (default stdin)
  -v, --verbose         Don't Supress empty fields
  -d DELIM, --delimiter DELIM
                        field delimiter
  -n NUMLINES, --numlines NUMLINES
                        number of lines to parse
  -s START, --start START
                        skip the first N lines
