questions = ['name','age','contact','address']
answer = ['surya',22,8650,'delhi']

for q,a in zip(questions,answer):
		print('what is your {0}? It is {1}'.format(q,a))