#!/usr/bin/python

# Features (in order of importance)
# 1. Transpose lines of tab delimited text (DONE)
# 2. Space out the header and the lines nicely (DONE)
# 3. Handle quoted tabs properly (DONE - csvwriter handles this)
# 4. accept arbitrary delimiters (DONE)
# 5. limit output lines to -n lines (DONE)
# 6. Skip the first N lines (DONE)

import sys
import csv
import argparse

# infile - the original filehandle
# pinfile - the parsed filehandle

def main():
    parser = create_parser()
    args = parser.parse_args()
    infile = csv.reader(args.infile, delimiter=args.delim)
    header, format_string = prep_output(infile)
    infile = skip_lines(args.start, infile)
    line_num = args.start + 1
    for i in range(args.numlines):
        print_line(args, infile, format_string, header, line_num)
        line_num += 1       

def print_line(args, infile, format_string, header, line_num):
    line_header = "Line Number (" + str(line_num) + ")"
    print format_string % line_header,  "######################"
    conditional_print(args.verbose, infile, format_string, header)
    print format_string % "",  "######################"


def prep_output(infile):
    header = infile.next()
    header = ["%-8s" % str(header.index(i) + 1) + i for i in header]
    linebuffer = max([len(i) for i in header])
    format_string = '%-' + str(linebuffer) + 's'
    return header, format_string

def skip_lines(start, infile):
    for i in range(start):
        infile.next()
    return infile

def create_parser():
    parser = argparse.ArgumentParser(description='tcat a delimited file')
    parser.add_argument('infile', metavar='FILE', type=file,
                        help='the delimited file to read (default stdin)', 
                        default=sys.stdin)
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="Don't Supress empty fields", dest='verbose')
    parser.add_argument('-d', '--delimiter', action='store', dest='delim',
                        type=str, help='field delimiter', default='\t')
    parser.add_argument('-n', '--numlines', action='store', dest='numlines',
                        type=int, help='number of lines to parse', default='1')
    parser.add_argument('-s', '--start', action='store', dest='start',
                        type=int, help='skip the first N lines', default='0')
    return parser

def conditional_print(verbose, infile, format_string, header):
    nextline = zip(header, infile.next())
    for i in nextline:
        if not verbose:
            if i[1]:
                print format_string % i[0], i[1]
        else:
            print format_string % i[0], i[1]





if __name__=="__main__":
    main()
