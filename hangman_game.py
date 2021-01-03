"""
Project: Hangman game
Author: Siham Elmali
Date: December 23rd, 2020
Status: working on improvements whenever I have a chance
"""
import random
import string
from PyDictionary import PyDictionary


# helper functions
def load_words(file):
	"""
    :param file: input file with bunch of words
    :return: a list of words
    """
	with open(file, "r") as f:
		print("Loading word list from file...")
		words_list = f.read().split()
		print(f"{len(words_list)} words loaded.")
		return words_list


def choose_word(words_list):
	"""
    :param words_list: a list of words
    :return: a random word from the list
    """
	chosen_word = random.choice(words_list)
	return chosen_word


def is_word_guessed(secret_word, letters_guessed_list):
	"""
    :param letters_guessed_list: a list of letters
    :param secret_word: a string
    :return: True if the word is guessed and False if it's not
    """
	answer = ''
	for letter in secret_word:
		if letter in letters_guessed_list:
			answer += letter
	if answer == secret_word:
		return True
	else:
		return False


def get_guessed_word(secret_word, letters_guessed_list):
	"""
    :param letters_guessed_list: a list of letters
    :param secret_word: a string
    :return:  a string that is comprised of letters and underscores, based
    on what letters in letters_guessed_list are in ​secret_word.
    """
	output_str = []
	for index, letter in enumerate(secret_word):
		if letter in letters_guessed_list:
			output_str.append(letter)
		else:
			output_str.append('-')
	return ''.join(char for char in output_str)


def get_available_letters(letters_guessed_list):
	"""
    :param letters_guessed_list: a list of letters
    :return: string of letters that are not yet guessed by the user
    """
	english_alphabet = string.ascii_lowercase

	letters_not_guessed = ''.join([char for char in english_alphabet if char not in letters_guessed_list])
	return letters_not_guessed


def play_hangman(file):
	# load the word file
	words = load_words(file)

	# choose a word from the list randomly
	chosen_word = choose_word(words)

	# set remaining guesses as the length of the word picked
	guesses_remaining = len(chosen_word)

	# initialize an empty list
	letters_guessed = []

	# print game welcome
	# print("Welcome to the game of Hangman!")
	print(f'I am thinking of a word  that is {len(chosen_word)} letters long')

	while True:

		# get user input
		user_input = input("Please guess a letter: ")

		# append user input to the letters guessed list
		letters_guessed.append(user_input)

		if user_input in chosen_word:
			print(f'Good guess {get_guessed_word(chosen_word, letters_guessed)}')
			print(f"Available Letters: {get_available_letters(letters_guessed)}")
			print("-----------------------------------------------------------")
		else:
			print(f'Oops! That letter is not in my word {get_guessed_word(chosen_word, letters_guessed)}')
			print("-----------------------------------------------------------")
			guesses_remaining -= 1
			print(f'You have {guesses_remaining} guesses left')
			print(f"Available Letters: {get_available_letters(letters_guessed)}")

		if guesses_remaining == 0:
			print("GAME OVER! YOU LOST")
			print("The secret word is: ", chosen_word)
			print(chosen_word + ": ", define_word(chosen_word))
			break

		if is_word_guessed(chosen_word, letters_guessed):
			print("Congratulations, you won!")
			print(chosen_word + ": ", define_word(chosen_word))
			print(f"Your total score is: {guesses_remaining * len(set(chosen_word))}")
			break


def define_word(secret_word):

	def_dict = PyDictionary.meaning(secret_word)
	return def_dict


if __name__ == '__main__':

	print(''' 
		 _                                             
	    | |                                            
	    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
	    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
	    | | | | (_| | | | | (_| | | | | | | (_| | | | |
	    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
	                        __/ |                      
	                       |___/  
			___________.._______
			| .__________))______|
			| | / /      ||
			| |/ /       ||
			| | /        ||.-''.
			| |/         |/  _  \\
			| |          ||  `/,|
			| |          (\\\\`_.'
			| |         .-`--'.
			| |        /Y . . Y\\
			| |       // |   | \\\\
			| |      //  | . | \\\\
			| |     ')   |   |   (`
			| |          ||'||
			| |          || ||
			| |          || ||
			| |          || ||
			| |         / | | \\
			""""""""""|_`-' `-' |"""|
			|"|"""""""\ \       '"|"|
			| |        \ \        | |
			: :         \ \       : : 
			. .          `'       . .
''')

	# input file with words to use
	file_name = "words.txt"

	while True:
		play_hangman(file_name)
		user_ans = input("Do you want to play again? type yes or no: ")
		if user_ans.lower() == "no":
			break

# TODO: if the player wins and wants to play again, keep track of the total score
