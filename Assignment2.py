# Word Guessing Game
# Houston Holman
# 2/16/23

import sys
import pathlib
import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

stop_words = set(stopwords.words('english'))
wnl = WordNetLemmatizer()


def preprocess(text):
    """Calculates lexical diversity, tokenizes, and extracts nouns from input text
    Args:
        text (string): input text to be processed
    Returns:
        filtered_tokens (list): list of tokens from the input string
        nouns (list): list of nouns from the input string
    """
    tokens = word_tokenize(text.lower())

    print("Lexical Diversity: "+ str(round(len(set(tokens)) / len(tokens), 2)))

    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words and len(token) > 5]

    lemmas = [wnl.lemmatize(t) for t in filtered_tokens]

    unique_lemmas = set(lemmas)
    tags = nltk.pos_tag(unique_lemmas)
    for j in range(20):
        print(tags[j])

    nouns = []
    for tag in tags:
        if "NN" in tag:
            nouns.append(tag[0])

    print("Number of tokens: " + str(len(filtered_tokens)))
    print("Number of unique nouns: " + str(len(nouns)))
    return filtered_tokens, nouns


def read_file(filepath):
    """Converts a text file into a string object
    Args:
        filepath (string): relative path of text file
    Returns:
        string: contents of text file
    """
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text_in = f.read()
    return text_in


def guessing_game(bank):
    """Starts a game where the user attempts to guess a word
    Args:
        bank (list): list of strings to select word from
    """
    score = 5
    guess = ""
    word = bank[random.randint(0, 49)]
    revealed_word = "_" * len(word)
    guessed_letters = {}

    while guess != "!" and score >= 0:
        print_word = ""
        for letter in revealed_word:
            print_word += letter
            print_word += " "

        print(print_word)

        if revealed_word == word:
            print("You solved it!")
            print("Guess another word")
            guessing_game(bank)

        guess = input("Guess a letter: ")

        if guess in guessed_letters:
            print(guess + " was already guessed")

        elif guess in word:
            score = score + 1
            print("Right! Score is " + str(score))

            occurrences = []
            start = 0
            loc = word.find(guess, start)
            while loc != -1:
                occurrences.append(loc)
                start = loc + 1
                loc = word.find(guess, start)

            for occurrence in occurrences:
                revealed_word = revealed_word[:occurrence] + guess + revealed_word[occurrence+1:]

        else:
            score = score - 1
            print("Sorry, wrong letter. Score is " + str(score))

        guessed_letters[guess] = 1

    print("Sorry, you lost. The word is " + word)


if __name__ == '__main__':
    """Reads in a text file, preprocesses it, and then starts a word guessing game using
       only the top 50 most common nouns in the file

       sys.argv must contain the filepath to the text file with the input text
    """
    if len(sys.argv) < 2:
        sys.exit('ERROR: filepath must be entered as sysarg')
    else:
        fp = sys.argv[1]
    input_text = read_file(fp)

    processed_text = preprocess(input_text)

    counts = {t: processed_text[0].count(t) for t in processed_text[1]}
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    word_bank = []
    for i in range(50):
        print(sorted_counts[i])
        word_bank.append(sorted_counts[i][0])

    print("Let's play a word guessing game!")
    guessing_game(word_bank)



