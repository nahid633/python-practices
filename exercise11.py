# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.
number = int(input("enter a number "))


def divisors(num):
    divs = []
    list_range = list(range(1, num + 1))
    for l in list_range:
        if num % l == 0 and l != 1 and l != num:
            divs.append(l)
    return divs


if len(divisors(number)) == 0:
    print(number, " is prime number")
else:
    print(number, " is not prime number")
