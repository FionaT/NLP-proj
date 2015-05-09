__author__ = 'dengjingwen'

import nltk
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

fin = open('/Users/dengjingwen/Courses/NLP/manual_read/sentens_samples.txt', 'r')
texts = fin.readlines()
tfidf = TfidfVectorizer()
x = tfidf.fit_transform(texts)
fin.close()
tv = open('/Users/dengjingwen/Courses/NLP/manual_read/_target_values.txt', 'r')
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

#test = ['I hate that it\'s cash only', 'service excellent time ordered whole pie', 'support parking']
#response = tfidf.transform(test)
#print(classifier.predict(response))
print(extractFeatures('I don\'t like them that they do not accept credit card. Charlotte Meeting Room is a modern and new place for holding events and business meetings. They have state of the art equipment included in the price. We held network training classes there for 30 people. The high wattage outlets were stable enough to power all our equipment and computers without any glitches. Internet bandwidth is also great. We used Wifi for most of our work. The business park is very professional and upscale with plenty of free parking.'))