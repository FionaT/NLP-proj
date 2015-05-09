import json

overlap_tags_file = open("overlap_tags.txt", 'r')
yelp_file = open("business_attributes.txt", 'r')
our_file = open("business_tags.txt", 'r')

find_index = {}

overlap_tags = []
business_attr = []

count = 0

#get the overlap_tags from yelp attributes set and our tags set
for line in overlap_tags_file:
	overlap_tags = line.split(",")

#get all business and its attributes from yelp data
#map the business id to its index for furture use
for line in yelp_file:
	line = line.split(",")
	line = line[:-1]
	business_attr.append(line)
	find_index[line[0]] = count
	count += 1

#initialize the variables
count = 0
precision = 0
recall = 0

total_corrects = 0
total_tags1 = 0
total_tags2 = 0

for line in our_file:

	#read our result file about predicted business tags
	line = line.split(",")
	line = line[:-1]

	index = find_index[line[0]]

	#set1 is the business attributes from yelp
	set1 = business_attr[index][1:]

	#calculate the intersection of set1 and overlap_tags
	#overlap_tags is the tags set that our system share with yelp attributes set
	set1 = set(set1).intersection(overlap_tags)

	#set1 is the business tags from our result
	set2 = line[1:]

	#calculate the intersection of set2 and overlap_tags
	#overlap_tags is the tags set that our system share with yelp attributes set
	set2 = set(set2).intersection(overlap_tags)

	overlap = set(set1).intersection(set2)
	
	count += 1
	
	response = len(set2)
	key = len(set1)
	correct = len(overlap)

	total_corrects += correct
	total_tags1 += response
	total_tags2 += key

	print "yelp: ",
	print business_attr[index][0], set1

	print "our: ",
	print line[0], set2
	
	if(response == 0):
		precision += 0
	else:
		precision += correct / float(response)
		print "precision: " + str(correct / float(response))
	
	if(key == 0):
		recall += 0
	else:
		recall += correct / float(key)
		print  "recall: " + str(correct / float(key))

	#print an empty line
	print ""
	#print precision, recall

print "total_precision: " + str(precision/count)
print "total_recall: " + str(recall/count)
print "total_corrects / total_response_tags: " + str(total_corrects / float(total_tags1))
print "total_corrects / total_key_tags: " + str(total_corrects / float(total_tags2))


