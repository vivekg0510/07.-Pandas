#!/usr/bin/env python
# coding: utf-8

# # Pandas Practice 01

# ## Pandas Cheat Sheet

# ['General Pandas Cheat Sheet'](https://assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)

# In[1]:


# Exercises


# ## 1.
# 
# In the cell below, create a DataFrame `fruits` that looks like this:
# 
# ![](https://i.imgur.com/Ax3pp2A.png)

# In[2]:


# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.

import pandas as pd
fruits = pd.DataFrame(columns = ["Apples" , "Banana"])
fruits.loc[0] = [30,21]
fruits


# ## 2.
# 
# Create a dataframe `fruit_sales` that matches the diagram below:
# 
# ![](https://i.imgur.com/CHPn7ZF.png)

# In[3]:


# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame(columns = ["Apples" , "Bananas"] , 
             index = ["2017 Sales" , "2018 Sales"],
             data = [   [35,21],[41,34]   ]
             )
fruit_sales


# ## 3.
# 
# Create a variable `ingredients` with a `pd.Series` that looks like:
# 
# ```
# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object
# ```

# In[4]:


ingredients = pd.Series(index = ["Flour", "Milk", "Eggs", "Spam"],
                       data = ["4 cups", "1cup", "2large", "1 can"])

ingredients


# ## 4.
# 
# Read the following csv dataset of wine reviews into a DataFrame called `reviews`:
# 
# ![](https://i.imgur.com/74RCZtU.png)
# 

# In[5]:


import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv")
reviews


# ## 5.
# 
# Run the cell below to create and display a DataFrame called `animals`:

# In[6]:


animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals


# In the cell below, write code to save this DataFrame to disk as a csv file with the name `cows_and_goats.csv`.

# In[7]:


# Your code goes here
animals.to_csv("cows_and_goats")

#for check if the file translate in csv read csv from present working directory
pd.read_csv("cows_and_goats", index_col = "Unnamed: 0")


# ## 6.
# 
# This exercise is optional. Read the following SQL data into a DataFrame called `music_reviews`:
# 
# ![](https://i.imgur.com/mmvbOT3.png)
# 
# The filepath is `../input/pitchfork-data/database.sqlite`. Hint: use the `sqlite3` library. The name of the table is `artists`.

# In[9]:


import sqlite3 as sql

# Read sqlite query results into a pandas DataFrame
con = sql.connect("database.sqlite")
df = pd.read_sql("SELECT * from artists", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())
print(df.shape)

con.close()


# In[ ]:




