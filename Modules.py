def sorting_acending(*L):
    L=[]
    for j in range(len(*L)):
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

sorting_acending(5,6,3,2,14,6)