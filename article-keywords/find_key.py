# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import jieba
import codecs
import io
from collections import Counter
import operator
import numpy


f = codecs.open(sys.argv[0],'r','utf8')
content = f.readlines()
article = []

jieba.set_dictionary('jieba_dict/dict.txt.big')
model = models.Word2Vec.load_word2vec_format('../word2vec-training/med250.model.bin',binary=True)

# import stopword
stopwordset = set()
with io.open('jieba_dict/stopwords.txt','r',encoding='utf-8') as sw:
	for line in sw:
		stopwordset.add(line.strip('\n'))


# Cut The Words , Output: short words in article
for line in content:
	seg_list = jieba.cut(line)
	for gg in seg_list:
		if gg not in stopwordset:
			article.append(gg)


print "* Count The Frequency of Data"
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


print "* Eliminate The Words Alike"
s_acc = sorted(acc_data.items(), key=operator.itemgetter(1), reverse=True)

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



with io.open(sys.argv[1],'w',encoding='utf-8') as output:
        for text in keywords:
            output.write(text + '\n')




		

