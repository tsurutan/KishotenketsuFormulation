#coding:utf-8
import MeCab
f = open("chumon.txt", "w")
def parse(s):
    tagger = MeCab.Tagger('-Owakati')
    result = tagger.parse(s)
    f.write(result)
    print (result)

for line in open("chumon.txt"):
    parse(line)
f.close()