#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import matplotlib.pyplot as plt

#Load the CSV into a DataFrame
data = pd.read_csv("SalesData.csv")



# scatter plot
#plt.subplot(2, 1, 1)

#fig size
plt.figure(figsize=(8,5))

#title

plt.title("Scatter Plot")
#plotting the points 
plt.scatter(data["Day"],data["Product A"])
plt.scatter(data["Day"],data["Product B"])
plt.scatter(data["Day"],data["Product C"])
# giving names to points by given order in points
labels = ['Product A', 'Product B', 'Product C']
#add the labels
plt.legend(labels)
# x,y label 
plt.xlabel("Days")
plt.ylabel("Sales")
#showing the plotting
plt.show()


#plt.subplot(2, 1, 2)

#line plot
#plot size
plt.figure(figsize=(8,5))
#title

plt.title("Line Plot")
#plotting the points
plt.plot(data["Day"],data["Product A"])
plt.plot(data["Day"],data["Product B"])
plt.plot(data["Day"],data["Product C"])
labels = ['Product A', 'Product B', 'Product C']
#add the labels
plt.legend(labels)
# x,y label 
plt.xlabel("Days")
plt.ylabel("Sales")
#plot show
plt.show()




# In[ ]:




