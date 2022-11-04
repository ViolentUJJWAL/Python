import random

while True:
    work=input('''
    1 for one time guessing game
    2 for guseeing no. correct game
        -''')
    if work=='1':
        '''one time guessing no.'''
        while True:
            u = input("guess one number 1 to 10 (Q for back) :- ")
            if u=='Q' or u=='q':
                break;
            else:
                u=int(u)
            c = random.randint(1, 10)
            if 0 < u < 11:
                if u == c:
                    print(u, "=", c)
                    print("Both are same")
                elif u < c:
                    print("random no.=", c)
                    print("your guessing no.=", u)
                    print(u, "<", c)
                    print("Your guessing number is smaller than random number ")
                elif u > c:
                    print("random no.=", c)
                    print("your guessing no.=", u)
                    print(u, ">", c)
                    print("Your guessing number is greater than random number ")
                else:
                    print("error")
            else:
                print('''guessing no. is 1 to 10.
your guessing no. is out of range.
                       ''')

    elif work=="2":
        '''guess no. '''
        rguess=random.randint(1,100)
        userguess=None
        guessingtime=0

        while (userguess!=rguess):
            userguess=int(input('Enter guessing number (1 to 100):'))
            if userguess==rguess:
                print('correct guess')
            else:
                if userguess<rguess:
                    print('higher number please')
                else:
                    print('lower number please')
            guessingtime += 1

        print(f'you guessed the number in {guessingtime} guesses')

    else:
        con=input('EXIT Yes/No y/n\n-')
        if con == "yes" or con == 'Y' or con == "y":
            exit()
        else:
            continue;
