'''
Boolean and Comparision operator 
1. = =    "is equals to"
2. ! =    "IS NOT EQUALS TO"
3. <      "LESS THAN"
4. >      ""GREATER THAN
5. < =    "LESS THAN OR EQUALS TO"
6. > =    "GREATER THAN OR EQUALS TO"
'''
variable_1=6
variable_2=7
if variable_1 ==variable_2:
    print("equal")

print("Not equal")

new1=True
new2=False
new3=True
print(new1 and new2)
print(new1 and new3)
print(new2 and new1)
print(new1 or new2)
print(new2 or new1)
print(not(new1))

print((new1 and new2)or (new2 and new3))

#some useful functions
#round()
round1=3.141568925
print(round(round1))
print(round(round1,3)) #gives roundoff 3 digits



#divmod()
divmod1=divmod(15,6)
print(divmod1)  #returns quotient and remainder 

print(type(divmod1))     #gives result in tuple
#Acessing the value
print(divmod1[0])
print(divmod1[1])

#isinstance()
print(isinstance(6,int))    #isinstance() check the value is specific data type or not here in this line of code it is checking 6 is int or not and returns it in bool format


#pow(x,y,z)  x raise to y and modulus z
print(pow(2,4,)) 

print(2**6)

#input function
first_name=input(str("Enter your First name: "))
last_name=input(str("Enter Your Last Name:  "))
print(f"Your name is {first_name} {last_name}")

