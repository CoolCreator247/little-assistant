
print("Hi, my name is little assistant ")   
print("I am here to help")
print("you can tell or ask me to go to google")
print("╭(◔ ◡ ◔)/ ")

try:
    reply = input()
# input = reply 
    if reply == "I am happy":
        print("I am too")
    elif reply == "I am sad":
        print("Sorry are you ok")
        print("Why are you sad?")
        input(">")
        print("interesting ")
    elif reply == "Are you happy":
        print("I am happy thanks for asking")

    elif reply == "go to google":
 import urllib.request
 webUrl  = urllib.request.urlopen('https://www.google.com/search?q=python&rlz=1CABASQ_enUS940&oq=python&aqs=chrome.0.69i59j35i39j0i433i512j69i60l2j69i61j69i60l2.2305j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on')
 print ("result code: " + str(webUrl.getcode()))  
 data = webUrl.read()
 print(data)

except:
     raise Exception("I do not get it")