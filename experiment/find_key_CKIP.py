# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import jieba
import codecs
import io
from collections import Counter
import operator
import numpy


f = codecs.open("target_seg.txt",'r','utf8')
content = f.readlines()
article = []

model = models.Word2Vec.load_word2vec_format('med250.model.bin',binary=True)

print "* Count The Frequency of Data"

line = content[0]
pos = line.find(u" ")

while pos != -1:
	words = line[:pos]
	article.append(words)
	line = line[pos+1:]
	pos = line.find(u" ")


# Count frequency
raw_data = Counter(article)
raw_data = { key:raw_data[key] for key in raw_data if key in model.vocab}


low_level = 0
for key in raw_data:
	low_level += raw_data[key]

low_level = int(round(low_level*0.01))


# Initial Accumalation
print "* Accumalated The Related Words"
acc_data = dict()
words = []

for keys in raw_data:
	words.append(keys)
	acc_data[keys] = 0

for word_1 in words:
	for word_2 in words:
 		if model.similarity(word_1, word_2) >= 0.6:
 			acc_data[word_1] += raw_data[word_2]


s_acc = sorted(acc_data.items(), key=operator.itemgetter(1), reverse=True)


print "* Eliminate The Words Alike"

keywords = []
fg = numpy.zeros(len(s_acc))

for i in range(len(s_acc)):

	if s_acc[i][1] < low_level or fg[i] == 1:
		continue

	for j in range(i+1,len(s_acc)):
		if fg[j] != 1:
			if model.similarity(s_acc[i][0], s_acc[j][0]) >= 0.6:
				fg[j] = 1

	keywords.append(s_acc[i][0])
	print s_acc[i][0]



with io.open("target_keywords.txt",'w',encoding='utf-8') as output:
        for text in keywords:
            output.write(text + '\n')




		

