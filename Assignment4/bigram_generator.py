# Houston Holman (hdh200000)
# 3/2/23
# Assignment 4: Ngrams

import pickle
import io

from nltk.tokenize import word_tokenize
from nltk.util import ngrams


def get_unigrams_and_bigrams_from_file(filepath):
    """ Extracts all the unigrams and bigrams from an input file and
        places them in dictionaries that track their counts
    Args:
        filepath (string): relative path of text file
    Returns:
        dictionaries that contain the counts of each unigram and bigram
    """
    f = io.open(filepath, mode="r", encoding="utf-8")
    text = f.read()
    text = text.strip();
    print('Extracting bigrams from ' + filepath)
    unigrams = word_tokenize(text)
    bigrams = list(ngrams(unigrams, 2))

    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}
    return unigram_dict, bigram_dict


if __name__ == '__main__':
    """Takes each training file and calls get_unigrams_and_bigrams_from_file
       to get the unigram and bigram dictionaries for that file. The dictionaries
       are then pickled to be used in probability_generator.py
    """
    english_dicts = get_unigrams_and_bigrams_from_file('LangId.train.English')
    french_dicts = get_unigrams_and_bigrams_from_file('LangId.train.French')
    italian_dicts = get_unigrams_and_bigrams_from_file('LangId.train.Italian')

    print('Pickling dictionaries...')
    pickle.dump(english_dicts[0], open('english_unigrams.p', 'wb'))
    pickle.dump(english_dicts[1], open('english_bigrams.p', 'wb'))
    pickle.dump(french_dicts[0], open('french_unigrams.p', 'wb'))
    pickle.dump(french_dicts[1], open('french_bigrams.p', 'wb'))
    pickle.dump(italian_dicts[0], open('italian_unigrams.p', 'wb'))
    pickle.dump(italian_dicts[1], open('italian_bigrams.p', 'wb'))
    print('Done!')