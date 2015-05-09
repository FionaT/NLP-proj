import json

file_name = "input"

tagsKeywords_out = open('tags_keywords.txt', 'w')
tags_out = open('tags.txt', 'w')

with open(file_name) as f:
    lines = f.readlines()
    
for line in lines:
	output = line.split(',')
	tag = output[0]
	output = output[1: -1]

	for i in range(0, len(output)):
		output[i] = output[i][1:]

	output.insert(0, tag)

	tags_out.write("%s \n" % tag)

	for item in output:
  		tagsKeywords_out.write("%s," % item)

  	tagsKeywords_out.write("\n")

	print output





