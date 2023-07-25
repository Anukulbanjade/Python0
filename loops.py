#Loops in python
# 1.while Loop
print("1. While Loops")
n=int(input("Enter The number: "))
i=0
while i<n:
    print(i)
    i+=1
print("Finished Iteration") 

#Example of While Loops
Input1=int(input("Enter the number you want to perform multiplication: "))
print(f"The multiplication table of {Input1}  is ")
j=1
while j<=10:
    print(Input1*j)
    j+=1

'''
 USE of Pass statement  just skips it

while i<n:
    if i%2==0:
    print(i)
else:
    pass
i+=1
print("Done)
 
'''
#Example of Pass Statement

"""
** Break statement immediately exit from function
break statement:

When the break statement is encountered inside a loop, it immediately terminates the loop execution, regardless of the loop's condition.
It allows you to exit the loop prematurely when a certain condition is met.
After encountering break, the program execution continues with the statement immediately following the loop.
Here's an example that uses break in a while loop:
"""
#Example:
i = 0
while i < 10:
    print(i)
    if i == 5:
        break  # Terminates the loop when i reaches 5
    i += 1



"""
**Continue statement

The continue statement is used to skip the remaining statements in the current iteration of a loop and move to the next iteration.
It is useful when you want to bypass specific iterations but continue the loop's execution.
After encountering continue, the program skips the rest of the loop's body and proceeds with the next iteration.
"""
#Example:
L=[]
for i in range(10):
    print(i+1)
    L.append(i**2)
    #4:46:40

s={"apple",4.9,"cherry",}
i=1
for x in s:
    print(x)
    i+=1
    if i==3:
        break
else:
    print("Loop Completes its iteration")

#dictionary
D={"apple":44,"cherry":"game"}          #"key":"Value"
for x in D:
    print(x,D[0])

"""
IMPORTANT NEED TO Study later

Given a list of number i.e.[1,2,3,4,-5,7,9,3,2] , make another list of number that contains all the items in sorted order from min to max . i.e . your result will be another list in acending order 
"""
L=[1,2,3,4,-5,7,9,3,2]
for j in range(len(L)):
    m=L[j]
    idx=j
    c=j
    for i in range(j,len(L)):
        if L[i]<m:
            m=L[i]
            idx=c
        c+=1
    tmp=L[j]
    L[j]=m
    L[idx]=tmp
print(L)
