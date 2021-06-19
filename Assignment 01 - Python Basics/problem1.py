#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math
#taking input from user 
x = float(input("Input an odd number "))
#checking odd number

if x%2!=0:
    # first loop for doing the half of pattern 
    for first_half in range(0,math.ceil(x/2)):
        
        # for print the spaces befor * 
        for space in range(math.ceil(x/2)-1,first_half,-1):
            print(" ",end="")
        #for printing the * which is odd number series
        for star in range(2*first_half+1):
            print("*",end="")
        #for new line after each iteration 
        print("")
    #senod half
    i=1; 
    for second_half in range(math.floor(x/2),0,-1):
        #for print the space
        for space in range(i):
            print(" ",end="")
        
        #for printing star
        for star in range(0,2*second_half-1):
            print("*",end="")
        print("")
        i+= 1

else:
    print("Make sure input is odd number")
        
        


# In[ ]:




