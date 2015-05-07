__author__ = 'dengjingwen'

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

#To predict one test sentence
test = ['I hate that it\'s cash only', 'service excellent time ordered whole pie']
response = tfidf.transform(test)
print(classifier.predict(response))
