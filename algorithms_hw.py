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
# # # The string 'aabcde' contains duplicate characters and should return False.
# #
# # def unique_char_string(string):
# #     if len(set(string)) == len(string):
# #         print(f'{string} contains unique characters')
# #     else:
# #         print (f'{string} contains duplicate characters')
# #
# #
# # unique_char_string('aabcde')
# # unique_char_string('abcde')
#
# #
# # Below The Arithmetical Mean
# # When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# # The arithmetical mean is the sum of all elements divided by the number of elements.
# # Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
#
# def below_arithmetical_mean(a):
#     sum = 0
#     n = 0
#     below_mean = []
#     for i in a:
#         sum += i
#         n += 1
#     avg = sum/n
#
#     for i in a:
#         if i < avg:
#             below_mean.append(i)
#
#     print (f'Avarage = {avg}')
#     print (f'values below average: {below_mean}')
#
# example_1 = [1, 3, 5, 6, 4, 10, 2, 3]
# below_arithmetical_mean(example_1)
#
# # Two Lowest Elements
# # When given a list of elements, find the two lowest elements.
# # They can be equal to each other or different.
# # Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
# # [3, 40, 198, 9, 10, 9, 2]
# def two_lowest_elements(l):
#     lowest1 = l[0] #3
#     lowest2 = l[1] #40
#
#     for i in l:
#         if i < lowest1:
#             lowest2 = lowest1
#             lowest1 = i
#         elif i < lowest2\
#                 and i != lowest1:
#             lowest2 = i
#
#     print (lowest1, lowest2)
#
#
# list = [3, 40, 198, 9, 10, 9, 20]
#
# two_lowest_elements(list)


#
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D
# and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#
# def plus_one(digits):
#     for i in range(len(digits)):
#         digits[i] += 1
#         if digits[i] == 10:
#             digits[i] = 0
#         if digits[i] > 10:
#             break
#     print(digits)
#
#
# list_1 = [1, 2, 9]
# list_2 = [3, 7, 2, 9, 9]
#
#
# plus_one(list_1)
# plus_one(list_2)
#
#
# # Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# # You are required to solve it without allocating additional storage (operate with the input list).
# # Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
# #           0  1  2  3  4  5   6  7
# def even_first(digits):
#     for i in range(len(digits)):
#         if digits[i] % 2 != 0:
#             digits.remove(digits[i])
#             digits.append(digits[i])
#         else:
#             continue
#     print(digits)
#
#
# list_3 = [7, 3, 5, 6, 4, 10, 3, 2]
#
#
# even_first(list_3)
#

sort_list = [1, 31, 5, 16, 47, 10, 2, 32]


def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    print(f"Selection - {lst}")


selection_sort(sort_list)


def bubble_sort(lst):
    for i in range (len(lst)):
        for j in range(len(lst)-i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(f"Bubble - {lst}")


bubble_sort(sort_list)


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1

        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

    print(f"Insertion - {lst}")


insertion_sort(sort_list)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    return merge_lst(merge_sort(lst[:middle]), merge_sort(lst[middle:]))


def merge_lst(left_lst, right_lst):
    merged_lst = []
    i = j = 0
    while i < len(left_lst) or j < len(right_lst):
        if i == len(left_lst):
            merged_lst.append(right_lst[j])
            j += 1
            continue
        if j == len(right_lst):
            merged_lst.append(left_lst[i])
            i += 1
            continue

        if left_lst[i] <= right_lst[j]:
            merged_lst.append(left_lst[i])
            i +=1
        else:
            merged_lst.append(right_lst[j])
            j += 1
    print(f"Merged - {merged_lst}")


merge_sort(sort_list)
print(merge_sort(sort_list))