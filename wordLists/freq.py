files = ['acronym','alnum','cap','mixed','lower']

d = {}
num_words = 0
for a in files:
	f = open(a,'r')
	file_string = f.read()
	word_list = file_string.split('\n')
	for word in word_list:
		num_words += 1
		for c in word:
			if(d.get(c) is None):
				d[c] = 1
			else:
				d[c] += 1

print d
print 'num_words', num_words

