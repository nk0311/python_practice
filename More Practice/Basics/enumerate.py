index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1


word = 'soccer'

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')