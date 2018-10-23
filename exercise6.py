# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

example  = input("enter a string ")
rvs = example[::-1]
if example == rvs:
    print("{} is palindrome".format(example))
else:
    print("{} is not palindrome".format(example))
