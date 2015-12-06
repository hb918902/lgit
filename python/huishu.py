def is_palindrome(n):
	m=list(str(n))
	m.reverse()
	#if m==list(str(n)):
	#	return n
	return m==list(str(n))


output = filter(is_palindrome, range(1, 1000))
print(list(output))