#FUNCTIONS

def add_number(a,b):
    add_number=a+b
    print(f"sum of two number is: {add_number}")

def multiply_number(a,b):
    multiply_number=a*b
    print("Multiplicstion of two number is:",multiply_number)

def divison(a,b):
    divison=a/b
    print("The Division Of two number is: ",divison)

a=float(input("Enter the first number:  "))
b=float(input("Enter The Second number: "))

print("*********Enter What you want to Perform******\n")
print("1.ADD")
print(add_number(a,b))
print("2.Multiply")
print("3.Division")
print("4.Exit")

