>>> words = ['surya','mohan','arya']
>>> words
['surya', 'mohan', 'arya']
>>> for w in words[:]:
...     if len(w)<=4:
...             words.insert(0,w)
... 
>>> words
['arya', 'surya', 'mohan', 'arya']
>>> 

