# Skeleton file for HW4 - winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = []



############
# QUESTION 2
############

 # c
def rec_slice_binary_search(lst, key):
    pass  # replace this with your code


############
# QUESTION 3
############

# b
def had_local(n, i, j):
    pass  # replace this with your code


# d
had_complete = lambda n: None  # replace this with your code

############
# QUESTION 4
############

# a
def find_zero_paths(m):
    pass  # replace this with your code

############
# QUESTION 5
############

# a
def find_max_profit(A, W, n, k):
    pass  # replace this with your code

# c
def find_max_profit_fast(A, W, n, k):
    pass  # replace this with your code



############
# QUESTION 6
############

def distance(s1, s2):
    pass


def distance_fast(s1, s2):
    pass


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
    if(find_max_profit(A, W, len(A), k) != 60):
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