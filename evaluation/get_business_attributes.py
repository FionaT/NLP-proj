import json

yelp_file = open("yelp_academic_dataset_business.json", 'r')
out_file = open("business_attributes.txt", 'w')

attr_map = {}

count = 0

for line in yelp_file:
	json_line = json.loads(line)

	#print json_line["business_id"],
	out_file.write(json_line["business_id"] + ","),

	yelp_tags = []

	for key, value in json_line["attributes"].iteritems():
		if(key == "Good For"):
			#print json_line["attributes"]["Good For"]
			for key, value in json_line["attributes"]["Good For"].iteritems():
				
				yelp_tags.append("Good For " + key)
				out_file.write("Good For " + key + ","),
				#print "Good For " + key,
				#attr_map["Good For " + key] = 1
		else:	
			yelp_tags.append(key)
			out_file.write(key + ","),
			#print key,
			#attr_map[key] = 1

	out_file.write("\n")
	#print "\n"
