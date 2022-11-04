import time

print('''__________CALCULATAR__________
	''')
time.sleep(1)
o=["   OPERATOR","+ for Addition","- for Subtraction","* for Multiplication","/ for Division", "** for first no. power of second no.", "*/ for Square Roots (second no. enter 1)" ]
for n in range(0,len(o)):
	print(o[n])
	time.sleep(0.5)
print("")
while True:
	f1=eval(input("Enter first Number : "))
	eo=input("Enter operator : ")
	f2=eval(input("Enter second Number : "))
	if eo=="+":
		print(f1,eo,f2," = ",f1+f2)
	elif eo=="-":
		print(f1,eo,f2," = ",f1-f2)
	elif eo=="*":
		print(f1,eo,f2," = ",f1*f2)
	elif eo=="/":
		print(f1,eo,f2," = ",f1/f2)
	elif eo=="**":
		print(f1,eo,f2," = ",f1**f2)
	elif eo=="*/":
		r=1/2
		print(eo,f1," = ",f1**r)
	else:
		print("Enter valid operator ")
	print('''
		Thank you
		''')