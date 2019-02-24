#!/usr/bin/env python
# coding: utf-8

# # Summary functions and maps workbook
# 
# ## Introduction
# 
# This is the workbook component to the "Summary functions and maps" section of the Advanced Pandas tutorial. 
# 
# In the last section we learned how to select relevant data out of our `pandas` `DataFrame` and `Series` objects. Plucking the right data out of our data representation is critical to getting work done, as we demonstrated in the visualization exercises attached to the workbook.
# 
# However, the data does not always come out of memory in the format we want it in right out of the bat. Sometimes we have to do some more work ourselves to reformat it for the task at hand.
# 
# The remainder of this tutorial will cover different operations we can apply to our data to get the input "just right". We'll start off in this section by looking at the most commonly looked built-in reshaping operations. Along the way we'll cover data `dtypes`, a concept essential to working with `pandas` effectively.

# In[1]:


import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
reviews.head()


# ## Exercises

# ## 1.
# 
# What is the median of the `points` column in the `reviews` DataFrame?

# In[2]:


median_point = reviews["points"].median()
median_point


# ## 2. 
# What countries are represented in the dataset? (Your answer should not include any duplicates.)

# In[3]:


reviews.sort_values('country' , ascending =True , inplace = True)
reviews = reviews.dropna(subset = ["country"],how = 'any')
reviews = reviews.drop_duplicates(subset = ["country"], keep = 'first')
list_Countries = list(reviews["country"])
list_Countries


# In[4]:


len(list_Countries)


# ## 3.
# How often does each country appear in the dataset? Create a Series `reviews_per_country` mapping countries to the count of reviews of wines from that country.

# In[5]:


reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
reviews.head()
reviews_per_country = reviews['country'].value_counts()
reviews_per_country


# ## 4.
# Create variable `centered_price` containing a version of the `price` column with the mean price subtracted.
# 
# (Note: this 'centering' transformation is a common preprocessing step before applying various machine learning algorithms.) 

# In[6]:


centered_price = reviews['price'].mean()
centered_price


# ## 5.
# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable `bargain_wine` with the title of the wine with the highest points-to-price ratio in the dataset.

# In[7]:


reviews.head(2)


# In[8]:


mask1 = (reviews['points'] / reviews ['price']).idxmax()
bargain_wine = reviews['title'].loc[mask1]
bargain_wine


# ## 6.
# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series `descriptor_counts` counting how many times each of these two words appears in the `description` column in the dataset.

# In[9]:


mask1 = reviews.description.map(lambda lo: 'tropical' in lo)
tropical = mask1.sum()

mask2 = reviews.description.map(lambda lo: 'fruity' in lo)
fruity = mask2.sum()

descriptor_counts = pd.Series(    [tropical, fruity]     ,  index=['tropical','fruity']     )
descriptor_counts


# ## 7.
# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# 
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
# 
# Create a series `star_ratings` with the number of stars corresponding to each review in the dataset.

# In[10]:


def stars(lines):
    stars = 0
    if 'Canada' == lines.country:
        stars= 3
    elif lines.points >= 95:
        stars= 3
    elif lines.points >= 85:
        stars= 2
    else:
        stars= 1
    return stars

star_ratings = reviews.apply(stars, axis='columns')
star_ratings


# In[ ]:




