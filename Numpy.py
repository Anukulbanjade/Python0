#Numerical Python(Numpy)
#it is extension of list faster than List

import numpy as np
#Array
a=np.array([1,45,"anukul",67])#,dtype='s') *defining a datatype

print(type(a)) #n dimentional Array 
print(a.dtype)
aa=np.array([[12,32,41,67],[12,41,63,90]])
print(aa.ndim)
bb=np.array([[[12,41,45,63,56],[45,65,28,37,94]],[[45,98,87,25,34],[78,68,64,98,45]]])
print(bb.ndim)
print(bb.shape[0],bb.shape[1],bb.shape[2])
print(bb[1,0,2])
