import string

from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

name = ""	#address of the dataset
file = open(name, "r")

dict_spam = {}
dict_ham = {}
dict_all = {}
corpus = ""

for i in range(0, 5575):
    line_o = file.readline()
    line = line_o[1:4]
    line_o = line_o.lower()
    for c in string.punctuation:
        line_o = line_o.replace(c, "")
    message = ""
    token_ham = []
    token_spam = []
    token = []

    if(line == "ham"):
        message = line_o[3:]
        corpus = corpus + " " + message
        token_ham = word_tokenize(message)
	stop_words = set(stopwords.words('english'))
        filtered_sentence = []
        for w in token_ham:
            if w not in stop_words:
                filtered_sentence.append(w)
        print(token_ham)
        print(filtered_ham_sentence)
        for j in range(len(filtered_ham_sentence)):
            dict_ham[filtered_ham_sentence[j]] = filtered_ham_sentence.count(filtered_ham_sentence[j])
    if(line == "spa"):
        message = line_o[4:]
        corpus = corpus + " " + message
        token_spam = word_tokenize(message)
	stop_words = set(stopwords.words('english'))
        filtered_sentence = []
        for w in token_spam:
            if w not in stop_words:
                filtered_sentence.append(w)
        print(token_spam)
        print(filtered_spam_sentence)
        for j in range(len(filtered_spam_sentence)):
            dict_spam[filtered_spam_sentence[j]] = filtered_spam_sentence.count(filtered_spam_sentence[j])
    token = word_tokenize(message)
    for j in range(len(token)):
        dict_all[token[j]] = token.count(token[j])
    t = len(token)
