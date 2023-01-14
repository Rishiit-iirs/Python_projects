
# coding: utf-8

# In[6]:

#GaussJordan Elimination method to solve the system of linear Equations
import numpy as np


# In[17]:

def gaussjordan(a,b):
    a=np.array(a,float)
    b=np.array(b,float)
    n=len(b)
    
        #main loop
    for k in range(n):
            #Partial Pivoting
            if np.fabs(a[k,k]) < 1.0e-12:
                for i in range(k+1,n):
                    if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                        for j in range(k,n):
                            a[k,j],a[i,j]=a[i,j],a[k,j]
                        b[k],b[i]=b[i],b[k]
                        break
        #Division of the Pivot row
            pivot = a[k,k]
            for j in range(k,n):
                a[k,j]/=pivot
            b[k]/=pivot     
                # Elimination Loop
            for i in range(n):
                if i==k  or a[i,k]==0: continue
                factor=a[i,k]
                for j in range(k,n):
                    a[i,j] -=factor*a[k,j]
                b[i]-=factor*b[k]
    return b,a


# In[18]:

a=[[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]]
b=[0,-2,-7,6]
X,A=gaussjordan(a,b)


# In[20]:

print("The Solution is: ")
print(X)
print("The Transformed matrix [a]:")
print(A)


# In[ ]:



