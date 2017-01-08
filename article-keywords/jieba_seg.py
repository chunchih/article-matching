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
out = codecs.open(sys.argv[1],'w','utf8')
content = f.readlines()
article = []

jieba.set_dictionary('jieba_dict/dict.txt.big')

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
            out.write(gg+u" ")
    out.write(u"\n")