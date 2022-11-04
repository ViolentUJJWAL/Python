def mean(xi,f,n):
	xifi=0
	for a in range(len(xi)):
		xifi=xifi+(xi[a]*f[a])
	fi=0
	for e in xi:
		fi=fi+e
	if n>0:
		xMean=xifi/n
	else:	
		xMean=xifi/fi
	return xMean

def make_xi_f(xi):
	l=[]
	for a in range(len(xi)):
		l.append(1)
	return l

while True:
	print('FIND THE MEAN')
	Que_type=input('Question type\n1 for single frequency\n2 for frequency and items\n3 for with range\n  -')
	if Que_type=='1' or Que_type=='2' or Que_type=='3':
		n=int(input('Enter no. of frequency = '))
		xi=[]
		for a in range(n):
			value=eval(input('Enter frequency value = '))
			xi.append(value)
		f=[]
		if Que_type=="1":
			f=make_xi_f(xi)
			for x in xi:
				print(f'{x}')

		elif Que_type=="2":
			for e in range(n):
				value=eval(input('Enter items no. of value = '))
				f.append(value)
			for x,g in zip(xi,f):
				print(f'{x}     {g}')
			n=0

		elif Que_type=="3":
			rangeList=[]
			for e in range(n):
				print(f'\n{e+1} range')
				minRange=eval(input('Enter min. range = '))
				maxRange=eval(input('Enter max. range = '))
				rangeList.append([minRange,maxRange])
			for i in rangeList:
				midrange=(i[0]+i[1])/2
				f.append(midrange)

			for ra,x,g in zip(rangeList,xi,f):
				print(f'{ra}     {x}     {g}')
			n=0

		Mean=mean(xi,f,n)
		print(f'Mean is {Mean}')
	else:
		print('Enter valid selection')


	 