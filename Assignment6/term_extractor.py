import os
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist


def extract_terms():
    all_text = ""

    # get all text in a single string
    for filename in os.listdir(os.getcwd() + '\\cleaned_pages'):
        with open(os.path.join(os.getcwd() + '\\cleaned_pages', filename), 'r') as page:
            text = page.read()
        all_text += text

    # extract all tokens, removing stopwords and punctuation
    all_tokens = word_tokenize(all_text)
    all_tokens = [token.lower() for token in all_tokens if token not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    all_tokens = [token for token in all_tokens if token not in stop_words]

    # get the 40 most common tokens
    freq_dist = FreqDist(all_tokens)
    most_common = freq_dist.most_common(40)

    for token, count in most_common:
        print(token, count)


if __name__ == '__main__':
    extract_terms()
    print('Term extractor finished.')
