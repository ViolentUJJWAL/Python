num=int(input("enter no. 0 to 999 :-"))
if num<0 or num>999:
    print("invalid no. number enter 0 to 999")
elif num<10:
    print("one digit no.")
elif num<100:
    print("two digit no.")
else:
    print("three digit no.")

