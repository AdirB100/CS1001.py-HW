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
