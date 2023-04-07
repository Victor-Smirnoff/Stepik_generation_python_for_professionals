word = input()
vowels = 'ауоыиэяюёе'
word_index = [i for i, ltr in enumerate(word) if ltr in vowels]
for _ in range(int(input())):
    s = input()
    word_index_s = [i for i, ltr in enumerate(s) if ltr in vowels]
    if word_index_s == word_index:
        print(s)
