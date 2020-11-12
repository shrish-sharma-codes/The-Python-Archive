word = 'father'
attempts = len(word)
remaining_word = len(word) * '*'
prev_guess = ''
print(f'word is {remaining_word} its length is {len(remaining_word)}')
while remaining_word != word and attempts != 0:
print(f'You have {attempts} attempts left ')
ch = input('enter a character(lowercase): ')
if ch in word:
for i in range(len(word)):
if ch == word[i]:
remaining_word = remaining_word[:i] + ch + remaining_word[i + 1:]
print(f'correct...\nword is {remaining_word}')
else:
prev_guess += ch
print(f'previous guess: {prev_guess}\ntry again...\nword is {remaining_word}')
attempts -= 1
[print('Congratulations! you got the word') if remaining_word == word else print(f'Better luck next
time :( \nthe word was {word}')]
