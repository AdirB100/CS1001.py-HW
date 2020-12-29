############
# QUESTION 2
############

# c
def rec_slice_binary_search(lst, key):
    n = len(lst)
    if n <= 0:
        return None

    if key == lst[n // 2]:
        return n // 2

    elif key < lst[n // 2]:
        return rec_slice_binary_search(lst[0:n // 2], key)

    else:
        right = rec_slice_binary_search(lst[n // 2 + 1:n], key)
        return right if right is None else right + n // 2 + 1


# import time
#
# t0 = time.perf_counter()
# rec_slice_binary_search(list(range(1, 20000001)), 0)
# t1 = time.perf_counter()
# print(t1 - t0)
