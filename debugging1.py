import pdb

pdb.set_trace()

def add(l):
	sum = 0 
	for value in l:
		sum += value
	return sum 

l = [10,20,30,40,50,60]
result = add(l)
print(result)


