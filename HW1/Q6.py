#Question 6
def max_div_seq(n, k):
    if n==0:
        return 0
    n = str(n)
    lst = []
    while len(n) > 0:
        for j in range(len(n)):
            if int(n[j]) % k != 0:
                lst.append(j)
                break
        if len(n) == j+1:
            return max(lst)
        n = n[j+1:]
    return max(lst)
