############
# QUESTION 3
############
import random


# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):
    n = len(lst)
    if k > n:
        raise ValueError('k parameter needs to be less or equal to the ' +
                         'length of lst parameter')
    sub_k_lists = []
    for i in range(0, n, k):
        sub_k_list = lst[i:i + k]
        selection_sort(sub_k_list)
        sub_k_lists.append(sub_k_list)
    return sub_k_lists


# lst=[random.choice(range(1000)) for i in range(1000000)]
# import time
# t0=time.perf_counter()
# lst[100000:500000]
# t1=time.perf_counter()
# print(t1-t0)
# lst = [random.choice(range(1000)) for i in range(100)]
# print(lst)
# print(generate_sorted_blocks(lst, 10))

# import time
#
# for j in [800, 1600,3200,6400]:
#     t0 = time.perf_counter()
#     generate_sorted_blocks([random.choice(range(1000)) for i in range(16000)], j)
#     t1 = time.perf_counter()
#     print(t1 - t0)


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    i = 0
    while len(lst) != 1:
        while i < len(lst) - 1:
            lst[i] = merge(lst[i], lst[i + 1])
            lst.pop(i + 1)
            i += 1
        i = 0
    return lst[0]


#import time
#
# ls = eval(('[' + str([f'a{i}' for i in range(1, 3)]).replace("'",'') + ' ' + ''.join([f'for a{i} in range(3) ' for i in range(1, 3)]))[:-1] + ']')
# t0 = time.perf_counter()
# merge_sorted_blocks([[random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)],
#                      [random.choice(range(100)) for i in range(200)]])
# t1 = time.perf_counter()
# print(t1 - t0)


# def merge_sorted_blocks(lst):
#     lst1, lst2 = [], []
#     for i in range(len(lst) // 2):
#         for j in lst[i]:
#             lst1.append(j)
#     for i in range(len(lst) // 2, len(lst)):
#         for j in lst[i]:
#             lst2.append(j)
#     return merge(lst1, lst2)
#
#
# def merge_sorted_blocks(lst):
#     if type(lst[0]) == list:
#         lst2 = []
#         for i in lst:
#             for j in i:
#                 lst2.append(j)
#         lst = lst2
#     n = len(lst)
#     if n == 1:
#         return lst
#     ls1, ls2 = lst[:n // 2], lst[n // 2:]
#     return merge(merge_sorted_blocks(ls1), merge_sorted_blocks(ls2))
#
#
# def merge_sorted_blocks(lst):
#     m = len(lst)
#     for i in range(1, m):
#         lst[0] = merge(lst[0], lst[i])
#     return lst[0]


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))

print(sort_by_block_merge([7,5,4,8,2,9,4,1], 3))
