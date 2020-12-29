# Skeleton file for HW4 - winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.




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


# d
had_complete = lambda n: [[had_local(n, i, j) for j in range(2 ** n)]
                          for i in range(2 ** n)]

############
# QUESTION 4
############

# a
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

############
# QUESTION 5
############

# a
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



############
# QUESTION 6
############

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


########
# Tester
########

def test():
    # print matrix, use this function only to check your results.
    def print_matrix(A):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in A]))

    # Q2-c
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    key = 8
    if(rec_slice_binary_search(lst, key) != 7):
        print("Error in rec_slice_binary_search")

    # Q3-b
    if(had_local(2,2,2) != 1):
        print("Error in had_local")

    # Q4-a
    m = [[0,0,0,2,4,6],
         [0,4,0,2,3,4],
         [0,0,0,3,2,4],
         [2,4,0,0,0,0],
         [3,6,0,4,6,0],
         [3,0,0,0,0,0]]
    rr, rm = find_zero_paths(m)
    if(rr != 4):
        print("Error in find_zero_path")
    print_matrix(rm)

    #Q5-a
    A = [20, 5, 10, 40, 15, 25]
    W = [1, 2, 3, 8, 7, 4]
    k = 10
    if(find_max_profit(A, W, len(A) -1, k) != 60):
        print("Error in find_max_profit")
    #Q5-c
    if (find_max_profit_fast(A, W, len(A) - 1, k) != 60):
        print("Error in find_max_profit_fast")

    #Q6
    if distance('computer', 'commuter') != 1 or \
            distance('sport', 'sort') != 1 or \
            distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
        print("Error in distance")

    if distance_fast('computer', 'commuter') != 1 or \
            distance_fast('sport', 'sort') != 1 or \
            distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
        print("Error in distance_fast")
