import random

word_bank = ['hello','world', 'random', 'words']

word = random.choice(word_bank)

guessesd_word = ['_'] * len(word)

attempts = 10

while attempts > 0: 
    
    print('\nCurrent word: ' + ' '.join(guessesd_word))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessesd_word[i] = guess    
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    
    if '_' not in guessesd_word:
        print('\nCongratulations!! You guessed the correct word: ' + word)
        break

else:
    print('\nYou\'ve run out of attempts! The word was: ' + word)