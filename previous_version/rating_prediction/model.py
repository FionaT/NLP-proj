import json

f = open("training_review.json", "r")
# global dict of tokens: {token : pos_prob} 
tokens = {}
pos = 0.0
neg = 0.0

i = 0
for each in f.readlines():
    dic = json.loads(each)
    star = dic["stars"]
    ifPos = (star >= 3)
    if ifPos:
        pos += 1
    else:
        neg += 1
    # normalize to a non-negative score
    positiveProb = [0.0, 1, 0.3, 0.3, 0.8, 1][star]
    # preprocess the text
    content = dic["text"].lower().split()
    # put it in the global dict
    for word in content:
        if word not in tokens:
            if ifPos:
                tokens[word] = (float(positiveProb), 0)
        else:
            (a, b) = tokens[word]
            if ifPos:
                a += positiveProb
            else:
                b += positiveProb
            tokens[word] = (a, b)
    i += 1
    if i % 100000 == 0:
        print i

f.close()
# normalize all stats and do Laplace smoothing
for each in tokens:
    (a, b) = tokens[each]
    a = float((a + 1) / (pos + 1))
    b = float((b + 1) / (neg + 1))
    tokens[each] = (a, b)
pos /= i
neg /= i
tokens["____special_positive____"] = pos
tokens["____special_negative____"] = neg

# write to file
g = open('models/complete.model', 'w')
g.write(json.dumps(tokens))
g.close()