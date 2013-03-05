tcat
====

Transpose delimited lines of text to nicely readable labeled and aligned rows at the CLI.

usage: 
----

tcat.py [-h] [-i FILE] [-v] [-d DELIM] [-n NUMLINES] [-s START]

tcat a delimited file

optional arguments:

  -h, --help            show this help message and exit

  -i, --infile FILE, 
                        the delimited file to read (default stdin)

  -v, --verbose         don't supress empty fields

  -d, --delimiter DELIM, 
                        field delimiter

  -n, --numlines N,
                        parse exact N lines

  -s, --start N,
                        skip the first N lines
