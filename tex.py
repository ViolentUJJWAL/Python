value=int(input("Enter Car Value: "))
carName=input("Car Name: ")
ctTax=value*0.015
stTax=value*0.04
lltyTax=value*0.1
l=['BMW', "MERCEDIS", "AUDI", "FERRARI"]
v=0
for a in l:
	if carName.upper()==a:
		v=1
if v==1:
	totaltax=ctTax+stTax+lltyTax
	totalValue=value+totaltax
	print("tex", totaltax)
	print("yes this is in a list")
	print('Total car value:', totalValue)
else:
	totaltax=ctTax+stTax
	totalValue=value+totaltax
	print("tex", totaltax)
	print('Total car value:', totalValue)
