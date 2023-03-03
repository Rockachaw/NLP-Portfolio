# NLP-Portfolio
Portfolio of my classwork for my Natural Language Processing course at UTD

## Overview of NLP

In [this document](Overview_of_NLP.TXT), I go over the basics of NLP and reflect on my personal interest in it

## Assignment 1: Text Processing with Python

[This program](Assignment1.py) uses python to process a text file filled with person data to fix inconsistencies and bad formatting.
To run this program, run the script with sys.argv set to the filepath of your input data (ex: `data/data.csv`)

[Example data file](data/data.csv)

In my opinion, python is a pretty strong language for text processing. Strings are indexed in a straightforward way, allowing for easy editing. From this assignment, I do not see any weaknesses of Python for text processing. I'd imagine its slower than other languages when given large amounts of text, but for this usecase it seems great.

This assignment served as a great reintroduction to Python since it has been about 7 years since I used it. It also helped me to review regex, which I have not used extensively before.

## Assignment 2: Word Guessing Game

[This program](Assignment2.py) uses python and the natural language toolkit to preprocess input text by tokenizing, removing stopwords, lemmatizing, and extracting nouns. These nouns are then used as the word bank in a word guessing game.
To run this program, run the script with sys.argv set to the filepath of your input data (ex: `data/anat19.txt`)

[Example data file](data/anat19.txt)

## Assignment 3: WordNet

[This notebook](Assignment3.ipynb) explores uses of the WordNet database in the field of Natural Language Processing.

## Assignment 4: N-grams

In this assignment, I learned how to use n-grams to predict which language a given sentence is in. The first step is to use the [bigram generator](Assignment4/bigram_generator) to create dictionaries of all the unigrams and bigrams. Next, run the [probability generator](Assignment4/probability_generator) to find the most likely language of origin for an lines of an example file based on those dictionaries. In [this narrative](Assignment4/Ngrams Narrative.pdf) I explore the purpose of n-grams and how they are used in the field of Natural Language Processing.


