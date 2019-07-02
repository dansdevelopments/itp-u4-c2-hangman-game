from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["Python","Snake","Noodle","Fox","Hound","Pencil","Acrobat","Beer","Wine","Hedgehog"]


def _get_random_word(list_of_words):
    return random.choice(LIST_OF_WORDS)


def _mask_word(word):
    return "*"*len(word)


def _uncover_word(answer_word, masked_word, character):
    if answer_word == "":
        raise InvalidWordException('The answer word is blank!')
    if masked_word == "":
        raise InvalidWordException('The guessed word is blank!')
    if character.lower() in masked_word.lower():
        return masked_word
    new_masked_word = ""
    counter = 0
    for char in answer_word:
        if char.upper() == character.upper() or masked_word[counter] != "*":
            new_masked_word += char
        else:
            new_masked_word += "*"
        counter += 1
    return new_masked_word


def guess_letter(game, letter):
    if letter.lower() not in "abcdefghijklmnopqrstuvwxyz":
        raise InvalidGuessedLetterException('{} is not a letter'.format(letter))
    game['masked_word'] = _uncover_word(game['answer_word'],game['masked_word'], letter)
    game['remaining_misses'] -= 1
    if game['masked_word'] == game['answer_word']:
        raise GameWonException('You Win!')
    if game['remaining_misses'] == 0:
        raise GameLostException('You lose!')
    return game


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
