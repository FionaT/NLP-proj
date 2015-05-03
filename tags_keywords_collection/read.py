import json

file_name = "tags_keywords.txt"

the_file = open(file_name, 'r')

j1 = json.load(the_file)

print j1