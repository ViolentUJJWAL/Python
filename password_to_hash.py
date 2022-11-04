import random
def rph(randomhasslist):
	 r=random.choice(randomhasslist)
	 return r

t=int(input('''
	1. for Password to Hashpassword
	2. for Hashpassword to password
	-'''))
if t==1:
	rl=[]
	l=[]
	password=input("Enter your password :")
	for pw in range(len(password)):
		l.append(password[pw])

	randomhasslist='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&'
	for ral in range(len(randomhasslist)):
		rl.append(randomhasslist[ral])

	hashp=[]
	for a in range(len(password)):
		for b in range(5):
			hashp.append(rph(randomhasslist))
		hashp.append(l[a])
	last=str(len(password))
	for ax in range(4):
		hashp.append(rph(randomhasslist))
	hashp.append(f"'{last}")
	hashpassword=''
	for has in hashp:
		hashpassword = hashpassword + has

	print(f'your password is convert in hashpassword\n[\n{hashpassword}\n]')

elif t==2:
	hashpassword=input("Enter Hashpassword :")
	password=''
	last=hashpassword.split("'")
	hashp=last[0]
	hashlist=[]
	for li in range(len(hashp)):
		hashlist.append(hashp[li])
	intlast=int(last[1])
	i=0
	for a in range(len(hashlist)):
		if a%5==0:
			if len(password)==intlast:
				pass;
			elif 1<a<len(hashlist)-3:
				b=a+i
				i=i+1
				password=password+hashlist[b]
	print(f'\nYour password is \n {password}')




