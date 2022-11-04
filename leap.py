while True:	
	try:
		year=int(input("\nYear: "))
		if year%4==0:
			if year%100==0:
				if year%400==0:
					print('____It is a leap year____')
				else:
					print('____It is not a leap year____')
			else:
				print('____It is a leap year____')
		else:
			print('____It is not a leap year____')
	except Exception as e:
		print("Enter only number")