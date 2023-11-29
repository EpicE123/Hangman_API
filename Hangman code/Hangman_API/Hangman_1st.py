import random
import requests
import json
import string

# word -> hanged -> isWordGuessed -> getAvailable -> getWordGuessed -> hangman

# Function to pull a random word from a list of words using API

def word():

    '''
    # FIXME - Returns a random word from "https://wordsapiv1.p.rapidapi.com/words/".
              There should be three parameters for request.get function - url, headers, and params
              headers should have   {
                    'x-rapidapi-host': SERVER_URL_HERE
                    'x-rapidapi-key': YOUR_API_KEY_HERE
              } format
              params should have {"random: "true/false"}
    '''

    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random" : "true" }

    headers = {
      "X-RapidAPI-Key": "c6a7192fc9msh4931c462d8c53c4p1ced90jsn45cd3d660151",
	    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )
    word = json.loads(response.text)["word"]
    
    return word

# Game graphics
def hanged(man):
    graphic = [
    '''
       +------+
       |
       |
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |      |
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     /
       |
    ==============
    ''',
    '''
       +------+
       |      |
       |      O
       |     -|-
       |     / \\
       |
    ==============
    '''
    ]
    return graphic[man]


# -----------------------------------

def isWordGuessed(secretWord, lettersGuessed):
    '''
    # FIXME - Takes two parameters - secertWord and lettersGussed
              secretWord: string, the word the user is guessing
              lettersGuessed: list, what letters have been guessed so far
              Increase count variable if the letter in letterGuessed equals the
              letter in secretWord.

              returns: Boolean, True if the count equals the length of the secretWord;
                       False otherwise
    '''
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    # FIXME - Takes two parameters - secertWord and lettersGussed
              secretWord: string, the word the user is guessing
              lettersGuessed: list, what letters have been guessed so far

              If the lettersGuessed is in secretWord, append that letter to correctGuesses.

              returns: String, add underscore for if the letter in correctGuesses
                       is not in secretWord and add the correct letter in correctGuesses
                       if it is.

              example: Should return _ a _ _ _ s if letters 'a' and 's' were guessed
    '''

    correctGuesses = []
    outputString = ''

    for letter in secretWord:
        for i in lettersGuessed:
            if i in letter:
                correctGuesses.append(i)
                outputString = outputString + i
                break
        if not i in letter:       
            outputString = outputString + "_ "
                
    # Add code here
    return outputString



def getAvailableLetters(lettersGuessed):
    '''
    # FIXME - lettersGuessed: list, what letters have been guessed so far
              Returns: string, comprised of letters that represents what letters have not
                yet been guessed.
    '''
    new_alphabet = []

    alphabet=list(string.ascii_lowercase)
    # Add code here
    for i in alphabet:
        if i not in lettersGuessed:
            new_alphabet.append(i)

    return new_alphabet

def hangman(secretWord):
  
    #FIXME - Takes one parameter - secretWord: string, the secret word to guess.

    '''Starts up an interactive game of Hangman.

    (1) At the start of the game, let the user know how many
      letters the secretWord contains.

    (2) Ask the user to supply one guess (i.e. letter) per round.

    (3) The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    (4) After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.'''
    

    print("Welcome to the game, Hangman!")
    print(len(secretWord))
    print("_ " * len(secretWord))

    

    # FIXME - Write your print statement according to the explanation (1)

    global lettersGuessed
    mistakeMade=0
    lettersGuessed=[]

    while 6 - mistakeMade > 0:

        # FIXME - Create an if statement to check if the player has won the game.
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            print("-------------")
            break
        
        else:
            print("-------------")
            print("You have", 6-mistakeMade, "guesses left.")
            print(getAvailableLetters(lettersGuessed))
            # FIXME - Print a statement to show the available letters.
            print(hanged(mistakeMade))
            # FIXME - Get user input of a letter to guess. The guessed letter must be in lower case string.
            while True:
                guess = str(input("Input a letter to guess:  ")).lower()
            # FIXME - If the user input is more than one letter, tell them to guess again with only one letter.
                if not len(guess) == 1:
                    print ("your geuss must be only ONE letter")
                if guess in lettersGuessed:
                    print ("you have already guessed that")
                else:
                    break
                
            
            # FIXME - Create an if statement to check if the player already guessed a letter.
            
              # FIXME - Create a print statement to tell the player that they have already guessed that letter.


            # FIXME - Create an elif statement to check if the guessedletter is in the word and has not been guessed before.
            lettersGuessed.append(guess)
            print(lettersGuessed)
            
              # FIXME - Append that letter to the lettersGuessed list.
              # FIXME - Create a print statement to tell the player that it was a good guess, including the guessed word.
            if not guess in secretWord:
                mistakeMade += 1
                print("your guess is incorrect" , getGuessedWord(secretWord, lettersGuessed))

            else:
                print("your guess is correct" , getGuessedWord(secretWord, lettersGuessed))
            
                # FIXME - Append to letter to the lettersGuessed list.
                # FIXME - Increment mistakeMade by 1.
                # FIXME - Create a print statement to tell the player that the guessed word is not in the word, including the guessed word.

    if mistakeMade == 6:
        print("-------------")
        print(hanged(6))
        print("Sorry, you ran out of guesses. The word was:",secretWord)

    return
# FIXME - Assign a random word to the secretWord variable.

secretWord = word()

hangman(secretWord)