word_list = ["apple", "banana", "cherry", "date", "grape", "kiwi"]

result_list = [''.join(w[::-1]) + w[-1].upper() if w[-1] not in 'aeiou' else w for word in word_list for w in word]
print(result_list)

