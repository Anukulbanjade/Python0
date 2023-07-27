# String Practice
s="python os a best language for data science "
t="in this course we are going to learn python"
print(s+'and '+t)
print(len(s))
print((s.strip()))


#styles of printing
price=120
s="the price of this book"
print(s+" is ",price)
print(s+" is "+str(price))
print(f"{s} is {price}")


#multiline strings
multiline="""Hello it's me anukul i am learning
git and python simultaneously.
now i am working with strings"""
print(multiline)

#indexing and slicing the strings

#Syntax _ s[start:end,stepsize]
print(multiline[7])

print(multiline[2:10])
print(multiline[-1])
print(multiline[-8:-1])
abc=multiline[1:15]
print(abc)
print(abc[::-1]) #reversing the string
#8:05:24
#Continuing 
#.replace function()

a="ABC deFg ;; sadfa QF"
print(a.replace(a[0:5],'EARTH'))
print(a.replace(';','!@#$'))
print(a.replace(';;','!@#$'))

#Split() function
ab='''This is a string ; def; etry;pavd;
    eer45
   ''' 
l=ab.split(";")
print(l[4])

print(a.removesuffix("QF"))
print(a.count("e"))

#in /not in function
str1="helloworldinchina"
print("inch" in str1 )
print("inca" not in str1)

str2="Python"
print("We are Learning %s here"%str2)
print("We are Learning \"string \"here") #here \ denotes don't  touch (" ") so it does not break 
#otherwise
print("We are \n Learning'string' here")

print("C:\name\drive")
#to overcome this issue we use r  it means (raw)
print(r"C:\name\drive")


#there are many functions in python just press .+ TAB in Jupyter Notebook to see available function\n and in vs code if 'a' contains strings just type a.(functions will appear here.)