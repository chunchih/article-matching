# -*- coding: utf-8 -*-

#################################################
# example.py
# ckip.py
#
# Copyright (c) 2012-2014, Chi-En Wu
# Distributed under The BSD 3-Clause License
#################################################

from __future__ import unicode_literals, print_function

from ckip import CKIPSegmenter, CKIPParser
import codecs
import time
from collections import Counter
import io

f = codecs.open("target.txt",'r','utf8')
f2 = codecs.open("target_seg.txt",'w','utf8')
r_txt = f.readlines()
content = []
for sete in r_txt:
    pos = sete.find(u"。")
    while pos != -1:
        content.append(sete[:pos])
        sete = sete[pos+1:]
        pos = sete.find(u"。")



segmenter = CKIPSegmenter('username', 'account')

j = 0
words = []
for line in content:
    print(j)
    j+=1

    if line == u"\n":
        continue
    
    result = segmenter.process(line)
    if result['status_code'] != '0':
        print('Process Failure: ' + result['status'])

    for sentence in result['result']:
        for term in sentence:
            words.append(term['term'])
    time.sleep(3)

f2.write(u' '.join(words))
     



# Usage example of the CKIPParser class
# parser = CKIPParser('jerry042827', 'howard128')
# result = parser.process('這是一隻可愛的小花貓')
# if result['status_code'] != '0':
#     print('Process Failure: ' + result['status'])

# for sentence in result['result']:
#     for term in traverse(sentence['tree']):
#         print(term['term'], term['pos'])
