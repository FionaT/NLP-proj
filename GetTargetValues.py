__author__ = 'dengjingwen'

f = open('/Users/dengjingwen/Courses/NLP/manual_read/target_values.txt', 'r')
t = f.readlines()
f.close()
f = open('/Users/dengjingwen/Courses/NLP/manual_read/_target_values.txt', 'w')
for s in t:
    i = 0
    while s[i] != ' ':
        f.write(s[i])
        i = i + 1
    f.write('\n')
f.close()