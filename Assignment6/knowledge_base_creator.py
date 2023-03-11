import os
import nltk
import pickle

from collections import defaultdict


def create_knowledge_base():
    best_words = ['ulbricht', 'silk', 'dpr', 'bitcoin', 'drug', 'fbi', 'tor', 'market', 'computer', 'court']
    knowledge_dict = defaultdict(list)

    # for each word, store every sentence that contains that word in the dictionary
    for word in best_words:
        for filename in os.listdir(os.getcwd() + '\\cleaned_pages'):
            with open(os.path.join(os.getcwd() + '\\cleaned_pages', filename), 'r') as page:
                text = page.read()
            for sentence in nltk.sent_tokenize(text):
                if word in nltk.word_tokenize(sentence.lower()):
                    knowledge_dict[word].append(sentence)

    # print the dictionary
    for key in knowledge_dict:
        print(key + ':')
        for sentence in knowledge_dict[key]:
            print('\t' + sentence)

    # pickle the dictionary
    pickle.dump(knowledge_dict, open('knowledge_dict.p', 'wb'))


if __name__ == '__main__':
    create_knowledge_base()
    print('Knowledge base created.')

