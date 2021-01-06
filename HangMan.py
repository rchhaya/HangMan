#Hangman game that uses random word
import random

def display_noose():
    """Displays the correct noose"""
    for i in range(0,8):
        print(noose.readline().rstrip())
    print('\n')

def correct_guess(guess, string_display):
    """Procedure if guess is correct"""
    print("The word contains the letter '" + guess + "'!")
    for index in range(len(word_used)):
        if word_used[index] == guess:
            string_display = string_display[:index] + guess + string_display[index+1:]
    return(string_display)

def incorrect_guess(guess, wrong_count, limit, name):
    """Procedure if guess is incorrect"""
    if wrong_count < limit: print("The letter '" + guess + "' is not in the word! Note that you can still make " + str(8-wrong_count) + " wrong guesses before " + name + " is hung.")
    else: print("The letter '" + guess + "' is not in the word! Note that you can still make 1 wrong guess before  " + name + " is hung.")
    display_noose()

flag = True
#Game loop
while flag: 
    #initialize variables
    word_used = ''
    string_display = ''
    letters_guessed = []
    wrong_count = 0
    limit = 7
    name = ''

    #Picking a word
    with open('files\\Hangman_Dictionary.txt') as words:
        word_list = words.readlines()
    word_used = word_list[random.randint(0,999)].strip()

    #setting up the blanks
    for i in range(len(word_used)):
        string_display+= '-'
    
    #Starting the noose
    noose = open('files\\hangman.txt')
    display_noose()
    #Getting a name
    while True:
            name = input("Enter your name please: ")          
            if (name.isalpha() and len(str(name)) >= 1):
                name = str(name.title())
                break
            else:
                print("Invalid input type. Please try again. ") 
    print("Welcome to hangman, " + name + "! The word to guess is " + str(len(word_used)) + " letters long. Good luck!")
    print("You have " + str(limit) + " wrong guesses that you can make before the stick figure (named " + name + ") is hung")

    #Guessing aspect of the game
    while '-' in string_display and wrong_count  < 8:
        while True:
            guess = input("Enter a lowercase letter to check if it is in the word: ")
            guess = str(guess.lower())
            if (guess.isalpha() and len(guess) == 1):
                break
            else:
                print("Invalid input type. Please try again. ") 
        
        if guess in letters_guessed:
            print("You already guessed that letter...")
        elif guess in word_used:
            string_display = correct_guess(guess, string_display)
            letters_guessed.append(guess)
        else:
            wrong_count+=1
            incorrect_guess(guess, wrong_count, limit, name)
            letters_guessed.append(guess)
        print(string_display + '\n')
        

    noose.close()
    words.close()

    if (wrong_count < 8):
        print("You guessed the word! It was '" + word_used + "'!")
    else:
        print("You lost! " + name + " was hung:(\nThe word was '" + word_used + "'!")
    
    #Asking if user wants to play again
    while True:
        play_again = input("Would you like to play again? Enter 'Y' for yes and 'N' for no: ")
        if str(play_again).lower() == 'y' or str(play_again).lower() == 'n':
            break
        else: 
            print("Invalid input.")

    if str(play_again).lower() == 'n': 
        flag = False
        print("Thanks for playing!")

