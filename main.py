# Hangman game
#

# -----------------------------------
# Starter code


import random

WORDLIST_FILENAME = "words.txt"

#This function loadWords() reads the contents from the text file words.txt and lists the words. It also displays the number of words the it found on the text file. 
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

#this function chooseWord(wordlist) returns a random word from the text file to use it for the game.
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of starter code

#the line below Loads the list of words into the variable wordlist so that it can be accessed from anywhere in the program.
wordlist = loadWords()

#isWordGuessed function is used to check if the guessed letter is in the secretWord or not. 
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

      

# function is used to write the partially guessed word so far, as well as letters that the user has not yet guessed.
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    string = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            string = string + letter
          
        else:
            string = string + "_"
    return string

#This function is used to show the letters that are left to be guessed from the set of english alphabets. 
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    string = "abcdefghijklmnopqrstuvwxyz"
    tempStr = ""
    for letter in string:
        if letter not in lettersGuessed:
            tempStr = tempStr + letter
    return tempStr
    


    
#The function hangman is used to make the game interactive to the user letting the user know whatsoever has happened after each round.
def hangman(secretWord):
    
    print ("This is hangman, you want to play?")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 8
    
    while True:


        print ("Possible letters: " + getAvailableLetters(lettersGuessed))
        print()
        guess = input("Guess a letter: ")
        print()
        
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess!")
            print(' '.join(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in lettersGuessed:
            print ("You can't choose the same letter twice...")
            continue 
        else:
            lettersGuessed += guess
            print ("Oops! That's wrong.. Try again")
            
            print(' '.join(getGuessedWord(secretWord, lettersGuessed)))

            guessesLeft = guessesLeft - 1
        
        # The following conditions is to display when all the guesses are made and the right word can not be guessed by the user
        if guessesLeft <= 0:
            print ("Sorry, You didn't get there. :(")
            print(" The word was: " + secretWord)
            break

        #The following comment is to display when the the user guesses the word.    
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Well done! You've beat me!")
            break
          
        print ("You only have " + str(guessesLeft) + " chance(s) to guess the right letters")
        


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)