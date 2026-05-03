#!/usr/bin/env python3
# Sample script that writes to a file
# By Yaya
#Script 1 - Collect info and save to hackme.txt
'''
Write a script that saves user input into a file, that gathers data about the user
'''

#These variables are questions that need to be answered
name = input("what is your name? ")
color = input("what is your favorite color? ")
pet = input ("what is first pets name? ")
maiden = input("what is your mother maiden name? ")
school = input(" what elementary school did you intend? ")

with open("hackme.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Favorite Color: {color}\n")
    file.write(f"First Pet: {pet}\n")
    file.write(f"Mothers Maiden Name: {maiden}\n")
    file.write(f"Elementary School: {school}\n")

    print("Save to hackme.txt Great work!")