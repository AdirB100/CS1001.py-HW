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