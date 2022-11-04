def determinant(matrix):
	if len(matrix)==2:
		deter1=matrix[0][0]*matrix[1][1]
		deter2=matrix[1][0]*matrix[0][1]
		return deter1 - deter2
	else:
		deter=0
		for a in range(len(matrix[0])):
			if matrix[0][a]==0:
				deter1=0
			else:
				deter1=matrix[0][a]*determinant(makeMatrix(a,matrix))
			if (a+1)%2==0:
				deter1=(-1*deter1)
				deter = deter + deter1
			else:
				deter = deter + deter1

		return deter



def makeMatrix(index, matrix):
	mkMatrix=[]
	for a in range(1, len(matrix)):
		row=[]
		for b in range(len(matrix[a])):
			if b != index:
				row.append(matrix[a][b])
		mkMatrix.append(row)
	# print('[------')
	# print(matrix[0][index])
	# for c in mkMatrix:
	# 	print(c)
	# print('------]')
	return mkMatrix


while True:
	size=int(input('Enter matrix size(a*a): a = '))
	matrix=[]
	for a in range(size):
		matrix_row=[]
		for b in range(size):
			n=int(input(f'Enter matrix element in {a+1} row and {b+1} col: '))
			matrix_row.append(n)
		print(matrix_row)
		matrix.append(matrix_row)

	print("\nYour input Matrix is:\n ")
	for c in range(len(matrix)):
		print('|', end="")
		for d in range(len(matrix)):
			print(str(matrix[c][d]).center(5), end="")
		print('|')

	determent=determinant(matrix)
	print(f'\nDeterminant is {determent}\n')