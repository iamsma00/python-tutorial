words = ['surya','mohan','arya']
print(words)
for w in words[:]:
	if len(w)<=4:
		words.insert(0,w)
print(words)

