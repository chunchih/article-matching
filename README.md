# article_match

[ref-link](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)

# Into word2vec-training Folder

## Step 1 : Download The Raw Data On Wiki 
Organize the article on Wiki to train the model, can choose what kind of data you like [Data Link](https://dumps.wikimedia.org/zhwiki/20160820/zhwiki-20160820-pages-articles.xml.bz2)
* Output : `word2vec-model/data.xml.bz2`

## Step 2 : Get Raw Data
Using the function `WikiCorpus` from `gensim.corpora`, to get the sentence of the article
```sh
python wiki_to_txt.py <filename of data.xml.bz2>
```
* Output : `word2vec-model/wiki_texts.txt`

## Step 3 : Translation
In some article, there are some simplified chinese words which have same meaning with traditional one, we use `opencc` to translate it.
```sh
opencc -i wiki_texts.txt -o wiki_zh_tw.txt -c s2tw.json
```
* Output :  `word2vec-model/wiki_zh_tw.txt`

## Step 4 : Cut the Sentence
Using the `jieba` to cut the chinese senetence into short words
```sh
python wiki_seg_jieba.py
```
* Output : `word2vec-model/wiki_seg.txt`

## Step 5 : Start Training
With `wiki_seg.txt`, we use `word2vec` to train the matching model
```sh
python w2v-train.py
```
* Output : `word2vec-model/[model.bin] (https://drive.google.com/file/d/0B9bH77JfnfxlZlhFaXdudjEwVEU/view?usp=sharing)`

# Into article-keywords Folder

## Step 6 : Find the Target Article-keywords:
Put the article in  medium length into `target_article.txt` in `article-keywords`. 

## Step 7 : Cut Target Article Into Short Pieces
Register the account and password on CKIP. `CKIP` can provide better effect to cut the chinese sentence than `jieba`; However, the shortcome of `CKIP` is slower to `jieba` because it needs to send sentence by part with Internet and get resouce back. 
```sh
python ckip_seg.py target_article.txt target_seg.txt
```
Rember to put your account and password into `ckip_account.txt` in two lines
* Output : `article-keywords/target_seg.txt`

## Step 8 : Find keywords in target article
First, Use `Counter()` to get the frequency of each words in target article. Second, each words to add the frequcy of similar words in order, and sort it. Third, from top of the list, eliminate the following words on list, which is very similar with previous one.
```sh
python find_key.py target_seg.txt target_keywords.txt
```
* Output : `article-keywords/target_keywords.txt`, list of the keywords in target article which all of them are not similar to each other.



