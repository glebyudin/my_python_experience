name = 'Gleb'
print(name)

import random
some_words = ['apple', 'banana', 'orange', 'grape', 'pear', 'strawberry', 'watermelon', 'potato']
word = random.choice(some_words)
print(word)

print('Угадай слово! Подсказка: это фрукт или ягода')

chances = len(word)+2
letters_guessed = ['_']*len(word)

#print(letters_guessed)

for letter in letters_guessed:
    print(letter, end=' ')
print(' ')
while letters_guessed != list(word) and chances > 0:
    guess = input('Введите букву ')
    chances = chances-1

    if not guess.isalpha():
        print('ВВОДИТЬ МОЖНО ТОЛЬКО БУКВЫ!')
        continue
    elif len(guess) > 1:
        print('ВВОДИТЬ МОЖНО ТОЛЬКО ПО ОДНОЙ БУКВЕ!')
        continue
    elif guess in letters_guessed:
        print('Данную букву вы уже угадали!')
        continue
    if guess in word:
        print('БУКВА УГАДАНА')
        for index, letter in enumerate(word):
            if letter == guess:
                letters_guessed[index] = letter

        for letter in letters_guessed:
            print(letter, end=' ')

    else:
        print('БУКВА НЕ УГАДАНА!!!')
    print('Осталось', chances, 'попыток')
if chances == 0 and letters_guessed != list(word):
    print('Попытки закончились! Вы проиграли!')
else:
    print('ВЫ ПОБЕДИЛИ!!!')