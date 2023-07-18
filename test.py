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