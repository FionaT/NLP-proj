__author__ = 'dengjingwen'

import os
from nltk.tree import Tree
from nltk.parse.stanford import StanfordParser

os.environ['STANFORD_PARSER'] = '/usr/local/Cellar/stanford-parser/3.4/libexec/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/usr/local/Cellar/stanford-parser/3.4/libexec/stanford-parser-3.4-models.jar'
parser=StanfordParser(model_path='/usr/local/Cellar/stanford-parser/3.4/libexec/edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
list(parser.raw_parse("the quick brown fox jumps over the lazy dog"))
sentences = parser.raw_parse("the quick brown fox jumps over the lazy dog")
print type(sentences)

# GUI
for line in sentences:
    print line