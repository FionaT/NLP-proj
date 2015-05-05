
file_name = "output.txt"

contents = []

with open(file_name) as f:
    lines = f.readlines()

for line in lines:
	content = line.split(',')
	contents.append(content)

print contents
print contents[0]
print contents[0][0]
