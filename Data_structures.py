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