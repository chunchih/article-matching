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

if len(content) == 0:
	content = r_txt


segmenter = CKIPSegmenter('jerry042827', 'howard128')

j = 0
words = []
for line in content:
    print(j)
    j+=1
    print(line)	

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
