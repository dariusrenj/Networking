#!/usr/bin/env python

import os, glob, subprocess

"""
# Given a list of strings (['string1', 'string2', 'string3']), reverse all of the characters, and
# join them all together into a single string, with each previous word separated by spaces
# (the above example becomes '1gnirts 2gnirts 3gnirts')
"""
def first_test(string_list):
    #loop through and reverse the strings
    for i in range(len(string_list)):
        string_list[i] = string_list[i][::-1]
    #create a return string variable
    return_string = ""
    #loop through and append each string to return string
    for i in range(len(string_list)):
        if (i == 0):
            return_string = string_list[i]
        else:
            return_string = return_string + " " + string_list[i]
    #return the return string
    return return_string

"""
# Given a directory path, find each file that ends with '.txt', and create a dictionary,
# where each element consists of the filename, and its contents (e.g., if we had a file called
# "foo.txt" that contained "AAAA", our dictionary would look like: 
# { "evalFolder\\foo.txt" : "AAAA" }). This dictionary will be our return item.
"""
def third_test(fname):
    #create a list of files from the provided directory
    file_list = glob.glob((fname+'/*.txt'))
    #create a dictionary variable
    file_dictionary = {}
    #loop through and add key:value pairs to dictionary
    #open and close file are in loop since dictionary value is specific to file
    for i in range(len(file_list)):
        #open file
        input_file = open(file_list[i])
        file_dictionary[file_list[i]] = input_file.read()
        #close file
        input_file.close()
    #return dictionary
    return file_dictionary