
# coding: utf-8

# In[47]:

#System Of Linear Equations in python
     # 8x+3y-2z=9
     #-4x+7y+5z=15
     # 3x+4y-12z=35   

import numpy as np



# In[3]:

A=np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
b=np.array([9,15,35])


# In[4]:

X=np.linalg.solve(A,b)


# In[5]:

print(X)


# In[6]:

#Solve the above equations using matrix inversion approach
A_inv=np.linalg.inv(A)
X1=np.dot(A_inv,b)


# In[7]:

print(X1)


# In[8]:

#Perform the LU Decomposition of the above matrix
from scipy.linalg import lu


# In[9]:

P,L,U=lu(A)
print('P: \n',P)
print('L: \n',L)
print('U: \n',U)
print('LU: \n',np.dot(L,U))


# In[10]:

#Diagonalization of the square matrix
from scipy.linalg import inv,eig


# In[11]:

#Input Square Matrix
P=np.array([[8,3,-2],[-4,7,5],[3,4,-12]])

#Calculate Eigen values and Eigen vectors
evals,evecs=eig(P)


# In[12]:

evals


# In[13]:

evecs


# In[32]:

print(evals)


# In[33]:

print(evecs)


# In[34]:

#Diagonalization of the Square Matrix
#input matrix(3*3)

P=np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
eigen_values,eigen_vectors=eig(P)


# In[35]:

print(eigen_values)


# In[36]:

print(eigen_vectors)


# In[37]:

# Define the Diagonal matrix D using the eigen value array and
# non singular matrix,S as the eigen vector array,finally determining S-inverse
# completes the diagonalization, P=SDS^-1

D=np.array([[eigen_values[0],0,0],[0,eigen_values[1],0],[0,0,eigen_values[2]]])


# In[38]:

S=eigen_vectors
S_inv=inv(S)


# In[39]:

print(S_inv)


# In[40]:

# Verify the result
Z=S.dot(D.dot(S_inv))


# In[41]:

print(Z)


# In[42]:

np.rint(Z)


# In[46]:

np.rint(Z)


# In[ ]:



