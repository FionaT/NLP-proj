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
		if(key == "Good For"):
			#print json_line["attributes"]["Good For"]
			for key, value in json_line["attributes"]["Good For"].iteritems():
				attr_map["Good For " + key] = 1
		else:	
			attr_map[key] = 1
			#print key


for key, value in attr_map.iteritems():
	output.write("%s \n" % key)
	#print key