def text2Unicode(text):
    """ return a list of ints representing text"""
    lst = []
    for c in text:
        lst += [ord(c)]
    return lst


def text2bits(text):
    """ return a string of bits representing text """
    lst = []
    for c in text:
        lst += [bin(ord(c))[2:]]
    return lst


############
# QUESTION 2
############

def text_2_16bits(text):
    return ''.join(['0' * (16 - len(bin(ord(c))[2:])) +
                    bin(ord(c))[2:] for c in text])


# Q2 - A, b
def bits_2_text(b_text):
    sep_bits = [b_text[i:i + 16] for i in range(0, len(b_text), 16)]
    return ''.join([chr(int(c, 2)) for c in sep_bits])


bit64_to_float_value3 = lambda st: 0.0 if st.count('0') == 64 \
    else (-1) ** int(st[0]) * 2 ** (int(st[1:12], 2) - 1023) * \
         (1 + int(st[12:], 2) * 2 ** (-52))


# Q2 - B
def float_add(a, b):
    exp1, exp2, = int(a[1:12], 2), int(b[1:12], 2)
    bfrac1_1, bfrac2_1 = '1' + a[12:-1], '1' + b[12:-1]
    shift = exp1 - exp2
    frac1_1 = -int(('0' * -shift + bfrac1_1)[:52], 2) if int(a[0]) \
          else int(('0' * -shift + bfrac1_1)[:52], 2)
    frac2_1 = -int(('0' * shift + bfrac2_1)[:52], 2) if int(b[0]) \
          else int(('0' * shift + bfrac2_1)[:52], 2)
    frac_sol_1 = frac1_1 + frac2_1
    bfrac_sol_1 = bin(abs(frac_sol_1))[2:]
    bfrac_sol = bfrac_sol_1[1:52] + '0' * (52 - len(bfrac_sol_1[1:52]))
    bsgn_sol = '1' if frac_sol_1 < 0 else '0'
    exp_sol = max(exp1, exp2)
    for i in range(len(bfrac_sol_1) - 52):
        exp_sol += 1
    bexp_sol = '0' * (11 - len(bin(exp_sol)[2:])) + bin(exp_sol)[2:]
    return bsgn_sol + bexp_sol + bfrac_sol


# def float_add(a, b):
#     bsgn1 = a[0]
#     bsgn2 = b[0]
#     bexp1 = a[1:12]
#     bexp2 = b[1:12]
#     bfrac1 = a[12:]
#     bfrac2 = b[12:]
#     exp1 = int(bexp1, 2)
#     exp2 = int(bexp2, 2)
#     bfrac1_1 = '1' + bfrac1[:-1]
#     bfrac2_1 = '1' + bfrac2[:-1]
#     if exp1 > exp2:
#         shift = exp1 - exp2
#         bfrac2_1_shifted = ('0' * shift + bfrac2_1)[:52]
#         frac1_1 = -int(bfrac1_1, 2) if int(bsgn1) else int(bfrac1_1, 2)
#         frac2_1_shifted = -int(bfrac2_1_shifted, 2) if int(bsgn2) else int(bfrac2_1_shifted, 2)
#         frac_sol_1 = frac1_1 + frac2_1_shifted
#         bfrac_sol_1 = bin(abs(frac_sol_1))[2:52]
#     elif exp2 > exp1:
#         shift = exp2 - exp1
#         bfrac1_1_shifted = ('0' * shift + bfrac1_1)[:52]
#         frac1_1_shifted = -int(bfrac1_1_shifted, 2) if int(bsgn1) else int(bfrac1_1_shifted, 2)
#         frac2_1 = -int(bfrac2_1, 2) if int(bsgn2) else int(bfrac2_1, 2)
#         frac_sol_1 = frac1_1_shifted + frac2_1
#         bfrac_sol_1 = bin(abs(frac_sol_1))[2:52]
#     else:
#         frac1_1 = -int(bfrac1_1, 2) if int(bsgn1) else int(bfrac1_1, 2)
#         frac2_1 = -int(bfrac2_1, 2) if int(bsgn2) else int(bfrac2_1, 2)
#         frac_sol_1 = frac1_1 + frac2_1
#         bfrac_sol_1 = bin(abs(frac_sol_1))[2:52]
#     bfrac_sol = bfrac_sol_1[1:]+'0'*(52-len(bfrac_sol_1[1:]))
#     bsgn_sol = '1' if frac_sol_1 < 0 else '0'
#     bexp_sol = '0'*(11-len(bin(max(exp1, exp2))[2:]))+bin(max(exp1, exp2))[2:]
#     return bsgn_sol + bexp_sol + bfrac_sol

# a = "0100000000101000000000000000000000000000000000000000000000000000"
# b = "0011111111101000000000000000000000000000000000000000000000000000"
# print(float_add(b, a),"0100000000101001100000000000000000000000000000000000000000000000",sep='\n')
