__author__ = 'dengjingwen'

import nltk
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

fin = open('sentens_samples.txt', 'r')
texts = fin.readlines()
tfidf = TfidfVectorizer()
x = tfidf.fit_transform(texts)
fin.close()
tv = open('_target_values.txt', 'r')
y = tv.readlines()
classifier = RandomForestClassifier()
classifier.fit(x, y)

negationWords = ['not', 'no', 'never', 'nt']

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
    test1 = ''
    test2 = ''
    for i in range(l1):
        w = tks[i]
        if (w in negationWords):
            p = 'neg_'
            continue
        test1 = test1 + p + w + ' '
        test2 = test2 + w + ' '
    test1 = [test1]
    test2 = [test2]
    result1 = classifier.predict(tfidf.transform(test1))
    result2 = classifier.predict(tfidf.transform(test2))
#    print(test1)
#    print(result1)
#    print(test2)
#    print(result2)
    for t in result1:
        features.append(t[:-1])
    if p != '':
        for t in result2:
            if (t[0] == '-'):
                features.append(t[1:-1])
            else:
                if (t[0] != '0'):
                    features.append('-' + t[:-1])
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
