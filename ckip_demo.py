# -*- coding: utf-8 -*-


from __future__ import unicode_literals, print_function

from ckip import CKIPSegmenter, CKIPParser
import codecs
import time
from collections import Counter
import io
import numpy
import time

class CKIPTransform(object):

    def __init__(self, in_file, out_file):
        in_f = codecs.open(in_file,'r','utf8')
        out_f = codecs.open(out_file,'w','utf8')
        r_txt = in_f.readlines()
        para = len(r_txt)
        self.log_in()
        
    def log_in(self):
        f_account = codecs.open("ckip_account.txt",'r')
        account_info = f_account.readlines()
        self.segmenter = CKIPSegmenter(account_info[0][:-1], account_info[1][:-1])


def art_iter(line):
    tmp = line
    len_art = len(tmp)
    try:
        if len(line) > 400:
            line = line -10 # go to except

        result = segmenter.process(line)
        if result['status_code'] != '0':
            print('Process Failure: ' + result['status'])

        words = []
        for sentence in result['result']:
            for term in sentence:
                words.append(term['term'])
        time.sleep(3)


        return words

            
    except:

        mid = int(len_art/2)
        mid = line.find(u" ", mid-10, mid +10)
        front = art_iter(line[:mid])
        back = art_iter(line[mid+1:])
        out = front
        for item in back:
            out.append(item)
        return out











list_word = []

tStart = time.time()
j = 0

for i in r_txt:
    output = art_iter(i)
    j+=1

    for item in output:
        f2.write(item+u" ")
    f2.write(u"\n")
    print("%s: %s s" % (str(j),str(time.time()-tStart)))
tEnd = time.time()

print(tEnd - tStart)