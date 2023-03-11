import os
import shutil
import re

from nltk import sent_tokenize


def clean_files():
    # create cleaned_pages directory
    cleaned_pages_dir = os.getcwd() + '\\cleaned_pages'
    if os.path.exists(cleaned_pages_dir):
        shutil.rmtree(cleaned_pages_dir)
    os.makedirs(cleaned_pages_dir)

    for filename in os.listdir(os.getcwd() + '\\pages'):
        with open(os.path.join(os.getcwd() + '\\pages', filename), 'r') as page:
            text = page.read()

        # remove all tabs and newlines
        new_text = re.sub('\s+', ' ', text)

        # extract sentences
        sentences = sent_tokenize(new_text)

        # write sentences to new file
        with open(os.path.join(cleaned_pages_dir, filename), 'w') as clean_page:
            for sentence in sentences:
                clean_page.write(sentence + '\n')

        print("Cleaned " + filename)


if __name__ == '__main__':
    clean_files()
    print('File cleaner finished.')