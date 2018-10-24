# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#
#   My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.

sentence  = str(input("enter a sentence "))


def backward_order(sent):
    result = sent.split()
    return " ".join(result[::-1])


print(backward_order(sentence))


#
# # method 3
# def reverse_v3(x):
#   y = x.split()
#   return " ".join(reversed(y))
#
# # method 4
# def reverse_v4(x):
#   y = x.split()
#   y.reverse()
#   return " ".join(y)