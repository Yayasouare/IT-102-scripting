#!/usr/bin/env python3
# Sample script that reads from a file
# By Yaya
'''
This is to read the file i created from the script writefile.py
'''


#Create a loop to open file and read its contents
with open("hackme.txt", "r") as file:
    contents = file.read()
print("here is someone to hack - info dumb")
print(contents)    