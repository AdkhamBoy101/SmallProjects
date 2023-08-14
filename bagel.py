import random
DIGITS  = 2 
MAX_GUESSES = 10

def main():
    print('''Bagels, adeductive logic game.
          I am thinking of a {}-digit number with no repeated digits. Try to guess what it is. Here are some clues: 
          When I say:    That means: 
          Pico           One digit is correct but in the wrong position. 
          Fermi          One digit is correct and in the right position. 
          Bagels         No digit is correct. 
          
          For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it .'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of gueses.")
                print("The answer was {}.".format(secretNum))
            
            print("Do you want to play agay? (yes or no)")
            if not input('> ').lower().stertwith('y'):
                break
        print("Thanks for playing!")


def getSecretNum():
    numbers = list('0123456789')
    random.shufle(numbers)

    # Get the firs DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(DIGITS):
        secretNum += str(numbers[i])
        return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return "You Got it!"
    
    clues = []

    for i in range(len(guess)):
        if  guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ''.join(clues)