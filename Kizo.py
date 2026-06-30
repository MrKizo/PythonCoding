x=57
print (type (x))

            
print (2 == 4)

myvariable = 10 
print (myvariable) 

Age = 22  
print (Age) 
Name = "Kizo"
print (Name) 
Myname = "kareem"
print (Myname)
My_name = "Kimo"
print (My_name)

print (type (Name))

x = 10  

x= "Kizo" 

print (x)


a,b,c = 1 , 2 , 3 

print (a)
print (b)  
print (c)


print ("kareem\bkoko")

print ("kareem\
       koko\
       kizo")

print ("I love Kimo \\")

# single quote 

print ('I love Kimo 1 \'test\'')

# double quote
print ("I love Kimo too \"test\"")\

#Line Feed

print ("I love kimo\nkizo")

#carriage Return

print ("123456789\rabcdef")

#Horizontal Tab 

print ("kareem\tkoko")

# Character hex value
print ("\x4B\x69\x7a\x6f")

#Concatenation

msg = "I love"
lang = "kizo"

print (msg + " " + lang)

full = msg + " " + lang
print (full)

a= "first\
    second\
    third"  

b= "a \
b \
c"

print (a + " \n " + b)

#Strings

MyStringOne = 'Kareem single quote'
MyStringTwo = "Kareem double quote"
mystringthree = 'Kareem triple "Test"'  
mystringfour = "Kareem triple 'Test'"

print (MyStringOne)
print (MyStringTwo) 
print (mystringthree)
print (mystringfour)

mystringfive = """I 
love "test" 'test'
koko"""
print (mystringfive)

mystringsix = '''I
love "test" 'test'
koko'''  

print (mystringsix)


# Indexing allows us to acess a signle item 
mystring = "I love Kizo"
print (mystring [4])   
print (mystring [-1]) # Starts from the end of the string 

# Slicing allows us to acess multiple items in the string from start to end from 2 => 6 as an example
# last index is not included in the output so always add a number so if you want "6" to be included you 
# have to add 1 to the last index 

mystring = "i love kimo"

print (mystring [2:9]) # it will print from index 2 to 8 and not including 9

print (mystring [0:10]) # if you do not add a start point it automatically starts from 0
# If an end is not added it will go all way to the end automatically
print (mystring [2:]) 
print (mystring [:]) #If you add neither start nor end it will print the whole string

print (mystring [::4])

#---------------------------------

# length is the of the string (len) counts the space as well

A = "i love K"
B = "           i love K"
print (len (A))
print (len (B))

# ---------------------------------

# Strip = removes the spaces from the beginning and the end of the string but not from the middle

# (strip) removes the spaces from them both left and right of the string
# (lstrip) removes the spaces from the left of the string
# (rstrip) removes the spaces from the right of the string
# you can you also remove chars from the output by inputing it in the brackets strip("#")


a = "                i love K                 "


print(a.strip())
print(a.rstrip())
print(a.lstrip())
print (len(a.strip()))

a = "@#@##i love K######"


print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))
print (len(a.strip("@#")))

#---------------

# Title= makes every Word in the start captial and every word after a number captial

b= " I love 3kimo"

print(b.title())

#---------

#Capitalize first word of a senetance capaital does not affect words followed with numbers

c = "i love 3kimo becasue 6he is good"

print (c.capitalize())


#----------

# zfill fills in the zeros so instaed of the number being 1 it becomes 001

c , d ,e , f = "1" , "11" ,"111", "1111"

print(c)
print (d)
print(e)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#----------------

#upper makes all words upper case

a="kareem"

print (a.upper())

#-----------

#lower makes everything lower case

print (a.lower())

#---------

#spilt allows you to split the string into list 2 types 
#By defualt it splits it using space 

#spilt() rsplit()


a = "i love kimo"

print (a.split())

#sperator the "(-)" repalces the space between words


b= "i-love-kimo"
print(b.split("-"))

#Max split allows you to split a certian part of the string can be 1 part 2 or 3 etcdepends 
# on your need allowing to spearte the elements of the string 

c = "i-love kimo-he-is-nice"
print(c.split("-", 2))

#rsplit only splits the right part of the string

d= "i-love-kimo-and-he-is-nice"

print(d.rsplit("-", 2))

#--------------

#Center() allows you to center the stuff you can also add @ or # before it 

a = "kareem"

print(a.center(85))
print(a.center(10 , "@"))
print(a.center(10 , "#"))

#count 

a = "i love kizo and kimo and kizo"

print(a.count("kizo")) # to find out yhe count of the codes

print(a.count("kizo" , 0 , 24)) #To select how many words do you want the output to find

#-----------

#Swap case simply swaps the cases of the letters if its upper makes it lower and vice versa

a= "I love kizo"
b = " i love KizO"

print (a.swapcase())
print (b.swapcase())


#--------

#startswith() allows you to determine the start of the word answers with true or false

a= "kizo is good"

print(a.startswith("k")) #As Kizo Starts with K the answer is true

print(a.startswith("o")) #As Kizo doesnt start with O the answer is false

print(a.startswith("i", 5, 12)) #Allows you to ask about a certain part of the string 


#----

#endswith() confirms the last letter of the last word in the string

a= "kizo is gud"

print(a.endswith("d")) # As gud ends with D the answer is true
print(a.endswith("s" , 0 , 7)) #asks about a certain part about the string

#------------------

#Index(substring , start , end) allows you to locate 1 element in the code itself be it a certian word or a letter

a="i love kimo"
print(a.index("e" , 0 , 6))

#print(a.index("e" , 0 , 5))  #gives an error if the serach target is not found


#find same function but will give -1 if the target was not found

b = " i love kizo"\

print(b.find("love" , 3 , 10)) 

#------------

#rjust(width , fill char on lhe right side) #ljust(width , fill char on lhe left side) just same same as center allows you to center the word but this 
#allows you to fill 

c = "Kareem"

print(c.rjust(11))  

print(c.ljust (11, "#"))  

#------------

#spiltlines() allows you to convert sperated lines back to a list
#you can always add "type" to make sure its converted to the data type you need

e = """Kizo
Kimo
Koko"""

print(e.splitlines())
print(type(e.splitlines()))

#Another method

f= "Kizo\nKizo\nKoko"

print(f.splitlines())

#---------

#Expandtabs() allows you to control the tabs between words "\t" (the space between em)

g= "i\tlove\tkizo"
print(g.expandtabs(22))

#-------------

#print(istitle) check on the type of the data if its tite boleen string etc...

one = "i love kimo and kizo"
two = "I Love Kimo And 3Kizo"


print(one.istitle())
print(two.istitle())

three = " "
four = ""

print(three.isspace())
print(four.isspace())

five = "i love kimo"
six = "I Love Kimo"
print(five.islower())
print(six.islower())

#print(isidentifier) allows you to check if the identifer is the correct  which follows the =
seven = "ilovekizo"
eight = "ilove_kizo"
nine = "i love--kizo"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())


#-------------------------

#(isalpha) allows you to confirm if the letter is from the alphabtics

x = "aaaaaaaaabbbBbbb"
y = "aaaaaaaaabbbBb111bb"

print(x.isalpha())
print(y.isalpha())

#(isalnum) allows you to confrim both alphabits and nums.

z = "aaaaaaaaabbbBb111bb"
l= "aaaaaaaaabbbBb111bb"

print(z.isalnum())
print(l.isalnum())


#-----------------

#replace()

a = "Hello my name is one kareem one one three"

print(a.replace("one" , "KIZO"))

print(a.replace("one" , "KIZO" , 2))

#----------

#join(iterable) allows you to convert list to string

mylist = ["Kimo" , "Kizo" , "Koko"]

print("-" .join(mylist))

print(" " .join(mylist))

print("," .join(mylist))


x = "hello "

y = "kizo"

print(x + y)


msg= "Elzero Web School"

print(msg [::2])

user_input = "###   Gamer123   ###"

print(user_input.strip("#").strip (" "))

order_id = "79"

print(order_id.zfill(5))

code_line = "We use PHP, because PHP is a backend language."

print(code_line.replace ("PHP", "Python"))

title = "elzero web 3school"
print(title.title())
print(title.capitalize())

username = "_Gamer123"

print(username.startswith("_"))

sentence = "Python is an amazing language, and I love Python!"

print(sentence.count ("Python"))

data = "###...loohcS beW orezlE...###"

print(data.strip("#") .strip(".") [::-1] .title())

log_data = "status_code:404-error_type:not_found"

print(type(int(log_data [12 : 15])))

#raw_password = "   ---mySecurePass123---   "

#print(raw_password.strip () .strip("-"))

serial = "79-elzero-2026"

print (serial.replace ("-" , " ").title())

record = "####item_name:gaming_chair_pro####"

print (record. strip ("#").strip("item_name:").replace("_" , " ").title())