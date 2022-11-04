import random


def showlst(lst):
	for a in lst:
		print(a, end="")
	print('')
fruitlst=['APPLE','ORANGE','PAPAYA','GRAPES','MANGO','BANANA']
veglst=['CARROT','POTATO','PUMPKIN','TOMATO','CILLI','ONION']
colorlst=['RED','BLUE','BLACK','YELLOW','GREEN','WHITE']
sportlst=['TENNIS','BOXING','CRICKET','FOOTBALL','HOCKEY','BADMINTON']
animallst=['LION','TIGER','BEAR','MONKEY','ELEPHANT','HORSE']

typelst=[fruitlst,veglst,colorlst,sportlst,animallst]
alllst=[]
for i in typelst:
	for a in i:
		alllst.append(a)
while True:
	print("\n--------|Missing Word|--------")
	start=input('''1 for Start
2 for EXIT
   -> ''')
	if start=='2':
		exit()
	else:
		word=random.choice(alllst)
		saveWord=word
		for i,w in enumerate(typelst):
			if word in w:
				if i==0:
					print('HINT- This is Fruits name')
				elif i==1:
					print('HINT- This is Vegetables name')
				elif i==2:
					print('HINT- This is Colours name')
				elif i==3:
					print('HINT- This is Sports name')
				elif i==4:
					print('HINT- This is Animals name')

		wordlst=[]
		for i in word:
			wordlst.append(i)
		lst=[]
		for e in range(len(wordlst)):
			lst.append('-')

		if len(wordlst)<=4:
			rang=1
		else:
			rang=2
		# showlst(wordlst)
		for i in range(rang):
			reddom_word=''
			while True:
				reddom_word=random.choice(wordlst)
				if reddom_word!="*":
					break;
			index=wordlst.index(reddom_word)
			lst[index]=reddom_word
			wordlst[index]='*'
		# showlst(wordlst)
		gameOver=0
		while True:
			showlst(lst)
			missing=input("Enter Letter: ")
			if missing.upper() in wordlst:
				index=wordlst.index(missing.upper())
				lst[index]=wordlst[index]
				wordlst[index]='*'
				gameOver=0
			else:
				print('Not in this word')
				gameOver=gameOver+1
				print(f"{gameOver} time wronge")
			if gameOver==3:
				print("\nGAME OVER")
				print(f"It's {saveWord}")
				break;
			if "-" not in lst:
				print('Complete the word')
				print(f"It's {saveWord}")
				break;

