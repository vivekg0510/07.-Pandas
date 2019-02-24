#!/usr/bin/env python
# coding: utf-8

# # DataFrame
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame
Potentially columns are of different types
Size – Mutable
Labeled axes (rows and columns)
Can Perform Arithmetic operations on rows and columns
# In[33]:


# Importing pandas as numpy with alias
import pandas as pd
import numpy as np


# In[35]:


# A pandas DataFrame can be created using the following constructor −


# pd.DataFrame( data, index, columns, dtype, copy)
Sr.No       Parameter & Description
1           data  ---   data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
2           index ---   For the row labels, the Index to be used for the resulting frame is Optional Default np.arrange(n) if no index is passed.
3           columns --- For column labels, the optional default syntax is - np.arrange(n). This is only true if no index is passed.
4           dtype ---   Data type of each column.
5           copy  ---   This command (or whatever it is) is used for copying of data, if the default is False.Create DataFrame
A pandas DataFrame can be created using various inputs like −

Lists
dict
Series
Numpy ndarrays
Another DataFrame
In the subsequent sections of this chapter, we will see how to create a DataFrame using these inputs.
# # Create an Empty DataFrame
# ## A basic DataFrame, which can be created is an Empty Dataframe.

# ## Example

# In[36]:


#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
print (df)


# ## Create a DataFrame from Lists
# The DataFrame can be created using a single list or a list of lists.

# ## Example 1

# In[37]:


import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)


# ## Example 2

# In[38]:


import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)


# ## Example 3

# In[39]:


import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print (df)


# In[40]:


# Note − Observe, the dtype parameter changes the type of Age column to floating point.


# # Create a DataFrame from Dict of ndarrays / Lists
All the ndarrays must be of same length. If index is passed, then the length of the index should equal to the length of the arrays.
If no index is passed, then by default, index will be range(n), where n is the array length.
# ## Example 1

# In[41]:


import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)

Note − Observe the values 0,1,2,3. They are the default index assigned to each using the function range(n).
# ## Example 2

# In[42]:


import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

Note − Observe, the index parameter assigns an index to each row.
# # Create a DataFrame from List of Dicts
List of Dictionaries can be passed as input data to create a DataFrame. The dictionary keys are by default taken as column names.
# ## Example 1
# The following example shows how to create a DataFrame by passing a list of dictionaries.

# In[43]:


import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)


# In[44]:


#Note − Observe, NaN (Not a Number) is appended in missing areas.


# ## Example 2
# The following example shows how to create a DataFrame by passing a list of dictionaries and the row indices.
# 

# In[45]:


import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
print (df)


# ## Example 3
# The following example shows how to create a DataFrame with a list of dictionaries, row indices, and column indices.
# 

# In[46]:


import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print (df1)
print (df2)


# Note − Observe, df2 DataFrame is created with a column index other than the dictionary key; thus, appended the NaN’s in place. Whereas, df1 is created with column indices same as dictionary keys, so NaN’s appended.

# # Create a DataFrame from Dict of Series

# Dictionary of Series can be passed to form a DataFrame. The resultant index is the union of all the series indexes passed.

# ## Example

# In[47]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)


# Note − Observe, for the series one, there is no label ‘d’ passed, but in the result, for the dlabel, NaN is appended with NaN.
# Let us now understand column selection, addition, and deletion through examples.
# 

# ## Column Selection

# We will understand this by selecting a column from the DataFrame.

# ## Example

# In[48]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df ['one'])


# In[49]:


# Column Addition
# We will understand this by adding a new column to an existing data frame.


# ## Example

# In[50]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print (df)

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print (df)


# In[51]:


# Column Deletion
# Columns can be deleted or popped; let us take an example to understand how.


# ## Example

# In[52]:


# Using the previous DataFrame, we will delete a column
# using del function
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print ("Our dataframe is:")
print (df)

# using del function
print ("Deleting the first column using DEL function:")
del df['one']
print (df)

# using pop function
print ("Deleting another column using POP function:")
df.pop('two')
print (df)


# # Row Selection, Addition, and Deletion
# We will now understand row selection, addition and deletion through examples. Let us begin with the concept of selection.
# 

# ## Selection by Label
# Rows can be selected by passing row label to a loc function.
# 

# In[53]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df.loc['b'])


# The result is a series with labels as column names of the DataFrame. And, the Name of the series is the label with which it is retrieved.

# # Selection by integer location
# Rows can be selected by passing integer location to an iloc function.
# 

# In[54]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.iloc[2]


# ## Slice Rows
# Multiple rows can be selected using ‘ : ’ operator.
# 

# In[55]:


import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df[2:4])


# ## Addition of Rows
# Add new rows to a DataFrame using the append function. This function will append the rows at the end.

# In[56]:


import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print (df)


# # Deletion of Rows
# Use index label to delete or drop rows from a DataFrame. If label is duplicated, then multiple rows will be dropped.
# If you observe, in the above example, the labels are duplicate. Let us drop a label and will see how many rows will get dropped.
# 

# In[57]:


import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print (df)


# In[1]:


# In the above example, two rows were dropped because those two contain the same label 0.


# # Used Terminal Features In Jupyter-Notebook

# In[3]:


#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import os
os.chdir("/home")
os.getcwd()


# In[4]:


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# In[ ]:




