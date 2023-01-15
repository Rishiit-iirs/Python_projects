
# coding: utf-8

# In[1]:

#Sigmoid Function using numpy
import numpy as np

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))


# In[2]:

print(sigmoid(0.5))


# In[3]:

print(sigmoid(1.0))


# In[4]:

x1=1
print("sigmoid activation function on(%.1f)gives %.1f" %(x1,sigmoid(x1)))


# In[5]:

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 200)   
p = sigmoid(x)
plt.xlabel("x") 
plt.ylabel("Sigmoid(x)")  
plt.plot(x, p) 
plt.show()


# In[6]:

X1=np.array([[1,2],[1,1]])


# In[8]:

print(sigmoid(X1))


# In[10]:

X1


# In[11]:

import numpy as np 
import matplotlib.pyplot as plt 
 
inp = np.linspace(-np.pi, np.pi, 24) 
opt = np.sin(inp) 
 
plt.plot(inp, opt, color = 'blue', marker = "o") 
plt.title("numpy.sin()") 
plt.show() 


# In[12]:


input=np.array([-1,0,0.3,0.5,0.6,0.9,1])
print("Input array  :\n",input)


# In[13]:

opt=np.arcsin(input)
print("\n Inverse Sine values:  \n",opt)


# In[35]:




# In[37]:

input=np.array([-1,0,0.3,0.5,0.6,0.9,1])


# In[38]:

print("Input array  :\n",input)


# In[42]:

opt=np.arcsin(input)
print("\n Inverse Sine values: \n",opt)


# In[15]:

#Create an I-D array
arr=[2,4,6,8,10]
# Get the exponential values of multiple elements
arr2=np.exp(arr)
print(arr2)


# In[20]:

#use numpy.exp() to graphical representation
import numpy as np
import matplotlib.pyplot as plt

array=[1,1.2,1.6,1.8,2,3,3.5,4,5,6]
out_array=np.exp(array)
array1=[1,1.2,1.5,1.9,2.4,4.8,5.2,5.8,6,6.5]
plt.plot(array,array1,color='blue',marker="*")

plt.plot(out_array,array1,color='red',marker="o")
plt.title("numpy.exp()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# In[ ]:



