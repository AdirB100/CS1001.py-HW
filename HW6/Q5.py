############
# QUESTION 5
############

# (b)
def CYK_d(st, rule_dict, start_var):
    ''' What is the minimal depth of a parse tree that generates st? '''
    n = len(st)

    # table for the dynamic programming algorithm
    table = [[None for j in range(n + 1)] for i in range(n)]
    # Initialize the relevant triangular region with empty sets
    for i in range(n):
        for j in range(i + 1, n + 1):
            table[i][j] = dict()

    # Fill the table cells representing substrings of length 1
    fill_length_1_cells_d(table, rule_dict, st)

    # Fill the table cells representing substrings of length >=2
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length
            fill_cell_d(table, i, j, rule_dict)

    # Original CYK: return start_var in table[0][n]
    if start_var in table[0][n]:
        return table[0][n][start_var]
    return -1


def fill_length_1_cells_d(table, rule_dict, st):
    n = len(st)
    for i in range(n):
        for lhs in rule_dict:  # lhs is a single variable
            if st[i] in rule_dict[lhs]:
                table[i][i+1][lhs] = 1


def fill_cell_d(table, i, j, rule_dict):
    for k in range(i + 1, j):  # non trivial partitions of s[i:j]
        for lhs in rule_dict:  # lhs is a single variable
            for rhs in rule_dict[lhs]:
                if len(rhs) == 2:  # rule like A -> XY (not like A -> a)
                    X, Y = rhs[0], rhs[1]
                    if X in table[i][k] and Y in table[k][j]:
                        current_depth = 1+max(table[i][k][X], table[k][j][Y])
                        if lhs in table[i][j]:
                            table[i][j][lhs] = min(table[i][j][lhs], current_depth)
                        else:
                            table[i][j][lhs] = current_depth


# Question 5
rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
if CYK_d("baaba", rule_dict, "S") != 4:
    print("Error in CYK_d")
if CYK_d("baab", rule_dict, "S") != -1:
    print("Error in CYK_d")