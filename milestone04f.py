secret_word = 'table'
print('\nWelcome to the word guessing Game!')

print("\n Your hint is: ", end="")
for letter in secret_word:
    print('_ ', end="")
guess = input('\nWhat is your guess? ')
count = 0
while guess.lower() != secret_word:
    count += 1
    guess_length = len(guess)
    #Ensuring the length of word is the-same as the secret word
    if guess_length == len(secret_word):
        #check for the correct and wrong word and display with hint 
        print('hint: ', end="")
        for i in range(guess_length):
            letter = guess[i]
            
            if letter == secret_word[i]:
                print(letter.upper(), end=" ")
            
            elif letter in secret_word:
                print(letter.lower(), end=" ")
            
            else :
                print('_', end=" ")
            
        guess = input('\nWhat is your guess? ')

    else:
        print('Sorry, your word should be 5 letters')
        guess = input('\nWhat is your guess? ')
count += 1
print(f'Congratulations! you guessed it! \nIt took you {count} guesses\n')
