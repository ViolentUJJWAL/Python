import time

def month(mo):
	if mo==1:
		m=3/12
		return m
	elif mo==2:
		m=2/12
		return m
	elif mo==3:
		m=1/12
		return m
	elif mo==4:
		m=1
		return m
	elif mo==5:
		m=11/12
		return m
	elif mo==6:
		m=10/12
		return m
	elif mo==7:
		m=9/12
		return m
	elif mo==8:
		m=8/12
		return m
	elif mo==9:
		m=7/12
		return m
	elif mo==10:
		m=6/12
		return m
	elif mo==11:
		m=5/12
		return m
	elif mo==12:
		m=4/12
		return m
	
def dep(j,d,value,mo,t):
	while j==1:
		m=month(mo)
		rd=d*m
		value=value-rd
		print(j,"year of deprciadion is ",rd, " and value is ", value )
		time.sleep(0.5)
		j=j+1
	while j<=t:
		value=value-d
		print(j,"year of deprciadion is ",d ," and value is ", value )
		time.sleep(0.5)
		j=j+1

if __name__=='__main__':
	while True:
		print('''
		Depreciasion Finder
			''')
		value=int(input("Enter assest value :"))
		t=int(input("Enter time (note- enter only years): "))
		mo=int(input("enter month (in a no. 1 to 12)[default enter 4]: "))
		pt=0
		sr=input('''Enter salvage value / rate of deprciadion 
		(note- enter rate of dep. with %) : ''')
		time.sleep(0.5)
		print("Beginning value of assest ",value)
		time.sleep(0.5)
		if sr[len(sr)-1]=="%":
			l=[]
			for a in sr:
				l.append(a)
			l.pop()
			s=""
			i=0
			while i<=len(l)-1:
				s=s+l[i]
				i=i+1
			s=eval(s)
			rate=s/100
			d=value*rate
			j=1
			dep(j,d,value,mo,t)
		else:
			j=1
			d=int(sr)
			dep(j,d,value,mo,t)
	


