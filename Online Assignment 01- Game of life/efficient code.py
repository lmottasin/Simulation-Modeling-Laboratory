# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aHMVaCrz2GE_bn0tTwhHkbmLUAfmBTb4
"""

import numpy as np
map = [
       [0,1,0,0,0],
       [0,0,1,0,0],
       [0,1,1,0,1],
       [0,1,0,0,1],
       [0,0,0,0,0],
]
map = np.array(map)
print("Time: 0")
print(map)

def boundary(i,j):
  if ( i>=0 and i<=4) :
    if (j>=0 and j<=4):
      return True
  return False


def count_live_neighbors(map, i, j):
    # Your code goes here
    count =0
    initial_i = i-1 
    last_i = i+1 
    initial_j = j-1 
    last_j = j+1 
    
    for a in range( initial_i , last_i +1 ):
      for b in range(initial_j , last_j +1):
        if ( boundary(a,b)  and map[a,b]==1  ):
            if ( a==i and b==j ):
              pass
            else: 
              count+=1

    return count

def flip(map, i, j):
    # Your code goes here
    # flips 
    if ( map[i,j] == 1 ):
      if ( count_live_neighbors(map, i, j) < 2):
        return True
    # not flips
    if  map[i,j] == 1 :
      if ( count_live_neighbors(map, i, j) == 2):
        return False
    # flips 
    if  map[i,j] == 1 :
      if ( count_live_neighbors(map, i, j) > 2):
        return True
    #flips
    if  map[i,j] == 0  :
      if ( count_live_neighbors(map, i, j) == 2 or  count_live_neighbors(map, i, j) == 3 ):
        return True
    
    return False

for t in range(1,21):
    new_map = np.zeros(map.shape, dtype = int)
    for i in range(0,map.shape[0]):
        for j in range(0,map.shape[1]):
            flip_flag = flip(map, i, j)
            if flip_flag==True:
                new_map[i,j] = 1 - map[i,j]
            else:
                new_map[i,j] = map[i,j]
    
    map = new_map
    print("Time: {}".format(t))
    print(map)
#print(count_live_neighbors(map, 0,4))