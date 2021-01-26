############
# QUESTION 5
############
# a
def prefix_suffix_overlap(lst, k):
    sol_lst = []
    n = len(lst)
    for i in range(n):
        reisha = lst[i][:k]
        for j in range(n):
            if j == i:
                continue
            seifa = lst[j][-k:]
            if reisha == seifa:
                sol_lst.append((i, j))
    return sol_lst


# s0 = "a" * 10
# s1 = "b" * 4 + "a" * 6
# s2 = "c" * 5 + "b" * 4 + "a"
# print(prefix_suffix_overlap([s0, s1, s2], 5))


# c
#########################################
### Dict class ###
#########################################

class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join(
            [str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):
        """ returns ALL values of key as a list, empty list if none """
        i = self.hash_mod(key)
        vals_lst = []
        for x in self.table[i]:
            if key == x[0]:
                vals_lst.append(x[1])
        return vals_lst


#########################################
### End Dict class ###
#########################################

# d
def prefix_suffix_overlap_hash1(lst, k):
    sol_lst = []
    n = len(lst)
    d = Dict(n)
    for i in range(n):
        d.insert(lst[i][:k], i)
    for j in range(n):
        vals = d.find(lst[j][-k:])
        for x in vals:
            if x != j:
                sol_lst.append((x, j))
    return sol_lst


# f
def prefix_suffix_overlap_hash2(lst, k):
    sol_lst = []
    n = len(lst)
    d = {}
    for i in range(n):
        reisha = lst[i][:k]
        if reisha not in d:
            d[reisha] = [i]
        else:
            d[reisha].append(i)
    for j in range(n):
        seifa = lst[j][-k:]
        if seifa in d:
            vals = d[seifa]
            for x in vals:
                if x != j:
                    sol_lst.append((x, j))
    return sol_lst


#     if st in d and d[st] != j:
#         sol_lst.append((d[st], j))
# return sol_lst


import time

ls = ['abc' * 500 + 'def' * 500 + 'jkl' * 500 for i in range(1000)]

for i in [prefix_suffix_overlap,
          prefix_suffix_overlap_hash1,
          prefix_suffix_overlap_hash2]:
    t0 = time.perf_counter()
    i(ls, 1000)
    t1 = time.perf_counter()
    print(i.__name__ + ': ' + str(t1 - t0))
