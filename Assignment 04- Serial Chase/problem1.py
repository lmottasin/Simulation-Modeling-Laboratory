# -*- coding: utf-8 -*-
"""offline 5 problem 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XtqUMq04bwmqgJuzz30_2_c9elL3SScl
"""

#libraries 
import matplotlib.pyplot as plt
import math

# simulation time
time = 20 
# initiail points 
B_P_X = [0]               # B , x coordinate
B_P_Y = [10]              # B, y coordinate

D_P_X = [0]               # D , x coordinate
D_P_Y = [0]               # D , y coordinate

A_P_X = [10]               # A , x coordinate
A_P_Y = [0]               # A , y coordinate

C_P_X = [10]               # C , x coordinate
C_P_Y = [10]               # C , y coordinate

#  shooting variable 

A_shoot_faced = 0
B_shoot_faced = 0
C_shoot_faced = 0
D_shoot_faced = 0 

# velocity 
s_A = 3
s_B = 5
s_C = 7
s_D = 2



for i in range (0,time+1):

  print("At time: ", i )
  
  # distance between D and B 
  dist_between_D_B = math.sqrt(( D_P_X[i] - B_P_X[i] )**2 + (D_P_Y[i] - B_P_Y[i])**2)

  # distance between A and D 
  dist_between_A_D = math.sqrt(( A_P_X[i] - D_P_X[i] )**2 + (A_P_Y[i] - D_P_Y[i])**2)

  # distance between C and A 
  dist_between_C_A = math.sqrt(( C_P_X[i] - A_P_X[i] )**2 + (C_P_Y[i] - A_P_Y[i])**2)

  # distance between B and C 
  dist_between_B_C = math.sqrt(( B_P_X[i] - C_P_X[i] )**2 + (B_P_Y[i] - C_P_Y[i])**2)
  
  # check the shooting between D and B 
  if dist_between_D_B < 5.0: 
    print("B shoots D :: Target D: ({},{}) and Pursuer B: ({},{}) ".format(D_P_X[i],D_P_Y[i],B_P_X[i],B_P_Y[i] ))
    D_shoot_faced +=1 

  # check the shooting between A and D 
  if dist_between_A_D < 5.0: 
    print("D shoots A :: Target A: ({},{}) and Pursuer D: ({},{}) ".format(A_P_X[i],A_P_Y[i],D_P_X[i],D_P_Y[i] ))
    A_shoot_faced +=1

   # check the shooting between C and A 
  if dist_between_C_A < 5.0: 
    print("A shoots C :: Target C: ({},{}) and Pursuer A: ({},{}) ".format(C_P_X[i],C_P_Y[i],A_P_X[i],A_P_Y[i] ))
    C_shoot_faced +=1

      # check the shooting between B and C 
  if dist_between_B_C < 5.0: 
    print("C shoots B :: Target B: ({},{}) and Pursuer C: ({},{}) ".format(B_P_X[i],B_P_Y[i],C_P_X[i],C_P_Y[i]))
    B_shoot_faced +=1

  # B calculation 

  # target = D , pursuier = B
                      # target x - pursuer x / dist  
  cos_theta_for_D_B = ( D_P_X[i] - B_P_X[i] ) / dist_between_D_B
  sin_theta_for_D_B = ( D_P_Y[i] - B_P_Y[i] ) / dist_between_D_B
            # persuer    persuer spped
  B_new_x =  B_P_X[i] + s_B * cos_theta_for_D_B
  B_new_y = B_P_Y[i] + s_B * sin_theta_for_D_B

  B_P_X.append(B_new_x)
  B_P_Y.append(B_new_y)

  # D calculation

  # target = A , pursuier = D
                      # target x - pursuer x / dist  
  cos_theta_for_A_D = ( A_P_X[i] - D_P_X[i] ) / dist_between_A_D
  sin_theta_for_A_D = ( A_P_Y[i] - D_P_Y[i] ) / dist_between_A_D
            # pursuer    persuer spped
  D_new_x =  D_P_X[i] + s_D * cos_theta_for_A_D
  D_new_y = D_P_Y[i] + s_D * sin_theta_for_A_D

  D_P_X.append(D_new_x)
  D_P_Y.append(D_new_y)

  # A calculation

  # target = C , pursuier = A
                      # target x - pursuer x / dist  
  cos_theta_for_C_A = ( C_P_X[i] - A_P_X[i] ) / dist_between_C_A
  sin_theta_for_C_A = ( C_P_Y[i] - A_P_Y[i] ) / dist_between_C_A
            # pursuer    persuer spped
  A_new_x =  A_P_X[i] + s_A * cos_theta_for_C_A
  A_new_y = A_P_Y[i] + s_A * sin_theta_for_C_A

  A_P_X.append(A_new_x)
  A_P_Y.append(A_new_y)

  # C calculation

  # target = B , pursuer = C 
                      # target x - pursuer x / dist  
  cos_theta_for_B_C = ( B_P_X[i] - C_P_X[i] ) / dist_between_B_C
  sin_theta_for_B_C = ( B_P_Y[i] - C_P_Y[i] ) / dist_between_B_C

            # pursuer    persuer spped
  C_new_x =  C_P_X[i] + s_C * cos_theta_for_B_C
  C_new_y = C_P_Y[i] + s_C * sin_theta_for_B_C

  C_P_X.append(C_new_x)
  C_P_Y.append(C_new_y)

  
  print("A values x: {} , y :{}".format(A_P_X[i],A_P_Y[i]))
  print("B values x: {} , y :{}".format(B_P_X[i],B_P_Y[i]))
  print("C values x: {} , y :{}".format(C_P_X[i],C_P_Y[i]))
  print("D values x: {} , y :{}".format(D_P_X[i],D_P_Y[i]))
  print("")
  #print("Distance Between D,B: ",dist_between_D_B)
  #print("Distance Between A,D: ",dist_between_A_D)
  #print("Distance Between C,A: ",dist_between_C_A)
  #print("Distance Between B,C: ",dist_between_B_C)
  
# finally print the number each car get shot
print("A got shot",A_shoot_faced)
print("B got shot",B_shoot_faced)
print("C got shot",C_shoot_faced)
print("D got shot",D_shoot_faced)
#print(len(A_P_Y))
print("")
#plotting the values
plt.figure(figsize=(15,8))
plt.plot(A_P_X,A_P_Y,marker="o", label= "Car-A")
plt.plot(B_P_X,B_P_Y,marker="o", label= "Car-B")
plt.plot(C_P_X,C_P_Y,marker="o", label= "Car-C")
plt.plot(D_P_X,D_P_Y,marker="o", label= "Car-D")
plt.legend(loc = 'upper right')
plt.title("Path of each car")
plt.show()
