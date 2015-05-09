import json

dis = [0.0, 0.0, 0.0, 0.0, 0.0]

f = open("training_review.json", "r")
i = 0
for each in f.readlines():
    dic = json.loads(each)
    star = dic["stars"]
    dis[star-1] += 1
    i += 1

f.close()
print dis
dis = [float(each/i) for each in dis]
print dis