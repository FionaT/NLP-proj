__author__ = 'dengjingwen'

import nltk
import re
import json
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

negationWords = ['not', 'no', 'never', 'nt']

fin = open('/Users/dengjingwen/Courses/NLP/manual_read/xac_', 'r')
fout = open('/Users/dengjingwen/Courses/NLP/manual_read/xac__', 'w')
content = fin.readlines()
tokenizer = PunktSentenceTokenizer()
stm = WordNetLemmatizer()
out = []
for line in content:
    line = line.lower()
    line = line.replace('\\n', '')
    line = line.replace('\\', '')
    ss = tokenizer.tokenize(line)
    for s in ss:
        tokens = nltk.word_tokenize(s)
        tks = ''
        p = ''
        for w in tokens:
            w = stm.lemmatize(re.sub(r'[^a-z\-]','', w))
            if (w in negationWords):
                if p == '':
                    p = 'neg_'
                else:
                    p = ''
                continue
            if len(w) > 2 and not w in stopwords.words('english'):
                tks = tks + ' ' + p + w
        out.append(tks)
json.dump(out, fout)
fin.close()
fout.close()
