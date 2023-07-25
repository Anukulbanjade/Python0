#FUNCTIONS

def add_number(a,b):
    add_number=a+b
    print(f"sum of two number is: {add_number}")

def multiply_number(a,b):
    multiply_number=a*b
    print("Multiplication of two number is:",multiply_number)

def divison(a,b):
    """IT performs division of two variable named a,b"""#write the documrntation of function
    divison=a/b
    print("The Division Of two number is: ",divison)

#a=float(input("Enter the first number:  "))
#b=float(input("Enter The Second number: "))

print("*********Enter What you want to Perform******\n")
print("1.ADD")
#add_number(a,b)
print("2.Multiply")
#multiply_number(a,b)
print("3.Division")
#divison(a,b)
print("4.Exit")

#remove comments
# divison? ,help(division)  it shows documentation of division function
#division?? it shows whole code of Functions in Jupyter notebook

def checkargs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b)**c)
    else:
        print("Data Type Error")
#changing the position of argument
checkargs(a=5,c=7,b=9)

checkargs("Ram",45,"r")