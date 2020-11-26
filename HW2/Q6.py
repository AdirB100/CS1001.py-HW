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
