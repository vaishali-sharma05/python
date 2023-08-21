#!/usr/bin/env python
# coding: utf-8

# Function
block of code  => reuse again and again
block of statement, worm, function   =>  small small postion
block => debugging

def function_name():
# In[ ]:


#function declare 
def hello():
    print("hello function")


# In[ ]:


#function call

hello()
hello()


# In[ ]:


#parameter
def hello(username):
    print("hello function",username)


# In[ ]:


#argument
hello("sikha")


# In[ ]:


age=100
print(age,id(age))


# In[ ]:


def addnumber(x):
    print(x,id(x))

addnumber(100)


# immutable= create new memory address
#            no changes to original memory address

# In[ ]:


def addnumber(x):
    x=2000
    print(x,id(x))

addnumber(100)


# In[ ]:


print(age,id(age))


# In[ ]:


def li(mylist):
    print(mylist,id(mylist))
    
mylist=[10,20]
print(mylist,id(mylist))
li(mylist)


# In[ ]:


def li(mylist):
    mylist[0]=300
    print(mylist,id(mylist))
    
mylist=[10,20]
print(mylist,id(mylist))
li(mylist)
print(mylist,id(mylist))

required argument: first argument(a)
postion argument: second argument(b)
hello(a,b)
# In[ ]:


def employee(eid,ename,email):
    print(f"Eid:{eid}, Name:{ename}, Email={email}")

employee(1,"sikha","sikha@gmail.com")


# In[ ]:


def employee(eid,ename,email):
    print(f"Eid:{eid}, Name:{ename}, Email={email}")

employee("sikha",1,"sikha@gmail.com")


# In[ ]:


#keyword argument
employee(ename="sikha", eid=1, email="sikha@gmail.com")


# In[ ]:


#postion argument
employee(ename="sikha", email="sikha@gmail.com", 1)


# In[ ]:


#postion argument
employee(1, ename="sikha", email="sikha@gmail.com")


# In[ ]:


def employee(eid,ename='sikha',email):          #default ename which is sikha if no argument is given to ename                  
    print(f"Eid:{eid}, Name:{ename}, Email={email}")

employee(1,"sikha@gmail.com")


# In[ ]:


#varibale length argument

def facebook(*args):
    print(args,type(args),args[-1])


# In[ ]:


facebook(10,20,30,"hello")


# In[ ]:


#keyword varibale length argument    (must be in right side)

def facebook(**args):
    print(args,type(args))


# In[ ]:


facebook(name=100, age=60)


# #Explain args and kwargs
# args= *args        (variable length argument)
# kwargs= **kwargs    (keyword variable length)
# 
# #difference between python2 and python3

# In[ ]:


def face(*args,**kwargs):
    print(args,kwargs)

face(10,name="hlo")


# In[ ]:


def face(*args,**kwargs):
    print(args,kwargs)

face()


# In[ ]:


def face1(**kwargs,*args):
    print(args,kwargs)

face(name="hlo")


# In[ ]:


def face1(*args,**kwargs):
    print(args,kwargs)

face(name="hlo")


# In[2]:


#lcm 

def lcm(a,b):
    if(a>b):
        greater=a
    else:
        greater=b
    while(True):
        if(greater%a==0 and greater%b==0):
            print("Lcm is",greater)
            break
        greater+1

a=int(input())
b=int(input())
lcm(a,b)


# In[3]:


#first class function: if we assign a function to another variable

def hlo():
    print("hlo function")

x=hlo


# In[4]:


x()


# In[5]:


hlo()


# In[8]:


print(hlo)
print(x)


# In[10]:


def square(x):
    print(x**2)
square(10)


# In[16]:


#Lambda functions => annomyous function => which 

lambda x:x**2


# In[14]:


out =lambda x:x**2
out(10)


# In[15]:


print(out)


# In[18]:


(lambda x:x**2)(10)


# In[20]:


def fun(x):
    print(x)
fun(20)


# In[24]:


def fun(x):
    print(x)
    
out=fun(10)
print("output",out)


# In[25]:


def fun(x):
    return x
    
out=fun(10)
print("output",out)


# In[26]:


def addnumber(x):
    return x+5


# In[30]:


mylist=[2,3,4]
map(addnumber,mylist)


# In[31]:


list(map(addnumber,mylist))


# In[32]:


list(map(lambda x:x+5, mylist))


# In[ ]:


#first class function : properties
#high class function

