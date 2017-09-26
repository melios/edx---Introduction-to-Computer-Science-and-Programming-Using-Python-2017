# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = ''
    #for each letter in secret word:
    for letter in secretWord:
        #if the letter in letterGuessed concantante the letter in the word string
        if letter in lettersGuessed:
            word += letter
        #otherwise concantante '_ '
        else:
            word += '_ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    #create a list with the alphaber
    alphabet = list(string.ascii_lowercase)
    #for any letter in lettersGuessed
    for letter in lettersGuessed:
        #remove that letter from alphabet
        if letter in alphabet:
            alphabet.remove(letter)
    return ''.join(alphabet)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    #variable to count the quesses/ count the mistakes
    mistakesMade = 8
    #declare lettersGuessed
    lettersGuessed = []

    # Greeding
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is %d letters long.' %len(secretWord))
    print('-------------')
    #print the secret word for testing
    print('the secret word is {0}' .format(secretWord))

    while mistakesMade != 0:
        print('You have {0} guesses left.' .format(mistakesMade))
        print('Available letters: {0}' .format(getAvailableLetters(lettersGuessed)))
        userletter = input('Please guess a letter: ')

        if userletter in lettersGuessed:
            print("Oops! You've already guessed that letter: {0}" .format(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------')
        elif userletter in secretWord :
            lettersGuessed.append(userletter)
            print('Good guess: {0} ' .format(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------')
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                mistakesMade = 0
        else:
             print('Oops! That letter is not in my word: {0}' .format(getGuessedWord(secretWord, lettersGuessed)))
             print('-----------')
             lettersGuessed.append(userletter)
             mistakesMade -= 1
             if mistakesMade == 0:
                 print('Sorry, you ran out of guesses. The word was {0}' .format(secretWord))



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
