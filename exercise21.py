# Take the code from the How To Decode A Website exercise
# (if you didn’t do it or just want to play with some different code, use the code from the solution),
# and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.
#
# Extras:
#
# Ask the user to specify the name of the output file that will be saved.

name_of_file = str(input("enter the name of file "))
data = str(input("now enter some data to file please "))
with open(name_of_file, 'w') as file_to_write:
    file_to_write.write(data)
