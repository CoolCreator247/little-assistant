
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

except:
     raise Exception("I do not get it")