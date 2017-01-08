# -*- coding: utf-8 -*-

from scipy.cluster.vq import  vq, kmeans, whiten
from scipy.spatial import distance
from gensim.models import word2vec
from gensim import models
import jieba
import codecs
import io
from collections import Counter
import operator
import numpy

f1 = codecs.open("target.txt",'r','utf8')
content = f1.readlines()
article = []

jieba.set_dictionary('jieba_dict/dict.txt.big')
stopwordset = set()
with io.open('jieba_dict/stopwords.txt','r',encoding='utf-8') as sw:
	for line in sw:
		stopwordset.add(line.strip('\n'))

for line in content:
	if line == u'\n' or line== u' ':
		continue
	seg_list = jieba.cut(line)
	for gg in seg_list:
		if gg not in stopwordset and gg != u'\n':
			article.append(gg)

length = len(article)
raw_data = Counter(article)


data_feature = dict() 
data_distributed = []

model = models.Word2Vec.load_word2vec_format('med250.model.bin',binary=True)

for key in raw_data:
	if key not in model.vocab:
		continue
	eignvalue = []
	for other_key in raw_data:
		if other_key not in model.vocab:
			continue
		eignvalue.append(model.similarity(key, other_key))
	
	data_feature[key] = eignvalue

print len(data_feature)

for key in data_feature:
	for iters in range(raw_data[key]):
		data_distributed.append(data_feature[key])		

codes, dist = kmeans(data_distributed, 50)


core = set()
for code in codes:
	closet_dist = 100000.0
	for key in data_feature:
		if key in core:
			continue
		dist = model.similarity(key, other_key)
		if closet_dist > dist:
			closet_dist = dist
			tmp = key
	core.add(tmp)

for c in core:
	print c

