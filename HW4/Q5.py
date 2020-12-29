############
# QUESTION 5
############

# a
# def find_max_profit(A, W, n, k):
#     if k < 0:
#         return 0
#     cur_price = n if n != len(A) - 1 else 0
#     if len(A) == 0:
#         return cur_price
#     w_price = cur_price + A[0]
#     w_first = find_max_profit(A[1:], W[1:], w_price, k - W[0])
#     wo_first = find_max_profit(A[1:], W[1:], cur_price, k)
#     return w_first if w_first > wo_first else wo_first


# def find_max_profit(A, W, n, k):
#     amount = 0
#     return find_max_profit_rec(A, W, n, k, amount)
#
# def find_max_profit_rec(A, W, n, k, amount):
#     if k < 0:
#         return 0
#     if n == 0 or k == 0:
#         return amount
#     w_amount = amount + A[0]
#     w_first = find_max_profit_rec(A[1:], W[1:], n - 1, k - W[0], w_amount)
#     wo_first = find_max_profit_rec(A[1:], W[1:], n - 1, k, amount)
#     return w_first if w_first > wo_first else wo_first

# def find_max_profit(A, W, n, k):
#     amount = 0
#     i = 0
#     return find_max_profit_rec(A, W, i, k, amount)
#
#
# def find_max_profit_rec(A, W, i, k, amount):
#     if k < 0:
#         return 0
#     if i == len(A) - 1 or k == 0:
#         return amount
#     w_first = find_max_profit_rec(A, W, i + 1, k - W[i], amount + A[i])
#     wo_first = find_max_profit_rec(A, W, i + 1, k, amount)
#     return w_first if w_first > wo_first else wo_first


def find_max_profit(A, W, n, k):
    if n == len(A) - 1:
        A.append(0)
    if k < 0:
        return A[-1] - A[len(W) - 2 - n]
    if n < 0 or k == 0:
        return A[-1]
    A[-1] += A[len(W) - 1 - n]
    w_first = find_max_profit(A, W, n - 1, k - W[len(W) - 1 - n])
    A[-1] -= A[len(W) - 1 - n]
    wo_first = find_max_profit(A, W, n - 1, k)
    return w_first if w_first > wo_first else wo_first


# print(find_max_profit([10, 15, 25], [8, 7, 4], 2, 15))


# A = [20, 5, 10, 40, 15, 25]
# W = [1, 2, 3, 8, 7, 4]
# k = 10
# if (find_max_profit(A, W, len(A)-1, k) != 60):
#     print("Error in find_max_profit")


# c


def find_max_profit_fast(A, W, n, k):
    dic = {}
    return find_max_profit_fast_rec(A, W, n, k, dic)


def find_max_profit_fast_rec(A, W, n, k, dic):
    if n == len(A) - 1:
        A.append(0)
    if k < 0:
        return A[-1] - A[len(W) - 2 - n]
    if n < 0 or k == 0:
        return A[-1]
    if (n, k) in dic:
        return A[-1] + dic[(n, k)]
    A[-1] += A[len(W) - 1 - n]
    w_first = find_max_profit(A, W, n - 1, k - W[len(W) - 1 - n])
    A[-1] -= A[len(W) - 1 - n]
    wo_first = find_max_profit(A, W, n - 1, k)
    maxi = w_first if w_first > wo_first else wo_first
    dic[(n, k)] = maxi
    return maxi


# import random
# import time
#
# A = [76, 2, 191, 177, 115, 104, 86, 147, 8, 82,83,84,85,86,87,88,89,90,91,92]
# W = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
# n = 19
# k = 46365
# t0 = time.perf_counter()
# find_max_profit(A, W, n, k)
# t1 = time.perf_counter()
# find_max_profit_fast(A, W, n, k)
# t2 = time.perf_counter()
# print(find_max_profit(A, W, n, k) == find_max_profit_fast(A, W, n, k))
# print(f'slow: {t1 - t0}, fast: {t2 - t1}')
