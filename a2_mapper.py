#!/usr/bin/env python
import sys
def mapper():
    for line in sys.stdin:
        line =line.strip()
        line = line.split(",")

        if len(line) >= 2:
            first_column='lines'
            data=line[0]
            print("%s\t%s" % (data,first_column))

mapper()
