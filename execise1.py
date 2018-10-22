# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name ")
age = int(input("now age please "))
print("{},You will reach to 100 in {},maybe till that time you will die".format(name,(2018 - age) + 100));