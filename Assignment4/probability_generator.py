# Houston Holman (hdh200000)
# 3/2/23
# Assignment 4: Ngrams

import pickle

from nltk.tokenize import word_tokenize
from nltk.util import ngrams


def compute_prob(text, unigram_dict, bigram_dict, V):
    """ Returns the probability that a line of text came from the supplied language
    Args:
        text (string): line of text to test
        unigram_dict (dictionary): contains counts of each unigram in language
        bigram_dict (dictionary): contains counts of each bigram in language
        V (int): total size of the vocabulary
    Returns:
        probability that text came from language
    """
    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))

    p_laplace = 1

    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0

        p_laplace = p_laplace * ((n + 1) / (d + V))

    return p_laplace


if __name__ == '__main__':
    """Tests each line of the input file against the pickled unigram and bigram dictionaries.
       Outputs the best guess of the language to an output file. Then it checks the output 
       file against the given solution file to see how accurate it was.
    """
    english_unigrams = pickle.load(open('english_unigrams.p', 'rb'))
    english_bigrams = pickle.load(open('english_bigrams.p', 'rb'))
    french_unigrams = pickle.load(open('french_unigrams.p', 'rb'))
    french_bigrams = pickle.load(open('french_bigrams.p', 'rb'))
    italian_unigrams = pickle.load(open('italian_unigrams.p', 'rb'))
    italian_bigrams = pickle.load(open('italian_bigrams.p', 'rb'))

    unigram_count = len(english_unigrams) + len(french_unigrams) + len(italian_unigrams)

    test = open('LangId.test', 'r')
    test_lines = test.readlines()

    count = 0

    with open("wordLangId.out", 'w') as file:
        pass
    for line in test_lines:
        count += 1
        english_chance = compute_prob(line, english_unigrams, english_bigrams, unigram_count)
        french_chance = compute_prob(line, french_unigrams, french_bigrams, unigram_count)
        italian_chance = compute_prob(line, italian_unigrams, italian_bigrams, unigram_count)

        answer = str(count) + " "

        if english_chance > french_chance and english_chance > italian_chance:
            answer += "English"
        elif french_chance > english_chance and french_chance > italian_chance:
            answer += "French"
        else:
            answer += "Italian"

        with open('wordLangId.out', 'a') as file:
            file.write(answer+'\n')

    output_file = open('wordLangId.out', 'r')
    solution_file = open('LangId.sol', 'r')

    output_list = output_file.read().split('\n')
    solution_list = solution_file.read().split('\n')

    correct_count = 0
    incorrect_line_numbers = []
    for i in range(len(solution_list)):
        if output_list[i] == solution_list[i]:
            correct_count += 1
        else:
            incorrect_line_numbers.append(i)

    print("Percentage of correctly classified lines: " + str((correct_count/len(solution_list)) * 100))
    print("Incorrect line numbers: ")
    print(incorrect_line_numbers)

