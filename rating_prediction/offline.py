import json

f = open("info.json", "r")
dic = json.loads(f.read().encode('utf-8'))

invertedindex = {}

for bid in dic:
	infos = dic[bid]
	if "name" not in infos:
		continue
	name = infos["name"].lower()
	invertedindex[name+"__"] = bid
	tokens = name.split()
	for word in tokens:
		if word in invertedindex:
			invertedindex[word].append((bid, 1))
		else:
			invertedindex[word] = [(bid, 1)]

f.close()
f = open("invertedindex", "w")
f.write(json.dumps(invertedindex))