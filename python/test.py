def triangles():
	L1=[1]
	yield(L1)
	L1=[1,1]
	yield(L1)
	while 1:
		L1=[1]+[L1[i]+L1[i+1]  for i in range(len(L1)-1)]+[1]
		yield(L1)

n=0
for t in triangles():
	print(t)
	n=n+1
	if n==10:
		break


