#I used the lib getpass to define the secret word.an
# For exemple: You're playing with a friend and you have to set the word that your friend has to guess
# Getpass was used to hide the word while typing
# when you're typing the program don't show any asterisk, but the word will be saved on the secret_word variable

# for this week as creativity I uploaded this program on the github, with the link below:
#https://github.com/limaofelipe/word_puzzle
import getpass


secret_word = getpass.getpass('define here a word that you want you friend guess: ')


guess_word = '_' * len(secret_word)
print('Guess the word: ' + guess_word)

guess_count = 0
hint = ''

while guess_word != secret_word:
    guess = input('Enter your guess: ')
    if len(guess) != len(secret_word):
        print('Your guess must have', len(secret_word), 'letters')
        continue

    guess_count += 1

    
    hint = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += '_'

    
    print('Hint:', hint)

    
    guess_word = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            guess_word += guess[i]
        else:
            guess_word += '_'

    
    print('Guess the word:', guess_word)

print('Congratulations! You guessed the word in', guess_count, 'guesses.')