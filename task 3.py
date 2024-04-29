#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data=pd.read_csv(r"C:\Users\Tanvi\Downloads\householdtask3.csv")
data


# In[9]:


import matplotlib.pyplot as plt
age=[35.9,29.9,40.0,34.7]
size=[2.7,2.6,2.3,2.8]
plt.bar(age,size)
plt.title('age vs size')
plt.xlabel('age')
plt.ylabel('size')
plt.legend
plt.show()


# In[13]:


plt.figure(figsize=(10, 5))
plt.plot(data['year'], data['size'], marker='s', linestyle='-', color='green', label='age')
plt.xlabel('year')
plt.ylabel('size')
plt.title('year vs size')
plt.legend()
plt.grid(True)  
plt.show()



# In[ ]:




