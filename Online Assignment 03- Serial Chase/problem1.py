# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rhoTu73TqBIOm0rzujnWE_a2tlpBcRjR
"""

import math

# calculating the target x,y values
T_x =[]
T_y = []
for t in range(0,51):
  x = 50 - t ; 
  T_x.append(x)
  y = 10 * math.sin( t / 10 )
  T_y.append(y)

# pursuer simulation

p1_x = [0]
p1_y =[60]

p2_x = [60]
p2_y = [60]

#initial speed

s_p1 = 1.5
s_p2 = 1.8

for i in range(0,51):

  # distance between T - p1 
  dist_between_T_p1 = math.sqrt(( T_x[i] - p1_x[i] )**2 + (T_y[i] - p1_y[i])**2)
  #distance between T-p2
  
  dist_between_T_p2 = math.sqrt(( T_x[i] - p2_x[i] )**2 + (T_y[i] - p2_y[i])**2)

  # p1 value calculation
  # target = t , pursuer = p1 
                      # target x - pursuer x / dist  
  cos_theta_for_T_p1 = ( T_x[i] - p1_x [i] ) / dist_between_T_p1
                       # target y - pursuer y / dist
  sin_theta_for_T_p1 = ( T_y[i] - p1_y[i] ) / dist_between_T_p1

  p1_new_x =  p1_x[i] + s_p1 * cos_theta_for_T_p1
  p1_new_y = p1_y[i] + s_p1 * sin_theta_for_T_p1

  p1_x.append(p1_new_x)
  p1_y.append(p1_new_y)


  # p2 value calculation
  # target = t , pursuer = p2 
                      # target x - pursuer x / dist  
  cos_theta_for_T_p2 = ( T_x[i] - p2_x [i] ) / dist_between_T_p2
                       # target y - pursuer y / dist
  sin_theta_for_T_p2 = ( T_y[i] - p2_y[i] ) / dist_between_T_p2

  p2_new_x =  p2_x[i] + s_p2 * cos_theta_for_T_p2
  p2_new_y = p2_y[i] + s_p2 * sin_theta_for_T_p2

  p2_x.append(p2_new_x)
  p2_y.append(p2_new_y)

print("Target")
print(T_x[50], T_y [50])
print("p1")
print(p1_x[50], p1_y [50])
print("p2")
print(p2_x[50], p2_y [50])

# graph drawing 
import matplotlib.pyplot as plt

plt.plot(T_x,T_y,marker='o',label='T')
plt.plot(p1_x,p1_y,marker='o',label='P1')
plt.plot(p2_x,p2_y,marker='o',label='P2')
plt.legend()
plt.show()