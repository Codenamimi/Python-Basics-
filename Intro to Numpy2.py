#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import numpy
import numpy as np


# In[5]:


#create a list 
person_height = [5,5.2,5.5,6.5,7]
person_weight = [60,50,44,55,65]

#create 2 numpy arrays for height and weight
person_height = np.array(person_height)
person_weight = np.array(person_weight)


# In[17]:


person_height
print(person_height)


# In[6]:


person_weight


# In[8]:


sample_list = [101,102,103,104,105,106,107,108,109,110]
numpy.array(sample_list)


# In[14]:


np.array [101,102,103,104,105,106,107,108,109,110]


# In[12]:


(sample_list)array.numpy


# In[11]:


array.numpy [101,102,103,104,105,106,107,108,109,110]


# In[15]:


import numpy as np
array = np.array([4,9,16,25])
type(array)


# In[16]:


sports = ['Cricket', 'Football', 'Tennis', 'Golf', 'Baseball']
sports_new = np.array(sports)
print(sports_new)


# In[18]:


#indexing an array
print(sports_new[1])


# In[22]:


#create an array in multiple dimensions
my_array =np.array([[1,2,3],[5.5,6.5,7],[60,55,65]])
my_array
my_array =np.array([[1,2,3],[5.5,6.5,7],[60,55,65]])


# In[23]:


my_array =np.array([[sports_new],[person_height],[person_weight]])
my_array


# In[29]:


#get element in 3rd row and 2nd column
my_array =np.array([[1,2,3],[5.5,6.5,7],[60,55,65]])
my_array
my_array =np.array([[1,2,3],[5.5,6.5,7],[60,55,65]])
print(my_array[2, 1])


# In[30]:


print(my_array[2],[1])


# In[34]:


#take the 
print(my_array[:3]) 


# In[67]:


#slicing an array: getting a piece of the array
#pick 2,3,4 element in the array

my_array = np.array([101,102,103,104,105,106,107,108,109,110])
my_array
my_array[1:4]


# In[68]:



my_array = np.array[101,102,103,104,105,106,107,108,109,110]
my_array
my_array[1:4]


# In[39]:


#pick the 1st 3 elements
my_array[:3]


# In[40]:


#pick from the 4th elemnt onwards
my_array[3:]


# In[41]:


#pick all elements in the array
my_array[:]


# In[44]:


#multidimensional array
my_array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
my_array


# In[49]:


#select elements on the 2nd row of column 3 & 4
my_array[1:2,2:4]


# In[51]:


#select all rows except the 1st, select column 3 and 4
my_array[1:,2:4]


# In[53]:


#slicing an array:
my_array = ['A', 'B', 'C', 'D', 'E']
#Here, there is an index associated with each element of my_array. The list of indices is given below:0, 1, 2, 3, 4
my_array[1:4]
my_array[1:] #would return ['B', 'C', 'D', 'E']
my_array[:4] #would return ['A', 'B', 'C', 'D']
my_array[:] #would return ['A', 'B', 'C', 'D', 'E']


# In[66]:


#passing logic in arrays
my_array = np.array([1,2,6,48])
new_array = my_array >= 10
new_array


# In[69]:


array1 = np.array([[0,3,2,5],[1,0,2,-2]])
print(array1 >= 3)


# In[70]:


array2 = np.array([[1,3,5],[2,4,6]])
print((array2*2)**2)


# In[71]:


a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b
a + 5


# In[75]:


a=np.arange(10)
a


# In[76]:


b=np.power(a,2)
b


# In[77]:


b.max()


# In[79]:


#concatenation of an array
my_array1 = np.array([1,2,3,4])
my_array2 = np.array([5,6,7,8])
np.concatenate([my_array1,my_array2])


# In[83]:


my_array3 = np.array([[1,2,3,4],[5,6,7,8]])
my_array3


# In[86]:


np.concatenate([my_array3,my_array3])


# In[87]:


#concatenate the array by add columns. when axis =1 means add colums the rows should match, axis=0 default for python, means add rows.
#axis=0 the columns must be equal. dimensions must be similar.
np.concatenate([my_array3,my_array3],axis=1)


# In[88]:


#concatenation of an array
my_array1 = np.array([1,2,3])
my_array2 = np.array([5,6,7,8])
np.concatenate([my_array1,my_array2])


# In[89]:


x = np.array([[3], [5], [7]])
y = np.array([[5], [7], [9]])
np.concatenate([x, y], axis = 1)


# In[90]:


x = np.array([[3], [5], [7]])
x


# In[92]:


x = np.array([[3, 5, 7]])
x


# In[ ]:




