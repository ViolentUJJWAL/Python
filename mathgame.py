import time

while True:
    c = int(input('''
    1 start game
    2 exit
    '''))
    if c == 1:
        e1 = int(input("Enter no. (only 1111 to 8000):- "))
        if 1111 <= e1 <= 8000:
            a = e1+20000-2
            print("prediction is ", a)
            e2 = int(input("Enter no. (only 1111 to 8000):- "))
            if 1111 <= e2 <= 8000:
                b = 9999-e2
                print("random no.:- ", b)
                e3 = int(input("Enter no. (only 1111 to 8000):- "))
                if 1111 <= e3 <= 8000:
                    c = 9999-e3
                    print("random no.:- ", c)
                    print("")
                    print("Next see magic")
                    print("Prediction is ", a)
                    print("")
                    print("Calculate")
                    time.sleep(0.5)
                    print("1st enter no.:+", e1)
                    time.sleep(0.5)
                    print("2nd enter no.:+", e2)
                    time.sleep(0.5)
                    print("random no.:   +", b)
                    time.sleep(0.5)
                    print("3rd enter no.:+", e3)
                    time.sleep(0.5)
                    print("random no.:   +", c)
                    time.sleep(0.5)
                    print("total:-       ", e1+e2+b+e3+c)
                    time.sleep(0.5)
                    print("total = prediction")
                    time.sleep(0.5)
                    print(e1+e2+b+e3+c, "=", a)
                    time.sleep(0.5)
                    print('''
                            Thank you
                            made by ViolentUJJWAL''')
                else:
                    print("no. is out of range lol")
            else:
                print("no. is out of range lol")
        else:
            print("no. is out of range lol")
    elif c == 2:
        print('''
        Thank you
        made by ViolentUJJWAL''')
        break
    else:
        print('''
        enter only 1 and 2)
        1 for start game
        2 for exit
        ''')

