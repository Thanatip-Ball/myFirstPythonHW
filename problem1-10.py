#!/usr/bin/env python
# coding: utf-8

# # ex1

# In[1]:


2 + 3


# # ex2

# In[2]:


print('hello, world!'*4)


# # ex3

# In[3]:


1 + 2


# # ex4

# In[4]:


x = 4
y = x +1
x = 2
print(x,y)


# # ex5

# In[1]:


x,y = 2,6
x,y = y,x+2
print(x,y)


# # ex6

# In[1]:


a,b = 2,3
c,b = a,b+1 #เปลี่ยนจาก a,c+1 เป็น a,b+1
print(a,b,c)


# # ex7

# In[32]:


numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x 
print (square(5))
print (square(2*5)) #เพิ่มวงเล็บตรง square


# # ex8

# In[43]:


x = 1
def f():
    return x
print (x)
print (f()) #ใส่วงเล็บให้ x,f


# # ex9

# In[42]:


x = 1
def f():
    x = 2
    return x
print (x)
print (f())
print (x)


# # ex10

# In[49]:


x = 1 
def f():
        global x
        y = x
        x = 2
        return x + y
print (x)
print (f())
print (x)


# In[ ]:




