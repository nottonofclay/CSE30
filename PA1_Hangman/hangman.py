'''
assignment: programming assignment 1
author: Clayton Lau
date: (write the date you finished working on the program)
file: hangman.py is a program that has the user play the game hangman
input: # of lives, # of letters in word
output: user guesses a letter which either fills a blank space(s) or loses a life, if all spaces are filled they win
'''

from asyncio.base_futures import _FINISHED
from random import choice, random
import os
import random
from re import A
os.chdir("C:/Users/tonof/OneDrive/Documents/Code/CSE30/PA1_Hangman")

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (dictionary_file):
    dictionary = {}
    max_size = 12
    readable_dictionary_file = open(dictionary_file, 'r')
    while True:
        line = readable_dictionary_file.readline().strip()                                              # gets another line from the dictionary file
        if len(line) == 0:                                                                              # stop when another word doesn't exist
            break
        try:
            if len(line) >= max_size:                                                                   # gets line length, sets to 12 if its > 12
                line_len = max_size
            else:
                line_len = len(line)
            dictionary[line_len].append(line)                                                           # adds value to dict list
        except:
            dictionary[line_len] = [line]                                                               # creates list with len of line as key
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    size = random.randint(3,12)
    lives = 5
    try:
        size = int(input('Please choose a size of a word to be guessed [3 – 12, default any size]:\n'))   # gets user input for word size
        if (size > 2 and size < 12):
            print('The word size is set to {word_size}\n'.format(word_size = size))
        else:
            raise Exception
    except:
        print('A dictionary word of any size will be chosen.\n')
    try:
        lives = int(input('Please choose a number of lives [1 – 10, default 5]:\n'))
        print('You have {lives_amt} lives\n'.format(lives_amt = lives))
    except:
        print('You have 5 lives\n')
    return (size, lives)



# MAIN

if __name__ == '__main__' :
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    game_running = True

    # print a game introduction
    print('Welcome to the Hangman Game!\n')
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while game_running:
        game_options = get_game_options()                                                               # set size of word and lives
        word = random.choice(dictionary[game_options[0]]).upper()                                               # select a word from a dictionary
        lives = game_options[1]
        lives_left = lives
        if ('-' in word):
            correct_letters = ['-']
        else:
            correct_letters = []
        guessed_letters = []
        # print(word)


        # START GAME LOOP   (INNER PROGRAM LOOP)

        while lives_left > -1:
            print('Letters Chosen: ', end='')
            print(', '.join(guessed_letters) + '\n')
            for j in range(len(word)):
                if word[j] in guessed_letters:
                    print(word[j] + " ", end='')
                elif (word[j] == '-'):
                    print('- ', end='')
                else:
                    print('__ ', end='')
            print('   lives: ' + str(lives_left) + ' ', end='')
            for k in range(lives):
                if (lives - k - lives_left > 0):
                    print('X', end='')
                else:
                    print('O', end='')
            if (''.join((sorted(set(word)))) == ''.join(sorted(correct_letters))):
                print('\nCongratulations!!! You won! The word is ' + word + '!')
                break
            if (lives_left > 0):
                while True:
                    user_input = input('\nPlease choose a new letter >\n').upper()
                    if (user_input == "" or len(user_input) > 1 or user_input.isdigit()):
                        print('Invalid input!')
                    elif (user_input in guessed_letters):
                        print('\nYou have already chosen this letter.')
                    elif(user_input in word):
                        guessed_letters.append(user_input)
                        correct_letters.append(user_input)
                        break
                    else:
                        print
                        guessed_letters.append(user_input)
                        lives_left -= 1
                        break
            else:
                print('\n\nYou lost! The word is ' + word.upper() + '!\n')
                lives_left -= 1

        if (input('Would you like to play again [Y/N]?\n').upper() == 'Y'):
            pass
        else:
            print('\nGoodbye!')
            break