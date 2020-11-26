#Skeleton file for HW1 - Winter 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include the ID number of the student submitting the solution (hw1_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#The first ID should be the ID of the student submitting the solution
#For example: SUBMISSION_IDS = ["123456000", "987654000"]

#Question 4a
def max_word_len(text):
    if text == '':
        return 0
    list_words = text.split()
    return max([len(word) for word in list_words])

#Question 4b
def frequent_word(text):
    if text == '':
        return ''
    list_words = text.split()
    frequency_list = []
    for word in list_words:
        if len(frequency_list) == 0:
            frequency_list.append((word, list_words.count(word)))
        else:
            if word not in [tupple[0] for tupple in frequency_list]:
                frequency_list.append((word, list_words.count(word)))
    times_frequent_word = max([tupple[1] for tupple in frequency_list])
    for tupple in frequency_list:
        if tupple[1] == times_frequent_word:
            return tupple[0]

#Question 4c
def vc_ratio(text):
    text = text.replace(' ', '')
    cnt_vowels = 0
    for vowel in ('a', 'e', 'i', 'o', 'u'):
        cnt_vowels += text.count(vowel)
    cnt_consonants = len(text) - cnt_vowels
    return cnt_vowels / cnt_consonants

#Question 5
def calc(expression):
    lst_expr = expression.split()
    if len(lst_expr) == 1:
        return int(expression)
    while True:
        if lst_expr[1] == '+':
            value = int(lst_expr[0]) + int(lst_expr[2])
        elif lst_expr[1] == '-':
            value = int(lst_expr[0]) - int(lst_expr[2])
        elif lst_expr[1] == '*':
            value = int(lst_expr[0]) * int(lst_expr[2])
        elif lst_expr[1] == '**':
            value = int(lst_expr[0]) ** int(lst_expr[2])
        else:
            value = int(lst_expr[0]) // int(lst_expr[2])
        if len(lst_expr) == 3:
            return value
        else:
            lst_expr[2] = value
            lst_expr = lst_expr[2:]


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


########
# Tester
########

def test():
    #testing Q4
    st = "the quick brown fox jumps over the lazy dog"
    if max_word_len(st) != 5:
        print("Error in max_word_len")
    if frequent_word(st) != "the":
        print("Error in frequent_word")
    if vc_ratio(st) != 11/24:
        print("Error in vc_ratio")

    #testing Q5
    if calc("2 ** 2 ** 2 ** 2") != 256:
        print("Error in calc")
    if calc("20 // 3") != 6:
        print("Error in calc")

    #testing Q6
    l = max_div_seq(23300247524689, 2)
    if l != 4:
        print("Error in max_div_seq")

    if not SUBMISSION_IDS:
        print("The list of IDs is empty")

    if not type(SUBMISSION_IDS) == list:
        print("The list of IDs is not a list type")

    if SUBMISSION_IDS and not all(type(x)==str for x in SUBMISSION_IDS):
        print("The list of IDs contains elments that are not strings")


