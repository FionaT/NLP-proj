import json

our_tags = open("our_tags_set", 'r')
yelp_tags = open("Yelp_tags_set.txt", 'r')

overlap = []
tags2 = []

for line in yelp_tags:
	line = line.split(" \n")
	tags2.append(line[0])

tags1 = our_tags.readline()

tags1 = tags1.split(",")

overlap = set(tags1).intersection(tags2)

#print tags1
#print tags2

print overlap

out_file = open("overlap_tags.txt", 'w')

for o in overlap:
	out_file.write(o + ",")
