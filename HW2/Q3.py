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
