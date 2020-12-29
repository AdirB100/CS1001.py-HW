############
# QUESTION 6
############

# def distance(s1, s2):
#     i1 = 0
#     i2 = 0
#     return distance_rec(s1, s2, i1, i2, 0)
#
#
# def distance_rec(s1, s2, i1, i2, depth):
#     print(f'd={depth}:', (s1[i1:], s2[i2:]))
#     if i1 == len(s1):
#         print(f'return: {len(s2) - i2}')
#         return len(s2) - i2
#     if i2 == len(s2):
#         print(f'return: {len(s1) - i1}')
#         return len(s1) - i1
#     if s1[i1] == s2[i2]:
#         eq = distance_rec(s1, s2, i1 + 1, i2 + 1, depth + 1)
#         print(f'd={depth}:', (s1[i1:], s2[i2:]))
#         return eq
#     print('Option 1:')
#     opt1 = distance_rec(s1, s2, i1 + 1, i2, depth + 1)
#     print(f'd={depth}:', (s1[i1:], s2[i2:]))
#     print('Option 2:')
#     opt2 = distance_rec(s1, s2, i1, i2 + 1, depth + 1)
#     print(f'd={depth}:', (s1[i1:], s2[i2:]))
#     print('Option 3:')
#     opt3 = distance_rec(s1, s2, i1 + 1, i2 + 1, depth + 1)
#     print(f'd={depth}:', (s1[i1:], s2[i2:]))
#     print(f'opt1 = {opt1} ', (s1[i1 + 1:], s2[i2:]))
#     print(f'opt2 = {opt2} ', (s1[i1:], s2[i2 + 1:]))
#     print(f'opt3 = {opt3} ', (s1[i1 + 1:], s2[i2 + 1:]))
#     print(f'''return: 1+{opt1 if opt1 <= opt2 and opt1 <= opt3
#         else opt2 if opt2 <= opt1 and opt2 <= opt3
#         else opt3}''')
#     return 1 + opt1 if opt1 <= opt2 and opt1 <= opt3 \
#         else 1 + opt2 if opt2 <= opt1 and opt2 <= opt3 \
#         else 1 + opt3


def distance(s1, s2):
    i1 = 0
    i2 = 0
    return distance_rec(s1, s2, i1, i2)


def distance_rec(s1, s2, i1, i2):
    if i1 == len(s1):
        return len(s2) - i2  # edge case: add the remaining letters of s2
    if i2 == len(s2):
        return len(s1) - i1  # edge case: remove the rest letters of s1
    if s1[i1] == s2[i2]:
        return distance_rec(s1, s2, i1 + 1, i2 + 1)  # check the rest of s1&s2
    opt1 = 1 + distance_rec(s1, s2, i1 + 1, i2)  # remove left rel letter of s1
    opt2 = 1 + distance_rec(s1, s2, i1, i2 + 1)  # add first rel letter from s2
    opt3 = 1 + distance_rec(s1, s2, i1 + 1, i2 + 1)  # change to rel letter s2
    return opt1 if opt1 <= opt2 and opt1 <= opt3 \
      else opt2 if opt2 <= opt1 and opt2 <= opt3 \
      else opt3


# def distance(s1, s2):
#     if not s1 or not s2:
#         return len(s1 + s2)
#     if s1[0] == s2[0]:
#         return distance(s1[1:], s2[1:])
#     opt1 = 1 + distance(s1[1:], s2)
#     opt2 = 1 + distance(s1, s2[1:])
#     opt3 = 1 + distance(s1[1:], s2[1:])
#     return opt1 if opt1 <= opt2 and opt1 <= opt3 \
#         else opt2 if opt2 <= opt1 and opt2 <= opt3 \
#         else opt3


# print(distance('kitten', 'sittign'))


def distance_fast(s1, s2):
    i1 = 0
    i2 = 0
    dic = {}
    return distance_mem(s1, s2, i1, i2, dic)


def distance_mem(s1, s2, i1, i2, dic):
    if i1 == len(s1):
        return len(s2) - i2
    if i2 == len(s2):
        return len(s1) - i1
    if (i1, i2) in dic or (i2, i1) in dic:
        return dic[(i1, i2)] if (i1, i2) in dic else dic[(i2, i1)]
    if s1[i1] == s2[i2]:
        eq = distance_mem(s1, s2, i1 + 1, i2 + 1, dic)
        dic[(i1, i2)] = eq
        return eq
    opt1 = 1 + distance_mem(s1, s2, i1 + 1, i2, dic)
    opt2 = 1 + distance_mem(s1, s2, i1, i2 + 1, dic)
    opt3 = 1 + distance_mem(s1, s2, i1 + 1, i2 + 1, dic)
    mini = opt1 if opt1 <= opt2 and opt1 <= opt3 \
        else opt2 if opt2 <= opt1 and opt2 <= opt3 \
        else opt3
    dic[(i1, i2)] = mini
    return mini

# print(distance_fast('kitten', 'sittign'))
# import time
#
# t0 = time.perf_counter()
# distance('kittdffsgdsen', 'sittidfsssdng')
# t1 = time.perf_counter()
# distance_fast('kittdffsgdsen', 'sittidfsssdng')
# t2 = time.perf_counter()
# print(f'slow: {t1-t0}, fast: {t2-t1}')
