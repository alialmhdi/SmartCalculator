dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
user_input = input().split()
misspelling = []
for word in user_input:
    if word not in dictionary:
        misspelling.append(word)
if len(misspelling) != 0:
    for incorrect_word in misspelling:
        print(incorrect_word)
else:
    print("OK")
