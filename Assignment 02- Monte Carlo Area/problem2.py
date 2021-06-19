# -*- coding: utf-8 -*-
"""problem2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16dr7PuliIM66NFopmBJ_MttVorMkZ-2k
"""

#import libraries
import matplotlib.pyplot as plt
import math
import numpy as np
import random
random.seed(10)
def plot_and_calculate(N):
  # drawing the square
  plt.figure(figsize=(10,5))
  plt.plot([0,4,4,0,0], [0,0,2,2,0], c='blue')
  # drawing the left segment
  plt.plot([0,1],[0,1], c= "blue")
  #drawing the right segment 
  plt.plot ([3,4],[1,0],c="blue")
  # drawing the middle arch
  arch_x = []
  arch_y = []
  #count=0 
  for x in np.arange(1,3.001,0.001):
    x = round(x,3)
    arch_x.append(x)
    #print(x)
    y = math.sqrt(1-(x-2)**2)+1
    arch_y.append(y)
    

    #count+=1
  #print(count)
  plt.plot(arch_x, arch_y,c='blue')

  # calculate pi vaLue
  hit=0


  #store the x,y values
  hit_x_value = []
  hit_y_value =[]
  miss_x_value = []
  miss_y_value =[]
  for i in range(1,N+1):
    x = random.uniform(0,4)
    y = random.uniform(0,2)

    #checking the left segment
    if x>=0 and x <=1:
      if y<= x : 
        hit+=1
        hit_x_value.append(x)
        hit_y_value.append(y)
      else:
        miss_x_value.append(x)
        miss_y_value.append(y)
    #checking the 3rd segment
    elif x>=3 and x <=4:
      if y<= 4-x : 
        hit+=1
        hit_x_value.append(x)
        hit_y_value.append(y)
      else:
        miss_x_value.append(x)
        miss_y_value.append(y)
    
    
    #checking the middle segment 
    elif x>1 and x <3:
      #chehcking the rectangle area
      if y<=1: 
        hit+=1
        hit_x_value.append(x)
        hit_y_value.append(y)
      #checking the arch with center (2,1)
      elif y>1 and y<=  math.sqrt(1-(x-2)**2)+1 :
        hit+=1
        hit_x_value.append(x)
        hit_y_value.append(y)
      else: 
        miss_x_value.append(x)
        miss_y_value.append(y)  
  
  #ploting the hit values
  plt.scatter(hit_x_value,hit_y_value,s=5,c="green")
  #plotting the miss values
  plt.scatter(miss_x_value,miss_y_value,s=6,c="red")

  estimated_pi = hit/N 

  grey_area = estimated_pi * (4*2)
  print("For Sample Number: ",N)
  print("Area of grey region: ", grey_area)

  # true value = left segment + right segment + middle rectangle + arch(area of cirle/2)
  true_area = (.5 * 1 * 1 ) +  (.5 * 1 * 1 ) + (2*1) + ( ( math.pi * 1 ) / 2)
  print("True area: ", true_area)
  plt.show()

N=[100,1000,10000]
for i in N:
  plot_and_calculate(i)