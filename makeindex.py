import sys
import pickle
import json

f = open("business.json", "r")
score = pickle.loads(open("star_index", "r").read())
index = {}

for each in f.readlines():
    dic = json.loads(each)
    bid = dic["business_id"]
    index[bid] = {}
    if bid in score:
        index[bid]["name"] = dic["name"]
        index[bid]["yelp_star"] = dic["stars"]
        index[bid]["analyzed_star"] = score[bid][1]

f.close()
f = open("index", "w")
pickle.dump(index, f)
f.close()