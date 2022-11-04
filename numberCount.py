def digit(a):
	n=1
	while(a!=0):
		a=a//10
		n = n *10
	return n

while True:
	print('')
	print('How many times comes number')
	a=int(input("Enter the starting no.: "))
	b=int(input("Enter the ending no.: "))
	s=int(input("Enter the count no. in range: "))
	count=0
	for i in range(a,b+1):
		j=i
		d=digit(s)
		while(j!=0):
			m=j%d
			if m==s:
				count += 1
			j=j//d

	print('')
	print(f'Number {s} occurs {count} times in the range from {a} to {b}')
