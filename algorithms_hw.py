# # Number 1.
# # Compute the sum of digits in all numbers from 1 to n.
# # When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# # Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
#
# n = 5
# list_n = [x for x in range(n+1) if 0<x<=n]
# print(sum(list_n))
#
# # Number 2.
# # Find the max number from 3 values.
# # Example: 124, 21, 32. Result = 124.
#
# a = 124
# b = 21
# c = 32
#
# if a > b:
#     if a > c:
#         print(f" a = {a} is the highest")
#     else:
#         print(f"c = {c} is the highest")
# else:
#     if b < c:
#         print(f"c = {c} is the highest")
#     else:
#         print(f"b = {b} is the highest")
#
#
# # Number 3.
# # Count odd and even numbers. Count odd and even digits of the whole number.
# # Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
#
# number = 34560
#
# num_list = [int(x) for x in str(number)]
# print(num_list)
#
# odd = []
# even = []
#
# for i in num_list:
#     if i%2 == 0:
#         even.append(i);
#     else:
#         odd.append(i)
#
# print(f"Even: {even}, Odd: {odd}")

# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


def split_string_to_equal_parts(a):
    b = len(a)//2
    print(b)
    new = (a[b+1:] + a[:b+1])
    print(new)

split_string_to_equal_parts("bbbbbcaaaaa")


# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unique_char_string(string):
    if len(set(string)) == len(string):
        print(f'{string} contains unique characters')
    else:
        print (f'{string} contains duplicate characters')


unique_char_string('aabcde')
unique_char_string('abcde')