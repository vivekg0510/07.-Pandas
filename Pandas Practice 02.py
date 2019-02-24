#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# This is the workbook component of the "Indexing, selecting, assigning" section.
# 
# Selecting specific values of a pandas `DataFrame` or `Series` to work on is an implicit step in almost any data operation you'll run, so one of the first things you need to learn in working with data in Python is how to go about selecting the data points relevant to you quickly and effectively.
# 
# 
# # Relevant Resources
# [Indexing and Selecting Data](https://pandas.pydata.org/pandas-docs/stable/indexing.html) section of pandas documentation

# In[1]:


import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)
print("Setup complete.")


# In[2]:


reviews.head(2)


# # Exercises

# ## 1.
# 
# Select the `description` column from `reviews` and assign the result to the variable `desc`.

# In[3]:


desc = reviews["description"]


# Follow-up question: what type of object is `desc`? If you're not sure, you can check by calling Python's `type` function: `type(desc)`.

# In[4]:


type(desc)


# ## 2.
# 
# Select the first value from the description column of `reviews`, assigning it to variable `first_description`.

# In[5]:


first_description = reviews.loc[0,"description"]
first_description


# ## 3. 
# 
# Select the first row of data (the first record) from `reviews`, assigning it to the variable `first_row`.

# In[6]:


first_row = reviews["country"]
first_row


# ## 4.
# 
# Select the first 10 values from the `description` column in `reviews`, assigning the result to variable `first_descriptions`.
# 
# Hint: format your output as a `pandas` `Series`.

# In[7]:


first_descriptions = reviews.loc[0:9,"description"]
first_descriptions


# ## 5.
# 
# Select the records with index labels `1`, `2`, `3`, `5`, and `8`, assigning the result to the variable `sample_reviews`.
# 
# In other words, generate the following DataFrame:
# 
# ![](https://i.imgur.com/sHZvI1O.png)

# In[8]:


sample_reviews = reviews.loc[[1,2,3,5,8]]
sample_reviews


# ## 6.
# 
# Create a variable `df` containing the `country`, `province`, `region_1`, and `region_2` columns of the records with the index labels `0`, `1`, `10`, and `100`. In other words, generate the following `DataFrame`:
# 
# ![](https://i.imgur.com/FUCGiKP.png)

# In[9]:


df = reviews.loc[[0,1,10,100],["country", "province", "region_1", "region_2"]]
df


# ## 7.
# 
# Create a variable `df` containing the `country` and `variety` columns of the first 100 records. 
# 
# Hint: you may use `loc` or `iloc`. When working on the answer this question and the several of the ones that follow, keep the following "gotcha" described in the reference.
# 
# > `iloc` uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So `0:10` will select entries `0,...,9`. `loc`, meanwhile, indexes inclusively. So `0:10` will select entries `0,...,10`.
# 
# > [...]
# 
# > ...[consider] when the DataFrame index is a simple numerical list, e.g. `0,...,1000`. In this case `reviews.iloc[0:1000]` will return 1000 entries, while `reviews.loc[0:1000]` return 1001 of them! To get 1000 elements using `iloc`, you will need to go one higher and ask for `reviews.iloc[0:1001]`.

# In[10]:


df = reviews.loc[0:99,["country", "variety"]]
df


# ## 8.
# 
# Create a DataFrame `italian_wines` containing reviews of wines made in `Italy`. Hint: `reviews.country` equals what?

# In[11]:


italian_wines = reviews["country"] == "Italy"
reviews[italian_wines]


# ## 9.
# 
# Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

# In[12]:


mask1 = reviews["points"] <= 95
mask2 = reviews["country"] == "Zealand"
mask3 = reviews["country"] == "Australia"
reviews[mask1 & (mask2 | mask3)]


# In[ ]:




