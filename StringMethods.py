#1 Python String capitalize() Method
txt = "this is a python program."

x = txt.capitalize()

print (x)

#2 Python String casefold() Method

txt = "This is A Python Code!"

x = txt.casefold()

print(x)

#3 Python String center() Method
txt = "Spyder"

x = txt.center(20)

print(x)

#4 Python String count() Method
txt = "Italy are out of the World Cup"

x = txt.count("Cup")

print(x)


#5 Python String encode() Method
txt = "I won the race"

x = txt.encode()

print(x)


#6 Python String endswith() Method
txt = "India is a country."

x = txt.endswith(".")

print(x)


#7 Python String expandtabs() Method
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)


#8 Python String find() Method
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)


#9 Python String format() Method
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#10 Python String index() Method
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


#11 Python String isalnum() Method
txt = "Company12"

x = txt.isalnum()

print(x)


#12 Python String isalpha() Method
txt = "CompanyX"

x = txt.isalpha()

print(x)


#13 Python String isdecimal() Method
txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)


#14 Python String isdecimal() Method
txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x) 


#15 Python String isdigit() Method
txt = "50800"

x = txt.isdigit()

print(x) 


#16 Python String isidentifier() Method
txt = "Demo"

x = txt.isidentifier()

print(x) 


#17 Python String islower() Method
txt = "hello world!"

x = txt.islower()

print(x) 


#18 Python String isnumeric() Method
txt = "565543"

x = txt.isnumeric()

print(x) 


#19 Python String isprintable() Method
txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x) 


#20 Python String isspace() Method
txt = "   "

x = txt.isspace()

print(x)



#21 Python String istitle() Method
txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x) 


#22 Python String isupper() Method
txt = "THIS IS NOW!"

x = txt.isupper()

print(x) 


#23 Python String join() Method
myTuple = ("Spain", "Germany", "France")

x = "#".join(myTuple)

print(x) 


#24 Python String ljust() Method
txt = "Madrid"

x = txt.ljust(20)

print(x, "is the capital of Spain.") 


#25 Python String lower() Method
txt = "CMON YOU GUNNERS"

x = txt.lower()

print(x) 


#26 Python String lstrip() Method
txt = "     mango     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


#27 Python String maketrans() Method
txt = "Information Tech!"
mytable = txt.maketrans("T", "M")
print(txt.translate(mytable))


#28 Python String partition() Method
txt = "Who will win today?"

x = txt.partition("win")

print(x) 


#29 Python String replace() Method

txt = "I will lose today"

x = txt.replace("lose", "win")

print(x)


#30 Python String rfind() Method

txt = "Hala Madrid la decima."

x = txt.rfind("la")

print(x)


#31 Python String rindex() Method
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x) 


#32 Python String rjust() Method
txt = "Liverpool"

x = txt.rjust(20)

print(x, "won the league.")


#33 Python String rpartition() Method
txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x) 


#34 Python String rsplit() Method
txt = "City,Liverpool,Arsenal"

x = txt.rsplit(", ")

print(x)



#35 Python String rstrip() Method
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite") 


#36 Python String splitlines() Method
txt = "The man shot the can\nHE won the game"

x = txt.splitlines()

print(x) 


#37 Python String startswith() Method
txt = "Hello, I am Shelby."

x = txt.startswith("Hello")

print(x)


#38 Python String startswith() Method
txt = "Hello, welcome home Shelby."

x = txt.startswith("welcome")

print(x)


#39 Python String swapcase() Method
txt = "Hi Thank You for the TEA"

x = txt.swapcase()

print(x) 


#40 Python String title() Method
txt = "You will never walk alone"

x = txt.title()

print(x)



#41  Python String translate() Method
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#42 Python String upper() Method
txt = "Hello my friends"

x = txt.upper()

print(x)


#43 Python String zfill() Method

txt = "99"

x = txt.zfill(10)

print(x) 
