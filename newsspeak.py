while True:
     import requests,json,time 

     def news(url):
          getNews=requests.get(url).text
          news=json.loads(getNews)
          return news

     def speak(str):
           from win32com.client import Dispatch
           speak=Dispatch('SAPI.SpVoice')
           speak.Speak(str)

     def genUrl(content):
          url=''
          if content==1:
               print("Business News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          elif content==2:
               print("Entertainment News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          elif content==3:
               print("Health News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          elif content==4:
               print("Science News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          elif content==5:
               print("Sports News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          elif content==6:
               print("Technology News")
               url="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=bd34c76ad9584cc0a3ef4a562b197b5c"
          
          Tnews=news(url)
          return Tnews


     if __name__== '__main__': 
          try:
               ne=speak('Today News')
               content=input('''\nWELCOME TO NEWS BY VIOLENT_LENOVO
1 for Business
2 for Entertainment
3 for Health
4 for Science
5 for Sports
6 for Technology
Q for EXIT

Choose the Types of News for you hear
- ''')
               if content.lower()=="q":
                    exit()
               elif 0<int(content)<7:
                    numofNews=input('''Enter number of news listening 
(for all news enter all) - ''')
                    if numofNews.lower()=="all":
                         numofNews=100
                    else:
                         numofNews=int(numofNews)
                    print("\nPlease wait Dawnload News....")
                    news=genUrl(int(content))
                    speak("listening carefully")
                    for i,a in enumerate(news["articles"]):
                         today=f"{a['title']}, \nDescription - \n{a['description']}"
                         url=a['url']
                         print(f'\n\nNews {i+1} \n{today}')
                         print(f'URL- {url}')
                         speak(f'News {i+1} {today}')
                         if numofNews==(i+1):
                              break;
                         time.sleep(1)
                    t='''\nThanks for listening News 
     by VIOLENT UJJWAL'''
                    print(t)
                    speak(t)
                    time.sleep(5)
               else:    
                    print("wrong Choose")
          except Exception as e:
               er=f"Error: Something Wrong "
               print(f"\n{er}\n{e}")
               speak(er)
               time.sleep(1)