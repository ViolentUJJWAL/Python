A_size=input('Enter matrix A size (in m*n formet): ')
m=int(A_size.split('*')[0])
n=int(A_size.split('*')[1])
A_matrix=[]
for i in range(m):
	print(f'elements of {i+1} row')
	l=[]
	for e in range(n):
		el=int(input('Enter matrix Row element: '))
		l.append(el)
	A_matrix.append(l)
print('matrix A is')
for x in A_matrix:
	print(x)

B_size=input('Enter matrix B size (in m*n formet): ')
m=int(B_size.split('*')[0])
n=int(B_size.split('*')[1])
B_matrix=[]
for i in range(m):
	print(f'elements of {i+1} row')
	l=[]
	for e in range(n):
		el=int(input('Enter matrix Row element: '))
		l.append(el)
	B_matrix.append(l)
print('Matrix B is')
for x in B_matrix:
	print(x)

while True:

	m=input('Enter Multipal formet (in A.B formet): ')
	if m=="q" or m=="Q":
		exit()
	ml=m.split(".")
	A=""
	B=''
	a=ml[0]
	b=ml[1]
	if a=="A" and b=="B" or a=="a" and b=="b":
		A=A_matrix
		B=B_matrix
	elif b=="A" and a=="B" or b=="a" and a=="b":
		B=A_matrix
		A=B_matrix
	else:
		print('Enter valid input')
		exit()
		

	if len(A[0])==len(B):
		main_l=[]
		for y in A:
			back_l=[]
			for z in range(len(B[0])):
				sa=0
				for o in range(len(y)):
					ta=y[o]*B[o][z]
					sa=sa+ta
				back_l.append(sa)
			main_l.append(back_l)
		for x in main_l:
			print(x)

	else:
		print('no Multipal value')



