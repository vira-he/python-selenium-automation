# # # Number 1.
# # # Compute the sum of digits in all numbers from 1 to n.
# # # When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# # # Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
# #
# # n = 5
# # list_n = [x for x in range(n+1) if 0<x<=n]
# # print(sum(list_n))
# #
# # # Number 2.
# # # Find the max number from 3 values.
# # # Example: 124, 21, 32. Result = 124.
# #
# # a = 124
# # b = 21
# # c = 32
# #
# # if a > b:
# #     if a > c:
# #         print(f" a = {a} is the highest")
# #     else:
# #         print(f"c = {c} is the highest")
# # else:
# #     if b < c:
# #         print(f"c = {c} is the highest")
# #     else:
# #         print(f"b = {b} is the highest")
# #
# #
# # # Number 3.
# # # Count odd and even numbers. Count odd and even digits of the whole number.
# # # Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
# #
# # number = 34560
# #
# # num_list = [int(x) for x in str(number)]
# # print(num_list)
# #
# # odd = []
# # even = []
# #
# # for i in num_list:
# #     if i%2 == 0:
# #         even.append(i);
# #     else:
# #         odd.append(i)
# #
# # print(f"Even: {even}, Odd: {odd}")
#
# # Given a string. Split it into two equal parts. Swap these parts and return the result.
# # If the string has odd characters, the first part should be one character greater than the second part.
# # Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
#
#
# def split_string_to_equal_parts(a):
#     b = len(a)//2
#     print(b)
#     new = (a[b+1:] + a[:b+1])
#     print(new)
#
# split_string_to_equal_parts("bbbbbcaaaaa")
#
#
# # Given a string, determine if it consists of all unique characters.
# # For example, the string 'abcde' has all unique characters and should return True.
# # The string 'aabcde' contains duplicate characters and should return False.
#
# def unique_char_string(string):
#     if len(set(string)) == len(string):
#         print(f'{string} contains unique characters')
#     else:
#         print (f'{string} contains duplicate characters')
#
#
# unique_char_string('aabcde')
# unique_char_string('abcde')

#
# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def below_arithmetical_mean(a):
    sum = 0
    n = 0
    below_mean = []
    for i in a:
        sum += i
        n += 1
    avg = sum/n

    for i in a:
        if i < avg:
            below_mean.append(i)

    print (f'Avarage = {avg}')
    print (f'values below average: {below_mean}')

example_1 = [1, 3, 5, 6, 4, 10, 2, 3]
below_arithmetical_mean(example_1)

# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
# [3, 40, 198, 9, 10, 9, 2]
def two_lowest_elements(l):
    lowest1 = l[0] #3
    lowest2 = l[1] #40

    for i in l:
        if i < lowest1:
            lowest2 = lowest1
            lowest1 = i
        elif i < lowest2\
                and i != lowest1:
            lowest2 = i

    print (lowest1, lowest2)


list = [3, 40, 198, 9, 10, 9, 20]

two_lowest_elements(list)



