__author__ = 'dengjingwen'

import nltk
import re
import json
from nltk.corpus import stopwords
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

negationWords = ['not', 'no', 'never', 'nt']

fin = open('/Users/dengjingwen/Courses/NLP/manual_read/xac_', 'r')
fout = open('/Users/dengjingwen/Courses/NLP/manual_read/target_values_c.txt', 'w')
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
        l = 0
        for w in tokens:
            w = stm.lemmatize(re.sub(r'[^a-z\-]','', w))
            if w in negationWords:
                p = 'neg_'
                continue
            if len(w) > 2 and not (w in stopwords.words('english')):
                tks = tks + ' ' + p + w
                l = l + len(w)
        if l == 0:
            continue
        #fout.write(tks[1:] + '\n')
        fout.write('0 ' + s)
        if s[-1] != '\n':
            fout.write('\n')
        out.append(tks)
#json.dump(out, fout)
fin.close()
fout.close()
