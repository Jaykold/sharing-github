#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1 solution to word problems on Four Operations
total_population = 198568
no_of_men = 45312
no_of_women = 35678
no_of_children = (total_population - (no_of_men + no_of_women))
print('The number of children in the town is:', no_of_children)


# In[2]:


# Question 2
amount_of_boxes = 2425
pencils_per_box = 24
tot_amount_of_pencils = (amount_of_boxes * pencils_per_box)
print('The total amount of pencils in all the boxes is:', tot_amount_of_pencils)


# In[3]:


import jovian


# In[4]:


jovian.commit(project='introductory-steps-with-python')

