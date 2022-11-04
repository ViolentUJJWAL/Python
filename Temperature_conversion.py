def fahrenheit(c):
	f=(c*(9/5))+32
	return f
def celsius(f):
	c=(f-32)/1.8
	return c

u=int(input('''
	1 for convert celsius
	2 for convert fahrenheit
	-'''))
if u==1:
	f=eval(input("Enter fahrenheit :"))
	c=celsius(f)
	print(f"{f} fahrenheit is equl to {c} celsius")
elif u==2:
	c=eval(input("Enter celsius :"))
	f=fahrenheit(c)
	print(f"{c} celsius is equl to {f} fahrenheit")
else:
	print("none")