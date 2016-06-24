# coding: utf-8

import sys
import json
import MeCab
# import urllib2
from collections import defaultdict
from operator import itemgetter
# from BeautifulSoup import *


# class HTMLParser():
#
#     def get(self, url):
#         try:
#             c = urllib2.urlopen(url)
#         except:
#             # print "Could not open %s" % url
#             return ""
#
#         soup = BeautifulSoup(c.read())
#         text = '\n'.join(self.__getNavigableStrings(soup))
#         return text
#
#     def __getNavigableStrings(self, soup):
#       if isinstance(soup, NavigableString):
#         if type(soup) not in (Comment, Declaration) and soup.strip():
#           yield soup
#       elif soup.name not in ('script', 'style'):
#         for c in soup.contents:
#           for g in self.__getNavigableStrings(c):
#             yield g
#

if __name__ == "__main__":

    f = open("sample0.txt", "r")
    # urls = json.load(f)
    # f.close()
    # print "Count of urls : " + str(len(urls))
    # STOP_WORD = " 。 、 「 」 （ ） ? ？ ： ， , ． ! ！ # $ % & ' ( ) = ~ | ` { } * + ? _ > [ ] @ : ; / . ¥ ^ 【 】 ￥ ＿ ／ 『 』 ＞ ？ ＿ ＊ ＋ ｀ ｜ 〜 ＊ ＋ ＞ ？ ＃ ” ＃ ＄ ％ ＆ ’ \" ・".split()
    #
    # hp = HTMLParser()
    tagger = MeCab.Tagger("-O wakati")
    wakati_text = []

    for url in f.readline():
        text = url
        wakati_raw = tagger.parse(text.encode('utf-8'))
        wakati_formalize = []
        for row in wakati_raw.split('\n'):
            row = row.rstrip().lower()
            for sw in STOP_WORD:
                row = row.replace(sw, '')
            wakati_formalize.append(row)
        wakati_text.append(' '.join(wakati_formalize))

    f = open("wakati_text.txt", 'w')
    f.write('\n'.join(wakati_text))
    f.close()