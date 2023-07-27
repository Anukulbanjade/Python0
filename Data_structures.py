#https://imgur.com/a/Q4IZCZg
# LIST TUPLE SET DICTIONARY
'''
***TSL***
1.List                L=[1,23,"Anukul",27]
2.Tuple               T=(2,34,"anukul",23)
3.Set                 S={12,34,"Anukul"}
4. Dictionary         D={'name':'Anukul','age':22}
'''
l=[12,77,"Anukul",45]
t=(14,15,"Banjade",67)
s={45,21,"PMC",98}
d={
    "name":"Anukul",
    "Age":"22",           #'key':'Value'
    'Campus':'PMC'
}

#printing
print(t)
print(s)
print(l)
print(d)


print(type(l))
print(type(t))
print(type(s))
print(type(d))

#Acessing the element
print(l[2])
print(t[2])
print(2 in s)       #we get result in bool
print(d['Age'])  #we have to find value only from Key



print(l[-1:])
print(l[::-1]) #reversing the List

print(t[::-1])
print(t[1:4])

#adding the value to the data structure
l.append(10)  #add element to the EOL
print(l)
l[2]=78   #replaces the elements of List
print(l)
print("deleting the elements from the list")
del l[2]
print(l)

#tuple is immutable , to update the value we have to typecast tuple to list
t1=(98,55)
t1=t+t1
print("tuple t2")
print(t1)

#set can be added by update(),add()
print("removing the elements from the set")
print(s)
s.remove('PMC')
print(s)


#adding the data to the dictionary
d['temp']=17
print(d)
#removal of elements from dic
del d["temp"]
print(d)

#concatenation of Dic
d2={
    "name":"ram",
    "Age":15,
    "Campus":"PK"
    }
#print(d2+d) we cannot add two dictionary

#we can delete  all datastructures by del function
# remove(),pop()etc

 