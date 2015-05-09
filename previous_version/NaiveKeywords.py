__author__ = 'dengjingwen'

import nltk
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

negationWords = ['not', 'no', 'never', 'nt']

fin = open('tags_keywords.txt', 'r')
lines = fin.readlines()
tags = []
for line in lines:
    line = line.split(',')
    tags.append(line)

tokenizer = PunktSentenceTokenizer()
stm = WordNetLemmatizer()

def getFeatures(s):
    features = []
    tokens = nltk.word_tokenize(s)
    tks = []
    for w in tokens:
        tks.append(stm.lemmatize(re.sub(r'[^a-z\-]','', w)))
    p = ''
    l1 = len(tks)
    for i in range(l1):
        w = tks[i]
        if (w in negationWords):
            p = 'not '
            continue
        for tag in tags:
            for kw in tag[1:]:
                kl = kw.split(' ')
                l2 = len(kl)
                w = 1
                for j in range(l2):
                    if i + j < l1 and kl[j] != tks[i + j]:
                        w = 0
                        break
                if w == 1:
                    features.append(p + tag[0])
                    break
    return features

def extractFeatures(line):
    multiFeatures = []
    features = {}
    line = line.lower()
    line = line.replace('\\n', '')
    line = line.replace('\\', '')
    ss = tokenizer.tokenize(line)
    for s in ss:
        multiFeatures = getFeatures(s)
        for f in multiFeatures:
            if f.startswith('not'):
                f = f.lstrip('not ')
                if f not in features:
                    features[f] = [0, 1]
                else:
                    li = features[f]
                    li[1] += 1
                    features[f] = li
            else:
                if f not in features:
                    features[f] = [1, 0]
                else:
                    li = features[f]
                    li[0] += 1
                    features[f] = li
    features = features.items()
    features.sort(key=lambda x: x[1][0]-x[1][1])
    features.reverse()
    return features