def  normalize(name):
	name=name.lower().capitalize()
	return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

