#coding: utf-8

import word2vec

def preprocess():
    word2vec.word2vec('wakati_text.txt', 'wakati_text.bin', size=300, verbose=True)

def echo(label, tlist):
    print ("==============================")
    print (label)
    print ('------------------------------')
    for x in tlist:
        print (x[0], x[1])


if __name__ == "__main__":

    # run only onece
    preprocess()

    model = word2vec.load('wakati_text.bin')

    key = 'google'
    tlist = model.cosine(key)
    echo(key, tlist)

    # key = 'ブラジル'
    # tlist = model.cosine(key)[key]
    # echo(key, tlist)