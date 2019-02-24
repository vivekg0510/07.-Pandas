#!/usr/bin/env python
# coding: utf-8

# # Series
Series is a one-dimensional labeled array capable of holding data of any type 
(integer, string, float, python objects, etc.). 
The axis labels are collectively called index.pandas.Series
A pandas Series can be created using the following constructor −
pandas.Series( data, index, dtype, copy)The parameters of the constructor are as follows −


Sr.No                Parameter & Description
  1           data  --- data takes various forms like ndarray, list, constants
  2           index --- Index values must be unique and hashable, same length as data. Default np.arrange(n) if no index is passed.
  3           dtype --- dtype is for data type. If None, data type will be inferred
  4           copy  --- Copy data. Default False

A series can be created using various inputs like −

Array
Dict
Scalar value or constant

# # Create an Empty Series
# 
A basic series, which can be created is an Empty Series.
# In[1]:


#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series()
print(s)


# # Create a Series from ndarray
# 
If data is an ndarray, then index passed must be of the same length. If no index is passed, then by default index will be range(n) where n is array length, i.e., [0,1,2,3…. range(len(array))-1].
# In[2]:


data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)

We did not pass any index, so by default, it assigned the indexes ranging from 0 to len(data)-1, i.e., 0 to 3.
# In[3]:


data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)

We passed the index values here. Now we can see the customized indexed values in the output.
# # Create a Series from dict
A dict can be passed as input and if no index is specified, then the dictionary keys are taken in a sorted order to construct index. If index is passed, the values in data corresponding to the labels in the index will be pulled out.
# In[4]:


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)

Observe − Dictionary keys are used to construct index.
# In[5]:


data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print (s)

Observe − Index order is persisted and the missing element is filled with NaN (Not a Number).
# # Create a Series from Scalar
If data is a scalar value, an index must be provided. The value will be repeated to match the length of index
# In[6]:


s = pd.Series(5, index=[0, 1, 2, 3])
print (s)


# # Accessing Data from Series with Position
Data in the series can be accessed similar to that in an ndarray.
# ## Example 1
Retrieve the first element. As we already know, the counting starts from zero for the array, which means the first element is stored at zeroth position and so on.
# In[7]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first element
print (s[0])


# ## Example 2
Retrieve the first three elements in the Series. If a : is inserted in front of it, all items from that index onwards will be extracted. If two parameters (with : between them) is used, items between the two indexes (not including the stop index)
# In[8]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first three element
print (s[:3])


# ## Example 3

# In[9]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the last three element
print (s[-3:])


# # Retrieve Data Using Label (Index)
A Series is like a fixed-size dict in that you can get and set values by index label.
# ## Example 1

# In[10]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# retrieve a single element using index label value
print (s['a'])


# ## Example 2

# In[11]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
# Retrieve multiple elements using a list of index label values.
print (s[['a','c','d']])


# ## Example 3

# In[12]:


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#If a label is not contained, an exception is raised.
print (s['f'])


# In[13]:


#import the pandas library and aliasing as pd
import pandas as pd

stu=["ram","raj","Amrit","Vivek"]
stu=[True,False,True,False]
s = pd.Series(stu)
print(s)


# In[14]:


#import the pandas library and aliasing as pd
import pandas as pd
stu={1:"Amrit" , 2:"Rajesh" , 3:"Vishwajeet" , 4:"Sheshmani"}
pd.Series(stu)


# In[15]:


#import the pandas library and aliasing as pd
import pandas as pd

stu=["ram","raj","Amrit","Vivek"]
s = pd.Series(stu)
print(s)


# In[ ]:




