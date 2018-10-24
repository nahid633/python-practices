# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]


def first_and_last(array):
    new_list = [array[0], array[-1]]
    return new_list


print(first_and_last(a))
