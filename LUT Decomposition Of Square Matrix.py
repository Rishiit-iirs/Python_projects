
# coding: utf-8

# In[1]:

#System Of Linear Equations in python
     #2x+2y+3z+2w=-2
     # 2y+w=0
     # 4x-3y+w=-7   
     # 6x+y-6z-5w=6
import numpy as np


# In[2]:

A=np.array([[2,2,3,2],[0,2,0,1],[4,-3,0,1],[6,1,-6,-5]])
b=np.array([-2,0,-7,6])


# X=np.linalg.solve(A,b)

# In[4]:

X=np.linalg.solve(A,b)
print(X)


# In[6]:

#Solve the above equations using matrix inversion approach
A_inv=np.linalg.inv(A)
X1=np.dot(A_inv,b)


# In[7]:

print(A_inv)

print(X1)


# In[68]:

#Perform the LU Decomposition of the above matrix
from scipy.linalg import lu


# In[16]:

P,L,U=lu(A)
print('P: \n',P)
print('L: \n',L)
print('U: \n',U)
print('LU: \n',np.dot(L,U))


# In[50]:

#Diagonalization of the square matrix
from scipy.linalg import inv,eig


# In[77]:

#Input Square Matrix
P=np.array([[2,2,3,2],[0,2,0,1],[4,-3,0,1],[6,1,-6,-5]])

#Calculate Eigen values and Eigen vectors
evals,evecs=eig(P)


# In[78]:

print(evals)


# In[79]:

print(evecs)


# In[80]:

print(evals)


# In[81]:

print(evecs)


# In[82]:

#Diagonalization of the Square Matrix
#input matrix(4*4)

P=np.array([[2,2,3,2],[0,2,0,1],[4,-3,0,1],[6,1,-6,-5]])
eigen_values,eigen_vectors=eig(P)


# In[83]:

print(eigen_values)


# In[84]:

print(eigen_vectors)


# In[85]:

# Define the Diagonal matrix D using the eigen value array and
# non singular matrix,S as the eigen vector array,finally determining S-inverse
# completes the diagonalization, P=SDS^-1

D=np.array([[eigen_values[0],0,0,0],[0,eigen_values[1],0,0],[0,0,eigen_values[2],0],[0,0,0,eigen_values[0]]])


# In[86]:

S=eigen_vectors
S_inv=inv(S)


# In[87]:

print(S_inv)


# In[88]:

# Verify the result
Z=S.dot(D.dot(S_inv))


# In[89]:

print(Z)


# In[90]:

np.rint(Z)


# In[92]:

np.rint(Z)


# In[91]:

np.abs(Z)


# In[ ]:



