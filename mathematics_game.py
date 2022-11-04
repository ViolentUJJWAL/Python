import random,time
def correct():
	print("your answer is correct")
def wrong(ex):
	print("correct answer is ",ex)
def addlist(ans,youra,ex,correctans):
	youra.append(ans)
	correctans.append(ex)
def timernow():
	print("_____Game______")
	time.sleep(1)
	print("_____Start_____")
	time.sleep(1)
	print("_____Now_______")
	time.sleep(1)
	print("_______________")
	
	

while True:
	print('')
	title=['M','A','T','H','E','M','A','T             G','I           A','C         M','S       E']
	for ti in range(len(title)):
		print(" "*ti*2,title[ti])
		time.sleep(0.5)
	print('')
	l=[]
	s=int(input("enter starting no. = "))
	n=int(input("enter ending no. = "))
	for a in range(s,n+1):
		l.append(a)
	o=['+','-','*']
	youra=[]
	correctans=[]
	w=0
	c=0
	r=0
	timernow()
	start=time.time()
	while r<10:
		f1=random.choice(l)
		f2=random.choice(l)
		o1=random.choice(o)
		r=r+1
		if o1=='+':
			print(f1,o1,f2)
			ans=eval(input("enter answer = "))
			ex=f1+f2
			addlist(ans,youra,ex,correctans)
			if ex==ans:
				correct()
				c=c+1
			else:
				wrong(ex)
				w=w+1
		elif o1=='-':
			print(f1,o1,f2)
			ans=eval(input("enter answer = "))
			ex=f1-f2
			addlist(ans,youra,ex,correctans)
			if ex==ans:
				correct()
				c=c+1
			else:
				wrong(ex)
				w=w+1
		elif o1=='*':
			print(f1,o1,f2)
			ans=eval(input("enter answer = "))
			ex=f1*f2
			addlist(ans,youra,ex,correctans)
			if ex==ans:
				correct()
				c=c+1
			else:
				wrong(ex)
				w=w+1
		else:
			print('error')

	end=time.time()
	ret=str(end-start)
	sret=ret.split(".")
	print("your timing is ",sret[0],"second")
	print("wrong answer is ",w)
	print("correct answer is ",c)
	print("your ans.      correct ans.")
	for p in range(0,len(youra)):
		time.sleep(1)
		print(youra[p],'            ',correctans[p])
	print("__________Game end__________")
	res=input('''R for Restart
Q for Exit
		-''')
	if res=="r" or res=="R":
		pass
	else:
		co=input('''Sure for exit game
Y for yes
N for no
		-''' )
		if co=="y" or co=="Y":
			break
		elif co=="n" or co=="N":
			pass