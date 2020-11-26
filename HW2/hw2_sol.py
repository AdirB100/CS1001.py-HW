#Skeleton file for HW2 - Winter 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw2_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.


import random # loads python's random module in order to use random.random() in question 2


############
# QUESTION 1
############

def poker_hand(hand):
    poker_hands = ["High Card", "One Pair", "Two Pairs", "Three of a Kind",
                   "Straight", "Flush", "Full House", "Four of a Kind",
                   "Straight Flush", "Royal Flush"]
    rank_dict = {'23456789TJQKA'[i]: i + 2 for i in range(13)}
    lst_hand = hand.split()
    suits, ranks = [lst_hand[i][1] for i in range(5)], [lst_hand[i][0] for i in range(5)]
    sorted_ranks_int = sorted([rank_dict[i] for i in ranks])
    same_suit = suits.count(suits[0]) == 5
    rank_difference = [sorted_ranks_int[i + 1] - sorted_ranks_int[i] for i in range(4)]
    sequential_rank = rank_difference.count(rank_difference[0]) == 4
    rank_count = {}
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1
    if sequential_rank:
        if same_suit:
            return poker_hands[9] if sorted_ranks_int[0] == 10 else poker_hands[8]
        return poker_hands[4]
    if same_suit:
        return poker_hands[5]
    count_vals = list(rank_count.values())
    return poker_hands[7] if 4 in count_vals \
      else poker_hands[6] if 3 in count_vals and 2 in count_vals \
      else poker_hands[3] if 3 in count_vals \
      else poker_hands[2] if count_vals.count(2) == 2 \
      else poker_hands[1] if 2 in count_vals \
      else poker_hands[0]


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


############
# QUESTION 3
############

# 3a
def has_repeat1(s, k):
    seq_list = []
    for i in range(len(s) - k + 1):
        seq_list.append(s[i:i + k])
    for seq in seq_list:
        if seq_list.count(seq) > 1:
            return True
    return False

# 3b
def has_repeat2(s, k):
    for i in range(len(s) - k):
        for j in range(i+1, len(s) - k + 1):
            if s[i:i+k] == s[j:j+k]:
                return True
    return False


############
# QUESTION 4
############

def interpolate(xy, x_hat):
    # Assume x_hat values are within x values range
    if len(xy) <= 1:
        raise ValueError('please enter at least two valid measurements')
    times_list = sorted([measure_tup[0] for measure_tup in xy])
    if all([req_x in times_list for req_x in x_hat]):
        return [(req_x, xy[times_list.index(req_x)][1]) for req_x in x_hat]
    req_x_zone_dic = {}
    for req_x in x_hat:
        for meas_index in range(len(xy) - 1):
            if times_list[meas_index] <= req_x <= times_list[meas_index + 1]:
                req_x_zone_dic[req_x] = meas_index
                break
    zone_lin_dic = {}
    lin = lambda tup1, tup2: lambda x: (tup2[1] - tup1[1]) / (tup2[0] - tup1[0]) * (x - tup1[0]) + tup1[1]
    for zone in sorted(list(set(req_x_zone_dic.values()))):
        zone_lin_dic[zone] = lin(xy[zone], xy[zone + 1])
    return [(req_x, zone_lin_dic[req_x_zone_dic[req_x]](req_x)) for req_x in x_hat]


############
# QUESTION 5
############

def parse_primes(filename):
    primes = []
    with open(filename, "r") as f:
        for line in f:
            primes += [int(num_str) for num_str in line.split(" ")[:-1] if num_str]
    return set(primes)


# 5a
def check_goldbach_for_num(n, primes_set):
    ord_primes_list = sorted(list(primes_set))
    for i in range(len(ord_primes_list)):
        for j in range(i, len(ord_primes_list)):
            if ord_primes_list[i] + ord_primes_list[j] == n:
                return True
    return False

# 5b
def check_goldbach_for_range(limit, primes_set):
    ord_primes_list = sorted(list(primes_set))
    range2check = range(4, limit, 2)
    for even_num in range2check:
        indicator = 0
        for i in range(len(ord_primes_list)):
            for j in range(i, len(ord_primes_list)):
                if ord_primes_list[i] + ord_primes_list[j] == even_num:
                    indicator = 1
                    break
            if indicator == 1:
                break
            if i == len(ord_primes_list) - 1:
                return False
    return True

# 5c1
def check_goldbach_for_num_stats(n, primes_set):
    ord_primes_list = sorted(list(primes_set))
    cnt = 0
    for i in range(len(ord_primes_list)):
        for j in range(i, len(ord_primes_list)):
            if ord_primes_list[i] + ord_primes_list[j] == n:
                cnt += 1
    return cnt

# 5c2    
def check_goldbach_stats(limit, primes_set):
    range2check = range(4, limit, 2)
    dic = {}
    for even_num in range2check:
        key = check_goldbach_for_num_stats(even_num, primes_set)
        dic[key] = dic.get(key, 0) + 1
    return dic


############
# QUESTION 6
############

# 6a
def add(bin1, bin2):
    if len(bin1) < len(bin2):
        bin1 = '0' * (len(bin2) - len(bin1)) + bin1
    elif len(bin1) > len(bin2):
        bin2 = '0' * (len(bin1) - len(bin2)) + bin2
    sol = ''
    carry = '0'
    for i in range(len(bin1) - 1, -1, -1):
        concat = carry + bin1[i] + bin2[i]
        if concat.count('1') == 3:
            sol = '1' + sol
            carry = '1'
        elif concat.count('1') == 2:
            sol = '0' + sol
            carry = '1'
        elif concat.count('1') == 1:
            sol = '1' + sol
            carry = '0'
        else:
            sol = '0' + sol
            carry = '0'
    if carry == '1':
        sol = '1' + sol
    return sol

# 6b
def sub(bin1, bin2):
    bin2 = '0' * (len(bin1) - len(bin2)) + bin2
    sol = ''
    for i in range(len(bin1) - 1, -1, -1):
        if bin1[i] == '1' and bin2[i] == '0':
            sol = '1' + sol
        elif bin1[i] == bin2[i]:
            if i == 0 and len(bin1) != 1:
                break
            sol = '0' + sol
        else:
            sol = '1' + sol
            if i == 1:
                return sol
            for j in range(i - 1, -1, -1):
                if bin1[j] == '0':
                    bin1 = bin1[:j] + '1' + bin1[j + 1:]
                else:
                    bin1 = bin1[:j] + '0' + bin1[j + 1:]
                    break
    if sol.count('1') == 0:
        return '0'
    for k in range(len(sol)):
        if sol[k] == '1':
            sol = sol[k:]
            break
    return sol

# 6c
def inc(binary):
    return add(binary, '1')

# 6d
def dec(binary):
    return sub(binary, '1')

# 6e
def mult(bin1, bin2):
    for j in range(len(bin2) - 1, -1, -1):
        locals()[f'line{len(bin2) - 1 - j}'] = '0' * (len(bin2) - 1 - j)
        for i in range(len(bin1) - 1, -1, -1):
            locals()[f'line{len(bin2) - 1 - j}'] = ('1' if bin2[j] == '1' and bin1[i] == '1' else '0') \
                                                   + locals()[f'line{len(bin2) - 1 - j}']
    for i in range(1, len(bin2)):
        locals()[f'line{0}'] = add(locals()[f'line{0}'], locals()[f'line{i}'])
    sol = locals()[f'line{0}']
    if sol.count('1') == 0:
        return '0'
    return sol


########
# Tester
########

def test():
    # 1
    if poker_hand("5H 5C 6S 7S KD") != 'One Pair' or \
       poker_hand("5D 8C 9S JS AC") != 'High Card' or \
       poker_hand("3D 6D 7D TD QD") != 'Flush' or \
       poker_hand("3C 3D 3S 9S 9D") != 'Full House' or \
       poker_hand("AC TC JC KC QC") != 'Royal Flush' or \
       poker_hand("AC TC JC KC QD") != 'Straight':
        print("error in poker_hand")

    # 2a
    if coin() not in [True, False]:
        print("error in coin")

    # 2b
    if not (-0.2 <= uniform(-0.2, 1.3) < 1.3):
        print("error in uniform")

    # 2c
    if choice(range(7)) not in range(7):
        print("error in choice")

    # 2d
    if weighted_choice([1, 2, 3], [0.1, 0.1, 0.8]) not in [1, 2, 3]:
        print("error in weighted_choice")

    # 2e
    if not callable(get_biased_coin(0.8)) or get_biased_coin(0.3)() not in [True, False]:
        print("error in get_biased_coin")

    # 2f
    if abs(test_biased_coin(0.3, 100000) - 0.3) > 0.01:
        print("error in test_biased_coin")

    # 3a
    if not has_repeat1("ababa", 3) or \
       has_repeat1("ababa", 4) or \
       not has_repeat1("aba",1):
        print("error in has_repeat1()")

    # 3b
    if not has_repeat2("ababa", 3) or \
       has_repeat2("ababa", 4) or \
       not has_repeat2("aba",1):
        print("error in has_repeat2()")
    
    # 4
    if interpolate([(1, 10), (4, 40)], [4, 2, 3]) != [(4, 40), (2, 20.0), (3, 30.0)] or \
       interpolate([(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)], [-2.5, -1.5, 0.5, 1.5, 2.5]) != [(-2.5, 6.5), (-1.5, 2.5), (0.5, 0.5), (1.5, 2.5), (2.5, 6.5)]:
        print("error in interpolate")

    # 5a
    if not check_goldbach_for_num(10, {2, 3, 5, 7}) or \
       check_goldbach_for_num(10, {2, 3}):
        print("error in check_goldbach_for_num()")

    # 5b
    if not check_goldbach_for_range(20, {2, 3, 5, 7, 11}) or \
       check_goldbach_for_range(21, {2, 3, 5, 7, 11}):
        print("error in check_goldbach_for_range()")

    # 5c
    primes_set = parse_primes('primes.txt')
    if check_goldbach_for_num_stats(20, primes_set) != 2 or \
       check_goldbach_for_num_stats(10, primes_set) != 2:
        print("error in check_goldbach_for_num_stats()")

    if check_goldbach_stats(11, primes_set) != {1: 3, 2: 1}:
        print("error in check_goldbach_stats")

    # 6a
    if add("10", "0") != "10" or \
       add("0", "0") != "0" or \
       add("1001", "11") != "1100":
        print("error in add")

    # 6b
    if sub("10", "0") != "10" or \
       sub("0", "0") != "0" or \
       sub("1000", "11") != "101":
        print("error in sub")

    # 6c
    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc")

    # 6d
    if dec("1") != "0" or \
       dec("101") != "100" or \
       dec("100") != "11" or \
       dec(dec("100")) != "10":
        print("error in dec")

    # 6e
    if mult("0", "10") != "0" or \
       mult("0", "0") != "0" or \
       mult("10", "1010") != "10100" or \
       mult("1", "1011") != "1011" or \
       mult("11", "111") != "10101":
        print("error in mult")
    
