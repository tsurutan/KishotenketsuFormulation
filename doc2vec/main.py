# coding: utf-8
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
from gensim import models

FILE_SIZE = 7
FILE_BASE_NAME = "sample"
FILE_SUFFIX = ".txt"
KISHOTENKETSU = ["起", "承", "転", "結"]

results = {}
scores = {"起": 0, "承": 0, "転": 0, "結": 0}
sum_scores = {"起": 0, "承": 0, "転": 0, "結": 0}
frequent_scores = {"起": {"起": 0, "承": 0, "転": 0, "結": 0},
                   "承": {"起": 0, "承": 0, "転": 0, "結": 0},
                   "転": {"起": 0, "承": 0, "転": 0, "結": 0},
                   "結": {"起": 0, "承": 0, "転": 0, "結": 0}}

plt.style.use('ggplot')
font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)

def calculate(filename):
    sentence = {}
    sentences = []
    for index, txt in enumerate(open("input/" + filename, 'r')):
        sentence[index] = []
        sentence[index] = txt.split(" ")
        sentences.append(models.doc2vec.LabeledSentence(
            words=sentence[index], tags=[KISHOTENKETSU[index]]))

    model = models.Doc2Vec(alpha=.001, min_alpha=.00001, min_count=1)
    model.build_vocab(sentences)

    for epoch in range(50):
        model.train(sentences)
        model.alpha -= 0.001  # decrease the learning rate`
        model.min_alpha = model.alpha  # fix the learning rate, no decay

    model.save("my_model.doc2vec")
    model_loaded = models.Doc2Vec.load('my_model.doc2vec')

    f = open("output/" + filename, "w")
    for word in KISHOTENKETSU:
        results[filename + word] = model.docvecs.most_similar(word)
        count = 3
        for dict in results[filename + word]:
            sum_scores[word] += dict[1]
            frequent_scores[word][dict[0]] += count
            count -= 1
        f.write(str(model.docvecs.most_similar(word)) + "\n")
        print ("normal", model.docvecs.most_similar(word))
    f.close()


def calculate_all():
    for i in range(FILE_SIZE):
        calculate(convert_name(i))


def convert_name(index):
    return FILE_BASE_NAME + str(index) + FILE_SUFFIX


def import_file():
    for i in range(FILE_SIZE):
        for word in KISHOTENKETSU:
            print (results[convert_name(i) + word])


def show():
    # print (sum_scores)
    print (frequent_scores)
    ki = np.array([frequent_scores["起"][word] for word in KISHOTENKETSU])

    sho = np.array([frequent_scores["承"][word] for word in KISHOTENKETSU])
    ten = np.array([frequent_scores["転"][word] for word in KISHOTENKETSU])
    ketsu = np.array([frequent_scores["結"][word] for word in KISHOTENKETSU])
    print (sum_scores)
    new_sum_scores = np.array([sum_scores[word] for word in KISHOTENKETSU])
    print (ki, sho, ten, ketsu)
    # for word in KISHOTENKETSU:
    #     ki.append(frequent_scores["起"][word])

    # x = np.array([1, 2, 3, 4])


    # plt.bar(x, ki, color="blue", label="起", align="center")
    # plt.bar(x, sho, bottom=ki, color="orange", label="承", align="center")
    # plt.bar(x, ten, color="green", label="転", align="center")
    # plt.bar(x, ketsu, bottom=ki, color="red", label="結", align="center")
    # plt.plot(x, new_sum_scores, "-o")
    # plt.legend()
    # plt.xticks(x, KISHOTENKETSU)
    # plt.show()


calculate_all()
# show()


