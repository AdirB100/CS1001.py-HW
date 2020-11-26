############
# QUESTION 2
############

# 2a
def coin():
    return random.random() >= 0.5

# 2b 
def uniform(a,b):
    assert a < b
    return (b - a) * random.random() + a

# 2c
def choice(seq):
    if not seq:
        return seq
    return seq[int(len(seq) * random.random())]

# 2d
def weighted_choice(seq, weights):
    assert sum(weights) == 1 and len(seq) == len(weights)
    n = len(seq)
    ran = random.random()
    lst = [0 for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            lst[j] += weights[i]
    lst = [0] + lst
    for i in range(len(lst)-1):
        if lst[i] < ran < lst[i+1]:
            return seq[i]

# 2e
def get_biased_coin(p):
    return lambda: random.random() < p

# 2f
def test_biased_coin(p, num_flips):
    cnt = 0
    for i in range(num_flips):
        cnt += get_biased_coin(p)()
    return cnt/num_flips
