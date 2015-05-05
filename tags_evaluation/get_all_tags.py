import json

file_name = "yelp_academic_dataset_business.json"
out_file = "all_tags_from_Yelp.txt"

the_file = open(file_name, 'r')
output = open(out_file, 'w')

attr_map = {}

count = 0

for line in the_file:
	#print line
	json_line = json.loads(line)

	for key, value in json_line["attributes"].iteritems():
		attr_map[key] = 1
		#print key


for key, value in attr_map.iteritems():
	output.write("%s \n" % key)
	#print key