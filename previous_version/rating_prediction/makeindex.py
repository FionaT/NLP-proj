import json
import sys
import pickle

f = open("models/complete.model", "r")
# read in the probabilities
probs = json.loads(f.read())
positive = probs["____special_positive____"]
negative = probs["____special_negative____"]
f.close()

# predict exact stars
def write_star():
    # total_stars in format {business_id: [real_star, predicted_star]}
    real_stars = []
    sentiment = []
    total_stars = {}
    g = open("review.json", "r")
    for each in g.readlines():
        dic = json.loads(each)
        b_id = dic["business_id"]
        total_stars[b_id] = []
        content = dic["text"].split()
        star = dic["stars"]
        real_stars.append((b_id, star))
        p_pos = positive
        p_neg = negative
        for word in [word for word in content if word in probs]:
            (a, b) = probs[word]
            p_pos *= a
            p_neg *= b
        if p_neg == 0:
            sentiment.append((b_id, sys.float_info.max))
        else:
            sentiment.append((b_id, p_pos / p_neg))

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
    print "computing the average scores .."
    for (a,b) in real_stars:
        total_stars[a].append(b)
    for each in total_stars:
        ori = total_stars[each]
        total = 0.0
        for i in range(0, len(ori)):
            total += ori[i]
        total /= (len(ori))
        total_stars[each] = [total]
    # compute predicted scores
    for (a,b) in sentiment:
        total_stars[a].append(b)
    for each in total_stars:
        ori = total_stars[each]
        total = 0.0
        for i in range(1, len(ori)):
            total += ori[i]
        total /= (len(ori)-1)
        total_stars[each] = [ori[0], total]
    # write the dict to file
    print 'generating index ..'
    for each in total_stars:
        total_stars[each][0] = round(total_stars[each][0] * 2) / 2.0
        total_stars[each][1] = round(total_stars[each][1] * 2) / 2.0
    f = open('star_index', 'w')
    pickle.dump(total_stars, f)
    f.close

# call the function you want
write_star()