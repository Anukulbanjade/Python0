#Numerical Python(Numpy)
#it is extension of list faster than List

import numpy as np
#Array
a=np.array([1,45,"anukul",67])#,dtype='s') *defining a datatype

print(type(a)) #n dimentional Array 
print(a.dtype)

#dimensions of Array 
aa=np.array([[12,32,41,67],[12,41,63,90]])

print(aa.ndim)  #gives the dimension of array

#accessing the elements of Array
#array[location of array]
#print(cc[0,0,1]) refer to line no 32
#performing operation in array
print(aa[0][1]*aa[1][2])
'''
#Array can be of any size but same number of elements 
'''
bb=np.array([[[12,41,45,63,56],[45,65,28,37,94]],[[45,98,87,78,25],[78,68,64,98,45]]])
print("bb.ndim")
print(bb.ndim)#ndim gives the number of dimension of array
print("printing The shape of Array")
print(bb.shape[0],bb.shape[1],bb.shape[2])
print(bb[1,0,2])


cc=np.array([[[12,41,45,63,56],[45,65,28,37,94]],[[45,98,87,78,25],[78,68,64,98,45]]])

print(cc.size)#gives total size of cc array
print(cc.nbytes)#gives the total number of bytes consume in a memory by this array

'''
Numpy (arrange,reshape,random)
np.arrange()
np.random.permutation()
np.reshape()
'''
#10:01:15
print(np.zeros(9)) #gives array containing zero
print(np.arange(10))#gives the array up to 10
print(np.arange(50,79,2))#get a array from custom number and with step value(jump value ) it is somehow like range()

print(range(10))#its an iterator
print(list(range(10)))#it provides list in this way



#np.random.permutation()
print("np.random.permutation()")

array1=np.arange(1,25)
print(np.random.permutation(array1)) #it randomize the array in suffling way
print(np.random.randint(array1)) #randomize the integer(randominteger)
