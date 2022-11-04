m=input("Enter the Name: ")
n=int(input("Enter the number: "))
k=0
for a in range(n, 0, -1):
	print(f'''{f"{m} "*a}{f"{' '*(len(m)+1)}"*k}{f"{m} "*a}''')
	k += 2
i=(n-1)*2
for b in range(1, n+1):
	print(f'''{f"{m} "*b}{f"{' '*(len(m)+1)}"*i}{f"{m} "*(b)}''')
	i -= 2