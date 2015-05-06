import json

overlap_tags_file = open("overlap_tags.txt", 'r')
yelp_file = open("business_attributes.txt", 'r')
our_file = open("business_tags.txt", 'r')

find_index = {}

overlap_tags = []
business_attr = []

count = 0

for line in overlap_tags_file:
	overlap_tags = line.split(",")

for line in yelp_file:
	line = line.split(",")
	line = line[:-1]
	business_attr.append(line)
	find_index[line[0]] = count
	count += 1

count = 0
precision = 0
recall = 0

for line in our_file:
	

	line = line.split(",")
	line = line[:-1]

	index = find_index[line[0]]
	set1 = business_attr[index][1:]

	set1 = set(set1).intersection(overlap_tags)

	#if(len(set1) == 0):
	#	continue

	

	set2 = line[1:]

	overlap = set(set1).intersection(set2)

	if(len(overlap) == 0):
		continue

	count += 1
	
	response = len(set2)
	key = len(set1)
	correct = len(overlap)

	print business_attr[index][0], set1
	print line[0], set2
	
	if(response == 0):
		precision += 0
	else:
		precision += correct / float(response)
		print correct / float(response)
	
	if(key == 0):
		recall += 0
	else:
		recall += correct / float(key)
		print correct / float(key)

	#print precision, recall

print precision/count , recall/count


	
