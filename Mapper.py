#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <tv_show, channel> or <tv_show, viewers_count> input file, and move channel/viewers into
#  the value field for output
#
#  Note: Input, it is assumed to be correct, meaning no extra spaces, missing inputs/counts,etc.
# --------------------------------------------------------------------------

for line in sys.stdin:
    key_value = [item.strip() for item in line.split(",")] #split line, into key and value, returns a list
    if not key_value[1].isdigit() and not key_value[1] == "ABC":
        continue
    else:
        key_in = key_value[0] #key is first item in list
        value_in = key_value[1] #value is 2nd item
        print('%s\t%s' % (key_in, value_in)) #print a string tab and string

#Hadoop expects a tab to separate key value, program assumes the input file has a ',' separating key value