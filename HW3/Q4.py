############
# QUESTION 4
############

# def find(lst, s):
#     n = len(lst)
#     m = 0
#     while n > 1:
#         if s == lst[(n - 1) // 2]:
#             return m + (n - 1) // 2
#         if s > lst[(n - 1) // 2]:
#             if s > lst[((n - 1) // 2) - 1]:
#                 lst = lst[((n - 1) // 2) + 1:]
#                 m += ((n - 1) // 2) + 1
#             elif s == lst[((n - 1) // 2) - 1]:
#                 return m + (n - 1) // 2 - 1
#             else:
#                 return None
#         else:
#             if s < lst[((n - 1) // 2) + 1]:
#                 lst = lst[:(n - 1) // 2]
#             elif s == lst[((n - 1) // 2) + 1]:
#                 return m + ((n - 1) // 2) + 1
#             else:
#                 return None
#         n = len(lst)
#     return m + n - 1 if lst[n - 1] == s else None

def find(lst, s):
    n = len(lst)
    left = 0
    right = n - 1
    if n == 2:
        return 0 if lst[0] == s else 1 if lst[1] == s else None
    while left <= right:
        mid = (left + right) // 2  # middle rounded down
        if left == right:
            return mid if lst[mid] == s else None
        if s == lst[mid]:  # item found
            return mid
        if s == lst[mid - 1]:
            return mid - 1
        if s == lst[mid + 1]:
            return mid + 1
        elif s < lst[mid - 1]:  # item cannot be in top half
            right = mid - 2
        else:
            left = mid + 2
    return None


# for i in [381, 369, 441, 598, 467, 656, 689, 780, 772, 811]:
#     print(find([381, 369, 441, 598, 467, 656, 689, 780, 772, 811], i))
# print(find([381, 369, 441, 598, 467, 656, 689, 780, 772, 811], 500))
# for i in [2, 1, 3, 5, 4, 7, 6, 8, 9]:
#     print(find([2, 1, 3, 5, 4, 7, 6, 8, 9], i))
# print(find([5,7,6], 8))


def sort_from_almost(lst):
    for i in range(len(lst) - 1):
        if lst[i + 1] < lst[i]:
            tmp = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = tmp
    return None


# lst_example = [381, 369, 441, 598, 467, 656, 689, 780, 772, 811]
# sort_from_almost(lst_example)
# print(lst_example)


def find_local_min(lst):
    n = len(lst)
    if n == 1:
        return 0
    for i in range((n - 1) // 2 + 1):
        if lst[i] <= lst[i + 1] or lst[n - 2 - i] >= lst[n - 1 - i]:
            return i if lst[i] <= lst[i + 1] else n - 1 - i


# import random
# 
# ls = [random.choice(range(100)) for i in range(10)]
# print(ls)
# print(find_local_min(ls))
