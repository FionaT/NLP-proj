import json

input_file = open("partfeature-1", 'r')
out_file = open("business_tags.txt", 'w')

the_file = []

for line in input_file:
	the_file = json.loads(line)

for key, value in the_file.iteritems():
	#print key + ",",
	out_file.write(key + ","),

	for v in value:
		if(v[1][0] >= v[1][1]):
			out_file.write(v[0] + ","),
			#print v[0] + ",",

	out_file.write("\n"),
	#print "\n"



#print the_file["_qvxFHGbnbrAPeWBVifJEQ"]
