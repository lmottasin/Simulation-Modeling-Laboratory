#imports libraries
import random
import math
import matplotlib.pyplot as plt
import numpy as np 

random.seed(500)
#no of needles
needles = int(input("Needles volume:"))
#hit count variable 
hit_count=0 
# to store values
y=[2,4,6,8]
plt.grid(axis='y')
for i in range(1,needles+1):
  c_x = random.uniform(1,9)
  c_y= random.uniform(1,9)
  theta = random.uniform (0,math.pi)
  #upper end values
  x_1 = c_x + (1/2)  * math.cos(theta)
  y_1 = c_y + (1/2)* math.sin(theta)
  #lower end values
  x_2 = c_x - (1/2)  * math.cos(theta)
  y_2 = c_y - (1/2)* math.sin(theta)
  
  #print(x_1,x_2,y_1,y_2)
  
  for i in np.arange(y_2,y_1+0.1,0.1):
    i = round(i,1)
    if ( round(i,1) %2.0==0 ):
      hit_count +=1 
      #print("this i",i)
      plt.plot([x_2,x_1],[y_2, y_1],'r')
      break
    else:
      plt.plot([x_2,x_1],[y_2, y_1],'g')


print("Pi value:")
print(needles/hit_count)
plt.show()
