import json

file_name = "subjclueslen1-HLTEMNLP05.tff"

f = open(file_name,"r") #opens file with name of "test.txt"
myList = []

thefile = open('postive_negative_dictionary.txt', 'w')

for line in f:
	myList.append(line)
	item = line.split(" ")
	word = item[2][6:]
	sentiment = item[5][14:]

	#print word, sentiment
	thefile.write("%s " % word)
	thefile.write("%s\n" % sentiment)

  