# coding: utf-8
import gensim
import doc2vec
# import mysql.connector

#定義
previous_title = ""
docs = []
titles = []

#MySQLに接続
config = {
  'user': "USERNAME",
  'password': 'PASSWORD',
  'host': 'HOST',
  'database': 'DATABASE',
  'port': 'PORT'
}

sentences = [
    ['human', 'interface', 'computer'],  # 0
    ['survey', 'user', 'computer', 'system', 'response', 'time'],  # 1
    ['eps', 'user', 'interface', 'system'],  # 2
    ['system', 'human', 'system', 'eps'],  # 3
    ['user', 'response', 'time'],  # 4
    ['trees'],  # 5
    ['graph', 'trees'],  # 6
    ['graph', 'minors', 'trees'],  # 7
    ['graph', 'minors', 'survey']  # 8
]

# connect = mysql.connector.connect(**config)
#Queryを実行する
# cur=connect.cursor(buffered=True)
#
# QUERY = "select d.title,d.body from docs as d order by doc.id" #ここはカスタマイズしてください
# cur.execute(QUERY)
# rows = cur.fetchall()

#Queryの出力結果をforで回してsentencesとlabelsを作成
# i = 0
# for row in rows:
#   if previous_title != row[0]:
#     previous_title = row[0]
#     titles.append(row[0])
#     docs.append([])
#     i+=1
#   docs[i-1].append(row[1])
#
# cur.close()
# connect.close()

"""
上で作っているデータは要するにこういうデータです。
docs = [
    ['human', 'interface', 'computer'], #0
    ['survey', 'user', 'computer', 'system', 'response', 'time'], #1
    ['eps', 'user', 'interface', 'system'], #2
    ['system', 'human', 'system', 'eps'], #3
    ['user', 'response', 'time'], #4
    ['trees'], #5
    ['graph', 'trees'], #6
    ['graph', 'minors', 'trees'], #7
    ['graph', 'minors', 'survey'] #8
]

titles = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5",
    "doc6",
    "doc7",
    "doc8",
    "doc9"
]
"""

# labeledSentences = doc2vec.LabeledListSentence(sentences, ["TSE", "TEST"])
sentences = doc2vec.LabeledSentence(words=[u'some', u'words', u'here'], labels=[u'SENT_1'])

model = gensim.models.doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
model.build_vocab(sentences)
for epoch in range(10):
    model.train(sentences)
    model.alpha -= 0.002  # decrease the learning rate
    model.min_alpha = model.alpha  # fix the learning rate, no decay

# model = gensim.models.doc2vec.Doc2Vec(documents, min_count=0)
#
# # ある文書に似ている文書を表示
# print model.most_similar_labels('SENT_doc1')
#
# # ある文書に似ている単語を表示
# print model.most_similar_words('SENT_doc1')
#
# # 複数の文書を加算減算した上で、似ているユーザーを表示
# print model.most_similar_labels(positive=['SENT_doc1', 'SENT_doc2'], negative=['SENT_doc3'], topn=5)
#
# # 複数の文書を加算減算した上で、似ている単語を表示
# print model.most_similar_words(positive=['SENT_doc1', 'SENT_doc2'], negative=['SENT_doc3'], topn=5)
