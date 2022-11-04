class vector:
	def __init__(self, vec):
		self.vec=vec

	def __add__(self, vec2):
		addlist=[]
		if len(self.vec) != len(vec2.vec):
			return 'Error: list index not same'
		else:
			for a in range(len(self.vec)):
				addlist.append(self.vec[a]+vec2.vec[a])
			return addlist

	def __sub__(self, vec2):
		sublist=[]
		if len(self.vec) != len(vec2.vec):
			return 'Error: list index not same'
		else:
			for a in range(len(self.vec)):
				sublist.append(self.vec[a]-vec2.vec[a])
			return sublist

	def __mul__(self, vec2):
		mullist=[]
		if len(self.vec) != len(vec2.vec):
			return 'Error: list index not same'
		else:
			for a in range(len(self.vec)):
				mullist.append(self.vec[a]*vec2.vec[a])
			return mullist

	def balance(self, v2):
		re=len(v2)-len(self.vec)
		for i in range(re):
			self.vec.append(0)
		return self.vec

	def __len__(self):
		return len(self.vec)

	def __str__(self):
		return f'{self.vec}'


list1=[]
ran=int(input('Enter 1st vector range: '))
for p in range(ran):
	list1.append(int(input('Enter value of vector = ')))
v1= vector(list1)
print(v1)
print(f'len of {len(v1)}')
print('')
list2=[]
ran=int(input('Enter 2nd vector range: '))
for p in range(ran):
	list2.append(int(input('Enter value of vector = ')))
v2= vector(list2)
print(v2)
print(f'len of {len(v2)}')
print('')
if len(v1)!=len(v2):
	if len(v1)<len(v2):
		v1.balance(v2)
	else:
		v2.balance(v1)
print(v1)
print(v2)
print('Add')
print(v1+v2)
print('Sub')
print(v1-v2)
print('Mul')
print(v1*v2)
print('(v1+v2)-v2')
v=vector(v1+v2)
print(v-v2)