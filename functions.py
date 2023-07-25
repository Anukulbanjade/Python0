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

def r():
    x=9
    y=10
    z="HP"
    return x,y,z      #only returned values are acessiable outside the function it can return multiple values

q,w,e=r()
print(q,w,e)

#arbitary number of argument in functions
def sum(*args):     # (*args) takes any number of argument
    sum=0
    for i in range(len(args)):
        sum+=args[i]
    return sum


print(sum(4,6,8,9.54))

#multiplication for arbitary number of variable
def multiplication(*abc):
    mul=1
    for i in range(len(abc)):
        mul=abc[i]*mul
    return print(mul)

multiplication(2,4,8)


#default values in Function
def default(defaultsum=0):
    print(defaultsum)

default(4)