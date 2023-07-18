#Global Inputs
variable_a=int(input("Enter a first variable: "))
#variable_b=int(input("Enter a Second Variable: "))
# 1. if statement
print("# if Statement")
if variable_a>0:
    print("A is Positive Integer")

# 2.if -else statement
print("# if - else statement")
if variable_a>0:
    print("A is positive Integer")
else:
    print("A is negative Integer")

# 3. Elif statement
print("#elif statement")
if variable_a>0:
    print("A is Positive Integer")
elif variable_a<0:
    print("A is Negative Integer")
elif variable_a==0:
    print("The Integer is Zero")

# 4. IF-ELIF-ELSE

#short hand if
a=10
b=10
print("A is greater than B") if a>b else print("A is equals to B") if a==b else print("B is greater than")

#check grade of student from Marks
marks=float(input("Enter The Marks: "))
if marks>=90:
    print("Congratulations A+ Grade")
elif marks>=80 and marks<90:
    print("Congratulation A Grade")
elif marks>=70 and marks<80:
    print("Great B+ Grade")
elif (marks>=60 and marks<70):
    print("Good, B grade")
elif(marks>=50 and marks<60):
    print("C+ grade, Try to improve")
elif(marks>=40 and marks<50):
    print("C grade, Try to improve")
else:
    print("Sorry You aren't qualified")    