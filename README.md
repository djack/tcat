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

    $ tcat test_file.tsv -d "\t" -s 4 -n 3
      
    Line Number (4)              ######################
    0       Packet               1
    1       Time                 2013-02-12 13:22:05
    2       Event                577
    3       Field                3810
    4       Red                  0
    5       Blue                 0
    6       Field_ID             1
    7       Field_Type           X
    81      Field_Code           XD
    100     Field_RD             0
    101     Field_Time           13:22:05
    102     Field_Field          0
                                 ######################
    Line Number (5)              ######################
    0       Packet               2
    1       Time                 2013-02-12 13:22:08
    2       Event                577
    3       Field                0
    4       Red                  0
    5       Blue                 0
                                 ######################
    Line Number (6)              ######################
    0       Packet               3
    1       Time                 2013-02-12 13:22:11
    2       Event                577
    3       Field                3810
    4       Red                  1880
    5       Blue                 1850
                                 ######################

