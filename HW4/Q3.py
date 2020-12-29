############
# QUESTION 3
############

# b
def had_local(n, i, j):
    if n == 0:
        return 0
    critic_val = pow(2, n - 1)
    if i >= critic_val and j >= critic_val:
        return 1 - had_local(n - 1, i - critic_val, j - critic_val)
    if i >= critic_val:
        return had_local(n - 1, i - critic_val, j)
    if j >= critic_val:
        return had_local(n - 1, i, j - critic_val)
    return had_local(n - 1, i, j)


# res_func = []
# for i in range(8):
#     for j in range(8):
#         res_func.append(had_local(3, i, j))
# assert res_func == [0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1]

# import time
#
# t0 = time.perf_counter()
# had_local(1000, 100, 95)
# t1 = time.perf_counter()
# print(t1 - t0)

# d
had_complete = lambda n: [[had_local(n, i, j) for j in range(2 ** n)]
                          for i in range(2 ** n)]


print(had_complete(2))