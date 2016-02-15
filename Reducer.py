#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input, at the end it will perform the last join
#
#
#  Note: Input, it is assumed to be correct, meaning no extra spaces, missing inputs/counts,etc.
# --------------------------------------------------------------------------

prnt = 0 # Variable for print set at 0 (variable = 0)
running_count = 0 # Variable for running total set at 0 (variable = 0)
prev_word = None             #initialize these variables

for line in sys.stdin:
    line = line.strip()       #strip out carriage return
    key_value = line.split('\t')   #split line, into key and value, returns a list

    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    if prev_word != curr_word:
        if prnt == 1:
            print('%s\t%s' % (prev_word, running_count)) #Prints out key,value pair
            prnt = 0 #Set print variable to 0
            running_count = 0 #Set running total to 0
        if value_in != "ABC":
            value_in = int(value_in) #Converts variable into integer
            running_count = value_in #Setting running total to value
    else:
        if value_in != "ABC":
            value_in = int(value_in) #Converts variable into integer
            running_count += value_in #Adds view onto running total
    if value_in == "ABC":
        prnt = 1 #Set print variable to 1
    prev_word = curr_word #Change prev_word to curr_word

"""
running_count = 0 #initialize previous word  to blank string

for line in sys.stdin:
    line = line.strip()       #strip out carriage return
    key, value = line.split('\t')   #split line, into key and value, returns a list

    if value == "ABC" and running_count == 0:
        continue

    elif value == "ABC" and running_count >= 1:
        print('%s\t%s' % (key, running_count))
        running_count = 0

    else:
        value = int(value)
        running_count += value
"""
