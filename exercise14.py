# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def remove_duplicates(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)
    return new_list


def remove_duplicates1(l):
    return list(set(l))


print(remove_duplicates(a))
print(remove_duplicates1(a))