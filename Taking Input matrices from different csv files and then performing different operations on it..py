
# coding: utf-8

# In[1]:

#Read a matrix A froma csv file and a vector b from another csv file
import numpy as np
import pandas as pd
from scipy.linalg import lu


# In[59]:

A=pd.read_csv("C:/Users/user1/Desktop/matrix_data.csv")


# In[70]:

b=pd.read_csv("C:/Users/user1/Desktop/constant vector.csv")


# In[71]:

print("A:--------------")
print(A)
print("b:---------------")
print(b)


# In[63]:

A


# In[74]:

X=np.array(A)
c=np.array(b.transpose())


# In[75]:

print(X)
print(c)


# In[76]:

Y=np.linalg.solve(X,c)


# In[77]:

print(Y)


# In[78]:

#Solve the above equations using matrix inversion aproach
X_inv=np.linalg.inv(X)
X1=np.dot(X_inv,c)


# In[79]:

print(X_inv)


# In[80]:

print(X1)


# In[81]:

#perform the LU decomposition of the above matrix
P,L,U=lu(X)
print("P: \n",P)
print("L: \n",L)
print("U: \n",U)
print("LU: \n",np.dot(L,U))


# In[82]:

###Diagonalization of the square matrix
from scipy.linalg import inv,eig


# In[83]:

#Input Square Matrix
Q=np.array(X)

#Calculate Eigen values and Eigen vectors
evals,evecs=eig(Q)


# In[84]:

print(evals)


# In[85]:

print(evecs)


# In[91]:

#Define a Diagonal matrix D whose main diagonal elements are eigen values
#and rest of the elenents are zeros
D =np.array([[evals[0],0,0,0],[0,evals[1],0,0],[0,0,evals[3],0],[0,0,0,evals[3]]])


# In[92]:

print(D)


# In[93]:

S=evecs
S_inv=inv(S)


# In[94]:

print(S_inv)


# In[96]:

#verify the result
Z=S.dot(D.dot(S_inv))


# In[97]:

print(Z)


# In[ ]:



