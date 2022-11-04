import time

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch('SAPI.SpVoice')
    speak.Speak(str)

class Su:
    def suma(self,a,b):
        return a+b
class mu(Su):
    def mult(self,a,b):
        return a*b
class di(mu):
    def div(self,a,b):
        return a/b

    def t(a):
        time.sleep(a)
while True:
    r=int(input('''1 for Chai
2 for coffee
3 for maggi
enter food cord :'''))
    p=int(input("Enter no, of people :-"))
    if r==1:
        obj=di()
        x=di.div("self",p,2)
        lst=["Recipes of Chai",f"step 1 - Boil {di.div('self',p,2)} cup of water",f"step 2 - Add {di.mult('self',p,0.5)} teaspoon Sugar",f"step 3 - Add {p} teaspoon chai patti"
        ,f"step 4 - Add grated Ginger",f"step 5 - Simmer for 3 and 4 mins. on medium flame ",f"step 6 - Add {x+0.5} cup of milk",
        f"step 7 - Simmer for 3 and 4 mins. on medium flame ",'''Switch off flame. stain the tea a mesh strainer 
    pour onto glasses and cups.''',"Enjoy homemade tea"]
        for i in lst:
            print(i)
            speak(i)
            di.t(1)
        print("THANKS FOR USE")
        di.t(1)
    elif r==2:
        obj = di()
        cp=di.suma("self",p,0.5)
        cs=obj.mult(p,1)
        lst=["Recipes of Coffee",f"step 1 - In a cup take {cp} teaspoons instant coffee.","step 2 - Add 3 tablespoons hot water",
        f"step 3 - Add {cs} teaspoons of sugar",f"step 4 - first mix the coffee and sugar with water",'''step 5 - Then being to stir briskly and beat coffee for 3 and 4 minutes.
        you can a break after 2 minutes and then continue it your hands start aching.''','''step 6 - beat the coffee till its color lightens and see a forthy on top.''',
        f"step 7 - Then take {p} cup of milk in a pan and on a medium to high flame boil it.",'''step 8 - adding 1/2 of milk to the coffee stir with spoon. you can even move 
        the cop so that the milk get mixed with coffee.''',"step 9 - Add remaining milk with frothy layer also","step 10 - Serve the coffee on glasses and cups.","Enjoy homemade hot coffee"]
        for i in lst:
            print(i)
            speak(i)
            di.t(1)
        print("THANKS FOR USE")
        di.t(1)
    elif r==3:
        obj = di()
        lst=["Recipes of maggi",f"step 1 - add {p} cup of water and get to a boil.",f"step 2 - then add {p} pack maggi noodle",f"step 3 - and add {p} pack of maggi masala.",
        "step 4 - mix well and boil for 2 minutes or until noodles are cooked well.","step 5 - serve the maggi on bowls","Enjoy homemade maggi"]
        for i in lst:
            print(i)
            speak(i)
            di.t(1)
        print("THANKS FOR USE")
        di.t(1)
    else:
        lst=["data not available","TRY AGAIN"]
        for i in lst:
            print(i)
            speak(i)
            di.t(1)
    print("")