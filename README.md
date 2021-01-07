# HangMan
A simple hang-man game with random words

The game beign with prompting the user for a name (if the input is 0 characters or contains illegal characters, the user is re-prompted). A word is chosen at random from 'Hangman_
Dictionary.txt,' which is a list of the 1000 most common English words. The user is then notified of the word length, number of guesses left until the figure is drawn, and the name 
of the stick figure (name of the user). The actual hangman graphics comes from ASCII art in 'hangman.txt.' Each drawing has 1 more body part than the previous one. 

The user is then pormpted to enter a lowercase letter. If the input is a lowercase letter, then the program checks if the word has the letter. If the input is an uppercase letter,
the program turns the letter into a lowercase one. If the input is not a single letter (illegal characters, more than 1 character, 0 characters, etc.), the game re-prompts the user 
after notifying them of an illegal input.

If the word has the letter, the blank is replaced with the letter and the user is congratulated. If the word does not have the letter, the ASCII art of the stick figure is updated
and the user is notified that they have 1 less guess left. 

The game continues until all letters are guessed (user wins) or the stick figure is completely drawn and the user is out of wrong guesses (user loses, stick figure is hung). 
Afterwards, the user is prompted to play again. A 'y'/'Y' input will result in the game restarting with a new word and empty noose, a 'N'/'n' will result in the program closing, 
and any other input is invalid and the user will be informed and re-prompted.

NOTE: Do not change the .txt files without accounting for it in the code. The ASCII art and word selection will both be flawed for the game. 
