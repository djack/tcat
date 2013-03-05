tcat
====

Transpose delimited lines of text to readable, labeled, aligned rows at the CLI.

usage: 
----

    tcat.py [-h] [-i FILE] [-v] [-d DELIM] [-n NUMLINES] [-s START]

    tcat a delimited file

    positional arguments:
        FILE                   the delimited file to read (default stdin)

    optional arguments:

        -h, --help             show this help message and exit
        -v, --verbose          don't supress empty fields
        -d, --delimiter DELIM, field delimiter
        -n, --numlines N,      parse exact N lines
        -s, --start N,         skip the first N lines
                        
Output
----      
      
    Line Number (1)              ######################
    0       Packet               1
    1       Time                 2013-02-12 13:22:05
    2       Event                577
    3       Field                3810
    4       Red                  0
    5       Blue                 0
    6       Field_ID             1
    7       Field_Type           X
    8       Field_Code           XD
    10      Field_RD             0
    11      Field_Time           0
    12      Field_Fighter        0
                                 ######################
    Line Number (2)              ######################
    0       Packet               2
    1       Time                 2013-02-12 13:22:08
    2       Event                577
    3       Field                0
    4       Red                  0
    5       Blue                 0
                                 ######################
    Line Number (3)              ######################
    0       Packet               3
    1       Time                 2013-02-12 13:22:11
    2       Event                577
    3       Field                3810
    4       Red                  1880
    5       Blue                 1850
                                 ######################

