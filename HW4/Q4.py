############
# QUESTION 4
############

# a
# def find_zero_paths(m):
#     n = len(m)
#     if m == [[0]]:
#         return 1
#     if m[0][0] != 0:
#         return 0
#     if n != 1:
#         out = m.pop(0)
#         down = find_zero_paths(m)
#         m.insert(0, out)
#     else:
#         down = 0
#     outs = []
#     if len(m[0]) != 1:
#         for row in m:
#             outs.append(row.pop(0))
#         right = find_zero_paths(m)
#         for row in m:
#             row.insert(0, outs.pop(0))
#     else:
#         right = 0
#     return down + right


# def find_zero_paths(m):
#     if len(m) == 0 or len(m[0]) == 0:
#         return 0
#     if len(m) == 1 and len(m[0]) == 1 and m[0][0] == 0:
#         return 1
#     if m[0][0] != 0:
#         return 0
#     out = m.pop(0)
#     down = find_zero_paths(m)
#     m.insert(0, out)
#     outs = [row.pop(0) for row in m]
#     right = find_zero_paths(m)
#     for row in m:
#         row.insert(0, outs.pop(0))
#     return down + right


# def find_zero_paths(m):
#     i = j = 0
#     ls = [[0 for k in m]
#     return find_zero_paths_rec(m, i, j, dic)
#
#
# def find_zero_paths_rec(m, i, j, dic):
#     if i >= len(m) or j >= len(m) or m[i][j] != 0:
#         return 0
#     if i == j == len(m) - 1:
#         return 1
#     r = find_zero_paths_rec(m, i, j + 1) + find_zero_paths_rec(m, i + 1, j)

def find_zero_paths(m):
    i = j = 0
    ls = [[0 for k in m] for q in m]
    return find_zero_paths_rec(m, i, j, ls)


def find_zero_paths_rec(m, i, j, ls):
    if i >= len(m) or j >= len(m) or m[i][j] != 0:
        return (0, ls) if i == j == 0 else 0
    if i == j == len(m) - 1:
        ls[i][j] += 1
        return 1
    r = find_zero_paths_rec(m, i, j + 1, ls) + \
        find_zero_paths_rec(m, i + 1, j, ls)
    ls[i][j] += r
    return (r, ls) if i == j == 0 else r

# print(find_zero_paths([]))

# print(find_zero_paths([[0, 0, 0, 5, 7, 9],
#                        [0, 9, 0, 3, 1, 5],
#                        [0, 0, 0, 8, 7, 6],
#                        [1, 6, 0, 0, 0, 0],
#                        [7, 3, 0, 6, 1, 0],
#                        [2, 4, 0, 0, 0, 0]]))


# def print_matrix(A):
#     print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#                      for row in A]))
# m = [[0, 0, 0, 2, 4, 6],
#      [0, 4, 0, 2, 3, 4],
#      [0, 0, 0, 3, 2, 4],
#      [2, 4, 0, 0, 0, 0],
#      [3, 6, 0, 4, 6, 0],
#      [3, 0, 0, 0, 0, 0]]
# rr, rm = find_zero_paths(m)
# if (rr != 4):
#     print("Error in find_zero_path")
# print_matrix(rm)
