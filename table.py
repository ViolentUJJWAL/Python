import time

while True:
    print("Hello TABLE World")
    time.sleep(0.5)
    a = str(input("your name: "))
    t = int(input("Enter no."))
    time.sleep(0.5)
    print("Table of ", t)
    time.sleep(0.5)
    for n in range(1, 11):
        print(t, "*", n, "=", t * n)
        time.sleep(0.5)
    print(
        "___________________________________")
    for x in a:
        print("   ", x)
        time.sleep(0.5)
    print("thankyou")
    time.sleep(0.5) 
    print("made by Violent Ujjwal")
    time.sleep(0.5)

    print("")
