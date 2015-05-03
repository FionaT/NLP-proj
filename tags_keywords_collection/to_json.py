import json

file_name = "input"

tag = []
keywords = []
tup = ()
output = []
my_dict = {}

with open(file_name) as f:
    lines = f.readlines()
    
for line in lines:
	content = line.split(',')
	tag.append(content[0])
	content = content[1: -1]
	keywords.append(content)

for i in range(0, len(tag)):
	for j in range(0, len(keywords[i])):
		keywords[i][j] = keywords[i][j][1:]

	tup = (tag[i], keywords[i])
	my_dict[tag[i]] = keywords[i]
	#print tag[i], keywords[i]

#print my_dict
j = json.dumps(my_dict)

with open('tags_keywords.txt', 'w') as outfile:
    json.dump(j, outfile)

thefile = open('tags.txt', 'w')

for item in tag:
  thefile.write("%s\n" % item)