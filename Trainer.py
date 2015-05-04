__author__ = 'dengjingwen'

from sklearn.feature_extraction.text import TfidfVectorizer

fin = open('/Users/dengjingwen/Courses/NLP/manual_read/xac__', 'r')
texts = fin.readlines()
tfidf = TfidfVectorizer()
tfidf.fit(texts)
test = ['hmmm neg_quite neg_sure neg_make neg_place', 'service excellent time ordered whole pie']
response = tfidf.transform(test)
print(response)
print('-----------')
feature_names = tfidf.get_feature_names()
print(response.nonzero())
for col in response.nonzero()[1]:
    print(feature_names[col])
    print(response[0, col])