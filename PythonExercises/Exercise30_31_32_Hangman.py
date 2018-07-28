# Part 1
#
# Exercise 30 - Pick Word
# This exercise is Part 1 of 3 of the Hangman exercise series.
#
# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary.
# Download this file and save it in the same directory as your Python code. This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.
#
# Hint: use the Python random library for picking a random word.

import random

with open('Hangman_Exercise_Word_List.txt', 'r') as f:
  word_list = [s.replace('\n', '') for s in f.readlines()]

#word_list = open('Hangman_Exercise_Word_List.txt','r').read().split('\n')

#print(word_list[0:4])

#print(len(word_list))

def pick_a_word(list):

    length = len(list)
    chosen_word = list[random.randint(0,length)]
    #print(chosen_word)
    return chosen_word

word_to_guess = pick_a_word(word_list)


# Part 2
#
# Exercise 31 - Guess Letters
#
# This exercise is Part 2 of 3 of the Hangman exercise series.
#
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed.
# (In the actual game, the player can only guess 6 letters incorrectly before losing).

HANGMANPICS = ['    +---+\n    |   |\n        |\n        |\n        |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n        |\n        |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n    |   |\n        |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n   /|   |\n        |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n   /|\  |\n        |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n   /|\  |\n   /    |\n        |\n  =========',
               '    +---+\n    |   |\n    O   |\n   /|\  |\n   / \  |\n        |\n  =========']

list_word_to_guess = list(word_to_guess)
length = len(word_to_guess)
guessing = ["_"] * length

print(' '.join(guessing))
#print(list_word_to_guess)
print(HANGMANPICS[0])

not_guessed = True
used_letters = []
incorrect_letters = 0

while not_guessed and incorrect_letters < 6:
    letter = input("Guess a letter: ").upper()
    #print(letter)
    if letter in used_letters:
        print("You have already used this letter. Choose another letter.")
        continue
    else:
        used_letters.append(letter)

    correct = False

    for l in range(length):
        #print(list_word_to_guess[l])
        if list_word_to_guess[l] == letter:
            correct = True
            guessing[l] = letter
            #print(guessing[l])
            #print(l)

    print(' '.join(guessing))

    if correct == False:
        incorrect_letters += 1
        print("You were wrong {} time(s).".format(incorrect_letters))

    print(HANGMANPICS[incorrect_letters])

    if '_' not in guessing:
        not_guessed = False

if not_guessed == False:
    print("Great! You have guessed it!")
else:
    print("Sorry... You have lost.")
    print("The correct word was:" + word_to_guess)



