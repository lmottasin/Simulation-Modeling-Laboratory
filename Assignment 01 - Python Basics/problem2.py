#!/usr/bin/env python
# coding: utf-8

# In[43]:


# creating class for double ended queue
class double_ended_queue:
    
    #creating a empty list 
    def __init__(self):
        self.list=[]
        
    #pushes value to end    
    def push_back(self,value):
        self.list.append(value)
        print("Inserts {} at back".format(value))
    #pushes value to front
    def push_front(self, value):
        self.list.insert(0,value)
        print("Inserts {} at front".format(value))
    # deletes front value
    def pop_front(self):
        try:
            value = self.list[0]
            self.list.pop(0)
            print("Removes {} from front".format(value))
        except:
            print("Emmpty list")
    # deletes last value    
    def pop_back(self):
        try:
            value = self.list[len(self.list)-1]
            self.list.pop(len(self.list)-1)
            print("Removes {} from back".format(value))
        except:
            print("Empty Queue")
    #prints front value 
    def print_front(self):
        try:
            #print(self.list[0])
            print("Prints front value",self.list[0])
        except:
            print("Empty Queue")
    #prints last value 
    def print_back(self):
        try:
            #print(self.list[len(self.list)-1])
            print("Prints back value ",self.list[len(self.list)-1])
        except:
            print("Empty Queue")
# check for file using try excetp 
try:
    #creating an object
    p = double_ended_queue() 
    #opnes file in read mode
    file = open("Input.txt","r")
    for i in file:
        # split line vlaues 
        list_2 =i.split()
        #print("read file values: ",list_2)
        # checks if it is push opertaions with values or not
        if(len(list_2)>1):
            
            if list_2[0]== 'A':
                p.push_front(list_2[1])
                
            elif list_2[0]== 'B':
                p.push_back(list_2[1])
                
        #for deleting and printing operation
        else:
            #checks if any emtpy line occurs
            try:
                if list_2[0]=='C':
                    p.pop_front()
                    
                elif list_2[0]=='D':
                    p.pop_back()
                    
                elif list_2[0]=='E':
                    p.print_front()
                    
                elif list_2[0]=='F':
                    p.print_back()
                    
            except:
                print("Empty line in input.txt file")
    
except FileNotFoundError:
    print("No such file found")


# In[ ]:




