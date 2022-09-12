#!/usr/bin/env python
# coding: utf-8

# In[6]:


#take the user input (age), above 60 (print("senoirs"), 40-60(print("your message")
a = int(input("enter the age:"))
if a>60:
    print("welcome to the seniors club")
elif 40<a<60:
    print("your are senior")
else a<40<20:
     print("your are junior")         
print(a)                                                             


# In[7]:


#2) print first 10 natural numbers using while and for loop
i = 1
while i <= 10:
    print(i)
    i += 1


# In[10]:


for i in range(1, 11):
    print(i)


# In[13]:


#wap to print the multiplication of table (ask the user input)

num = int(input ("Enter multiplication table: "))          

print ("The Multiplication Table of: ", 5)    

for count in range(0, 11):      

  print (num,count, '=', num * count)


# In[17]:


# 4) create a list of your favouraite fruits and print one by one 

fruits=['apples','oranges','bananas','mangoes','grapes','strawberry']
print(fruits[1:6])


# In[18]:


# 5) wap to sum of all the items in a list (create a list )

list1 = [12,34,45,65,75]
total = sum(list1)
print("sum of all items is:",total)


# In[19]:


# 6) wap to reverse a list 
list = [10,20,30,40,50,60,70,80,90,100]
list. reverse()  
print(list)


# In[24]:


# 7) wap to return the maximum of 2 numbers using list comprehension
a = 200
b = 90
print(a if a >= b else b)
 


# In[25]:


# 8) print the following pattern 
#1
#11
#111
#1111
#11111

for i in range (5):
    for j in range(i):  
        print('1',end='')
    print()


# In[ ]:


# 9) genrate a python list of all even numbers between 4 to 30


# In[ ]:


#10) convert 2 list into 1 dictionary


# In[ ]:


# 11) create a tuple with 3 items and assign every valuse to a avariable and print each variable 
x = "java","python"
z,y=x


# In[34]:


print(z)


# In[ ]:


#12) create a function for:
given 2 integers return their product only if the product is equal to or lower than 1000, else return thier sum


# In[ ]:


#13) what is append 
ans: append is to add something at end of list 
    # what is insert 
ans: insert  the given element at a particular index in a list 
    # what is extend 
ans : extend is to add specified elements in list 


# In[43]:


#14) create a numpy array and print its shape and dimesntion 
import numpy as np
a = np.array([[2,3],[4,5], [6,7]])
b = np.array([[4,6],[7,8],[1,2]])
print(a)
print(a.ndim)


# In[44]:


a.shape()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




