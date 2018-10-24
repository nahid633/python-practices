# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


num = int(input("enter a number(not negative numbers) "))



def fibonacci(num):
    a, b = 0, 1
    array = []
    for i in range(num+1):
        a, b = b, a+b
        array.append(a)
    return array


print(1 if num-1 <= 0 else num-1,"'s length is",num , fibonacci(num -1))