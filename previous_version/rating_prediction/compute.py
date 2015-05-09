import json
import sys

f = open("models/complete.model", "r")
# read in the probabilities
probs = json.loads(f.read())
positive = probs["____special_positive____"]
negative = probs["____special_negative____"]
f.close()

# predict positive or negative
def eval_pos_neg():
    sentiment = []
    g = open("test_review.json", "r")
    for each in g.readlines():
        dic = json.loads(each)
        content = dic["text"].split()
        star = dic["stars"]
        p_pos = positive
        p_neg = negative
        for word in [word for word in content if word in probs]:
            (a, b) = probs[word]
            p_pos *= a
            p_neg *= b
        # plus 1 so everything is positive
        if p_pos >= p_neg:
            sentiment.append((star, "positive"))
        else:
            sentiment.append((star, "negative"))
    g.close()
    # soft evaluate
    correct = 0.0
    for (star, pred) in sentiment:
        if (star>=3 and pred == "positive") or (star<3 and pred == "negative"):
            correct += 1
    print "soft evaluation: %.3f" % (correct / len(sentiment))

# predict exact stars
def eval_star():
    sentiment = []
    stars = {}
    i = 0
    g = open("review.json", "r")
    for each in g.readlines():
        dic = json.loads(each)
        content = dic["text"].split()
        star = dic["stars"]
        stars[i] = star
        p_pos = positive
        p_neg = negative
        for word in [word for word in content if word in probs]:
            (a, b) = probs[word]
            p_pos *= a
            p_neg *= b
        if p_neg == 0:
            sentiment.append((i, sys.float_info.max))
        else:
            sentiment.append((i, p_pos / p_neg))
        i += 1

    # sort sentiment list and assign stars
    print "sorting the list .."
    sentiment.sort(key=lambda x:x[1])
    print "assigning stars .."
    length = len(sentiment)
    # use the distribution of original set
    marks = [length*10/100, length*20/100, length*35/100, length*65/100]
    cur = 1
    j = 0
    while j < length:
        (a, b) = sentiment[j]
        sentiment[j] = (a, cur)
        j += 1
        if j in marks:
            cur += 1
    print "gathering result .."
    correct = 0.0
    ok = 0.0
    for (a, b) in sentiment:
        if stars[a] == b:
            correct += 1
            ok += 1
        elif abs(stars[a] - b) <= 1:
            ok += 1
    print len(sentiment)
    print "perfect match: %.3f" % (correct / len(sentiment))
    print "good match: %.3f" % (ok / len(sentiment))

# call the function you want
eval_star()