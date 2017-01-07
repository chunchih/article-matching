# article_match

[ref-link]

## Step 1 : Download The Raw Data On Wiki 
Organize the article on Wiki to train the model, can choose what kind of data you like [Data Link]
Output : <data>.xml.bz2

## Step 2 : Get Raw Data
Using the function "WikiCorpus" from "gensim.corpora", to get the sentence of the article
* Code : wiki_to_txt.py
```sh
python wiki_to_txt.py <filename of data.xml.bz2>
```
* Output : wiki_texts.txt

## Step 3 : Translation
In some article, there are some simplified chinese words which have same meaning with traditional one, we use "opencc" to translate it.
```sh
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
```
* Output : wiki_zh_tw.txt

## Step 4 : Cut the Sentence
Using the "jieba" to cut the chinese senetence into short words
* Code : segment.py
```sh
python segment.py
```
* Output : wiki_seg.txt

## Step 5 : Start Training
With "wiki_seg.txt", we use "word2vec" to train the matching model
* Code : train.py
```sh
python train.py
```
* Output : <model.bin> (Ref Link : https://drive.google.com/file/d/0B9bH77JfnfxlZlhFaXdudjEwVEU/view?usp=sharing)

## Step 6 : Find Keywords in Article
First, Use "Counter()" to get the frequency of each words in target article. Second, each words to add the frequcy of similar words in order, and sort it. Third, from top of the list, eliminate the following words on list, which is very similar with previous one.
* Code : find_key.py
```sh
python find_key.py
```
* Output : list of the keywords in target article which all of them are not similar to each other.

[ref-site] : http://zake7749.github.io/2016/08/28/word2vec-with-gensim/
[Link]: <https://dumps.wikimedia.org/zhwiki/20160820/zhwiki-20160820-pages-articles.xml.bz2>

