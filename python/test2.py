from functools import reduce
def str2float(s):
	def f1(x1,x2):
		return x1*10+x2
         #def char2num(s):
         #	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	m=list(s).index('.')
	#int
	inta=reduce(f1,map(int,s[:m]))
	#float
	floata=reduce(f1,map(int,s[(m+1):]))/(10**len(s[(m+1):]))
	return floata+inta
	
print('str2float(\'123.456\') =', str2float('123.456'))



