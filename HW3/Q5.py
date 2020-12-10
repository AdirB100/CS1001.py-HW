############
# QUESTION 5
############

# a
def string_to_int(s):
    keys = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    sol = 0
    for i in range(len(s)):
        sol += keys[s[i]] * 5 ** (len(s) - 1 - i)
    return sol


# import time
#
# t0 = time.perf_counter()
# string_to_int('e'*1000)
# t1 = time.perf_counter()
# print(t1 - t0)


# b
# def int_to_string(k, n):
#     assert 0 <= n <= 5 ** k - 1
#     alphabet = 'abcde'
#     s = ''
#     while n:
#         s = alphabet[n % 5] + s
#         n //= 5
#     s = 'a' * (k - len(s)) + s
#     return s

def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    alphabet = 'abcde'
    s = []
    while n:
        s.insert(0, alphabet[n % 5])
        n //= 5
    s = ''.join(s)
    s = 'a' * (k - len(s)) + s
    return s


# print(int_to_string(6, 10587))
# for j in range(10):
#     for i in range(5 ** j):
#         assert string_to_int(int_to_string(j, i)) == i
#
# for i in range(5**3):
#     if string_to_int(int_to_string(3, i)) != i:
#         print("Problem with ", i)
#
# alphabet = ["a", "b", "c", "d", "e"]
# lst = [x + y + z for x in alphabet for y in alphabet for z in alphabet]
# for item in lst:
#     if int_to_string(3, string_to_int(item)) != item:
#         print("Problem with ", item)


# c
def sort_strings1(lst, k):
    sol = []
    aux_lst = [0 for i in range(5 ** k)]
    for st in lst:
        aux_lst[string_to_int(st)] += 1
    for i in range(len(aux_lst)):
        while aux_lst[i]:
            sol.append(int_to_string(k, i))
            aux_lst[i] -= 1
    return sol


# print(sort_strings1(
#     ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea',
#      'ccea'], 4))


# def sort_strings1(lst, k):
#     aux_lst = eval('[' + ''.join([f'a{i}+' for i in range(1, k)]) + f'a{k} ' +\
#                    ''.join([f'for a{i} in alphabet ' for i in range(1, k)]) +\
#                    f'for a{k} in alphabet' + ']', {'alphabet': 'abcde'})
#     return aux_lst
#
# print(sort_strings1(['aede'], 8))


# e
def sort_strings2(lst, k):
    n = len(lst)
    sol = []
    for i in range(5 ** k):
        for j in range(n):
            if string_to_int(lst[j]) == i:
                sol.append(int_to_string(k, i))
    return sol

# print(sort_strings2(['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea'], 4))
