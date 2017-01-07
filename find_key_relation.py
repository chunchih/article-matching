# -*- coding: utf-8 -*-

from gensim.models import word2vec
from gensim import models
import jieba
import codecs
import io
from collections import Counter
import operator
import numpy


f = codecs.open("target.txt",'r','utf8')
content = f.readlines()
article = []

jieba.set_dictionary('jieba_dict/dict.txt.big')
model = models.Word2Vec.load_word2vec_format('med250.model.bin',binary=True)

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


# Count frequency
raw_data = Counter(article)
raw_data = { key:raw_data[key] for key in raw_data if key in model.vocab}

low_level = 0

for key in raw_data:
	low_level += raw_data[key]

low_level = int(round(low_level*0.01))


# Initial Accumalation
words = []
acc_data = dict()
map_words = []
related_word = dict()

for keys in raw_data:
 	words.append(keys)
# 	acc_data[keys] = 0

# Pick up the Friends
for word_1 in words:
	cand_words = []
	for word_2 in words:
 		if model.similarity(word_1, word_2) >= 0.6:
 			cand_words.append(word_2)
 	map_words.append(cand_words)



for i in range(len(map_words)):
	friend_list = map_words[i]
	value = 0.0
	for friend_1 in friend_list:
		for friend_2 in friend_list:
			if friend_1 == friend_2:
				continue
			value += model.similarity(friend_1, friend_2)

	leng = len(friend_list)
	related_word[words[i]] = value/float(leng*leng)

s_imp_words = sorted(related_word.items(), key=operator.itemgetter(1), reverse=True)
for i in s_imp_words[:20]:
	print i[0]
print "-----------------------"
#print s_imp_words

# for value in output:
# 	if value[1] == 0.0:
# 		continue
# 	print value[0], value[1]
# 	print "-----------------------"
keywords = []
fg = numpy.zeros(len(s_imp_words))

for i in range(len(s_imp_words)):

	if fg[i] == 1:
		continue

	for j in range(i+1,len(s_imp_words)):
		if fg[j] != 1:
			if model.similarity(s_imp_words[i][0], s_imp_words[j][0]) >= 0.7:
				fg[j] = 1

	keywords.append(s_imp_words[i])
	#print s_imp_words[i][0]

for i in keywords[:10]:
	print i[0]



# with io.open("target_keywords.txt",'w',encoding='utf-8') as output:
#         for text in keywords:
#             output.write(text + '\n')




		

