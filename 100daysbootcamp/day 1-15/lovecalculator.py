print("""Love calculator system
This system ask the name of the couple
and check whether they are true love or not
      based on the checking of their name with true love 
      and generating percentage of their love
      """)

boy = str(input("\nEnter boy Name: "))
girl = str(input("Enter girl Name: "))
name = boy + girl
name  =name.lower()

#true count
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t + r + u + e

# love count
l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e

percent = str(true) + str(love)
percent  =int(percent)
if percent<10 or percent>90:
    print(f" Your score is {percent}, and you go together like coke and mentos")
elif percent>40 and percent<50:
    print(f" Your score is {percent}, and you two are alright")
else:
    print(f"YOur score is {percent}")