import math


def inter_to_bin(intermediate, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ converts intermediate format compressed list
        to a string of bits"""
    W_width = math.floor(math.log(W, 2)) + 1
    L_width = math.floor(math.log(L, 2)) + 1
    bits = []
    for elem in intermediate:
        if type(elem) == str:
            bits.append("0")  # to note a single char ahead
            bits.append((bin(ord(elem))[2:]).zfill(7))
        else:  # elem is a list [m,k]
            bits.append("1")  # to note a repetition ahead
            m, k = elem
            bits.append((bin(m)[2:]).zfill(W_width))
            bits.append((bin(k)[2:]).zfill(L_width))
    return "".join(ch for ch in bits)


def maxmatch(T, p, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ Finds a maximum match of length k<=L within a
        W long window, T[p:p+k] = T[p-m:p-m+k].
        Returns m (offset) and k (match length) """
    assert isinstance(T, str)
    n = len(T)
    m = 0
    k = 0
    for offset in range(1, 1 + min(p, W)):
        match_len = 0
        j = p - offset  # starting point of earlier repetition
        while match_len < min(n - p, L) and T[j + match_len] == T[
            p + match_len]:
            match_len += 1  # at this point, T[j:j+match_len]==T[p:p+match_len]
        if match_len > k:
            k = match_len
            m = offset
    return m, k  # returned offset is smallest one (closest to p)
    # among all max matches


def LZW_compress(text, W=2 ** 12 - 1, L=2 ** 5 - 1):
    """ LZW compression of an ascii text. Produces
        a list comprising of either ascii characters
        or pairs [m,k] where 1<=m<=W is an offset and
        3<=k<=L is a match """
    intermediate = []
    n = len(text)
    p = 0
    while p < n:
        m, k = maxmatch(text, p, W, L)
        if k <= 2:
            intermediate.append(text[p])  # a single char
            p += 1
        else:  # k>=3
            intermediate.append([m, k])  # compressing 3+ characters
            p += k
    return intermediate  # a list composed of chars and pairs


def LZW_compress_new(text, start=0, W=2 ** 12 - 1, L=2 ** 5 - 1):
    n = len(text)
    if start >= n:
        return []
    # find the maximal length matching
    m, k = maxmatch(text, start, W, L)
    res1 = [text[start]] + LZW_compress_new(text, start + 1, W, L)
    res1_len = len(inter_to_bin(res1, W, L))
    if k < 3:
        return res1
    res2 = [[m, k]] + LZW_compress_new(text, start + k, W, L)
    res2_len = len(inter_to_bin(res2, W, L))

    if res2_len < res1_len:
        return res2
    return res1


for i in range(97, 99):
    for j in range(97, 99):
        for k in range(97, 99):
            for l in range(97, 99):
                for m in range(97, 99):
                    for n in range(97, 99):
                        for o in range(97, 99):
                            for p in range(97, 99):
                                for q in range(97, 99):
                                    for r in range(97, 99):
                                        for s in range(97, 99):
                                            st = chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n) + chr(o) + chr(p) + chr(q) + chr(r) + chr(s)
                                            assert len(inter_to_bin(LZW_compress_new(st))) >= len(inter_to_bin(LZW_compress(st))), f'{st}\n{LZW_compress(st)}\n{LZW_compress_new(st)}'
