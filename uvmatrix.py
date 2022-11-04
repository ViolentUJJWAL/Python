import random, time

def re():    		                        							  #pick random
	l=['z', ' ', 'x', 'c', 'v', 'b', 'n', 'm', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/', '*', '-', '+', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '<', '>', ':', ';', '/', '*', '-', '+', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '<', '>', ':', ';']
	a=random.choice(l)
	return a

def abcd(name,r=60):							#start slow matrix 
	t=0.1
	while True:
		time.sleep(t)
		print(f' {name}  ', end='')
		for a in range(r):
			print(f' {re()}', end='')
		print(f'   {name} ', end='')
		print('')

def sabcd(name,r=60):   	                    #start fast matrix
	while True:
		print(f' {name}  ', end='')
		for a in range(r):
			print(f' {re()}', end='')
		print(f'   {name} ', end='')
		print('')

def mr():										#print matrix 13 times in top of matrix start
	m='MATRIX  '
	print(f'   {m*18}')
	print('')

						#satrt matrix coding

print('')
print('		WELCOME_TO_MATRIX_WORLD')
print('	(note- Matrix stop for [ Ctrl + C ])')
work=input('''		    1 for with Name
    		    2 for without name
    		    3 for EXIT
	-''')
if work=='1':								#for with name 
	name=input('Name- ')
	s=input('''
		Speed
		1 for Slow
		2 for Fast
		   -''')
	if s=="1":								#slow matrix with name 
		mr()
		abcd(name)
	elif s=="2":							#fast matrix with name
		sabcd(name)
	else:
		print('enter valid no.')
elif work=="2":								#for without name
	s=input('''
		Speed
		1 for Slow
		2 for Fast
		   -''')
	if s=="1":								#slow matrix without name
		mr()
		abcd('',70)
	elif s=="2":							#fast matrix without name
		sabcd('',70)
	else:
		print('enter valid no.')
elif work=='3':								#for exit
	print('EXIT      '*5)
else:								
	print("enter valid")
