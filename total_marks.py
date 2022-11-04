import time,math

def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch('SAPI.SpVoice')
      speak.Speak(str)

a = input("Enter you name :- ")
print("Dear"+" "+a)
speak(f'Dear {a}')
time.sleep(0.5)
print("BEST OF LUCK")
speak('BEST OF LUCK')
time.sleep(0.5)
print("Enter your marks")
speak('Enter your marks')
time.sleep(0.5)
speak('English')
e = int(input("English ="))
time.sleep(0.5)
if 30 > e >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= e <= 100:
    print("next subject")
else:
    print("Enter valid number")
time.sleep(0.5)
speak('Hindi')
h = int(input("Hindi ="))
time.sleep(0.5)
if 30 > h >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= h <= 100:
    print("next subject")
else:
    print("Enter valid number")
time.sleep(0.5)
speak('Maths')
m = int(input("Maths ="))
time.sleep(0.5)
if 30 > m >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= m <= 100:
    print("next subject")
else:
    print("Enter valid number")
time.sleep(0.5)
speak('Science')
s = int(input("Science ="))
time.sleep(0.5)
if 30 > s >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= s <= 100:
    print("next subject")
else:
    print("Enter valid number")
time.sleep(0.5)
speak('SSt')
ss = int(input("SSt ="))
time.sleep(0.5)
if 30 > ss >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= ss <= 100:
    print("next subject")
else:
    print("Enter valid number")
time.sleep(0.5)
speak('Computer')
c = int(input("Computer ="))
time.sleep(0.5)
if 30 > c >= 0:
    print("sorry you are fail in this subject")
    speak('sorry you are fail in this subject')
elif 30 <= c <= 100:
    print("and")
else:
    print("Enter valid number")
time.sleep(0.5)
total = e+h+m+s+ss+c
if 0 <= total <= 600 and 0 <= e <= 100 >= h >= 0 <= m <= 100 >= s >= 0 <= ss <= 100 >= c >= 0:
    d = total/600
    per = math.floor(d*100)
    print("Total Marks is ", total)
    speak(f'Total Marks is {total}')
    time.sleep(0.5)
    print("your percentage is ", per,"%")
    speak(f'your percentage is {per}')
    time.sleep(0.5)
    if per >= 61:
        print("you are pass first division")
        speak('you are pass first division')
    elif per >= 45:
        print("you are pass second division")
        speak('you are pass second division')
    elif per >= 30:
        print("you are pass third division")
        speak('you are pass third division')
    else:
        print("you are fail try again next year")
        speak('you are fail try again next year')
else:
    print("invalid entry check your number and then enter ")
tf = input("Feedback : ")
time.sleep(0.5)
print("Thankyou dear", a, "have a nice day")
speak(f'Thankyou dear {a} have a nice day')
