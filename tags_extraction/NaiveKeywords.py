__author__ = 'dengjingwen'

import nltk
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

negationWords = ['not', 'no', 'never', 'nt']

fin = open('/Users/dengjingwen/Courses/NLP/manual_read/tags_keywords.txt', 'r')
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
    features = []
    line = line.lower()
    line = line.replace('\\n', '')
    line = line.replace('\\', '')
    ss = tokenizer.tokenize(line)
    for s in ss:
        multiFeatures = multiFeatures + getFeatures(s)
    for f in multiFeatures:
        if not f in features:
            features.append(f)
    return features

print(extractFeatures('I don\'t like them that they do not accept credit card. Charlotte Meeting Room is a modern and new place for holding events and business meetings. They have state of the art equipment included in the price. We held network training classes there for 30 people. The high wattage outlets were stable enough to power all our equipment and computers without any glitches. Internet bandwidth is also great. We used Wifi for most of our work. The business park is very professional and upscale with plenty of free parking.'))