#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("hello /n world")
print("regex")


# In[3]:


print("hello world",end="\n")
print("regex")


# In[4]:


print("hello world",end=" ")
print("regex")


# In[5]:


print("hello world",end="$$")
print("regex")


# In[6]:


print("yash","aman")


# In[7]:


print("yash","aman",sep=" ")


# In[8]:


print("yash","aman",sep="--")


# In[9]:


#variable=container(to store value)


# In[10]:


age=100
print('age is ',age)


# In[11]:


age=100
print(type(age))


# In[12]:


age="ten"
print(type(age))


# In[13]:


'''datatype of python: int,float,string,boolean,complex,list,tuple,dict,set,frozenset
number,string,boolean: are immutable
# : documnet(to understand)
""" : multi line string'''
''':multi line comment'''


# In[14]:


address="""hello,
my name is
Vaishali sharma"""
print(address)


# In[15]:


type("""hello,
my name is
Vaishali sharma""")


# In[16]:


# string formatting
age=20
fname="hlo"
company="regex"
print(f"age is {age}")


# In[17]:


#call by object reference


# In[18]:


fname="tushar"
print(fname,id(fname))

fname="goyal"
print(fname,id(fname))


# In[19]:


fname="tushar"
print(fname,id(fname))

company="tushar"
print(company,id(company))


# In[20]:


fname="tushar"
print(fname,id(fname))

fname="goyal"
print(fname,id(fname)) 

company="tushar"
print(company,id(company))


# In[22]:


#slicing
'''-4-3-2-1
stop
0123

slice:
slicing: var[start:stop:[step=1]]
stop is exclusive'''


# In[23]:


state="RAJASTHAN"
state[0]


# In[24]:


state="RAJASTHAN"
state[0:3]


# In[25]:


state="RAJASTHAN"
state[5:8]


# In[26]:


state="RAJASTHAN"
state[0:4:1]

#0+1 1+1 2+1 


# In[27]:


state="RAJASTHAN"
state[0:4:-1]


# In[28]:


state="RAJASTHAN"
state[0:6:2]


# In[29]:


state="RAJASTHAN"
state[-1:-4]


# In[30]:


state="RAJASTHAN"
state[-1:-4:-1]


# In[31]:


state="RAJASTHAN"
state[-1:-4:-1]


# In[32]:


state="RAJASTHAN"
state[-1::]


# In[33]:


state="RAJASTHAN"
state[::-1]


# In[34]:


state="RAJASTHAN"
state[3::-1]


# In[35]:


#session link = https://bit.ly/3DzhJYb


# In[43]:


num_list = [int(input("enter an integer")) for _ in range(5)]
print(num_list)


# In[44]:


input_string=input("enter multiple inputs with spaces")
input_list=input_string.split()
numbers=[int(num) for num in input_list]
numbers


# In[48]:


input_string=input("enter three numbers")
input_list=input_string.split()
numbers=list(map(int,input_list))
print(numbers)


# In[49]:


a,b,c=list(map(int,input("enter three values").split()))


# In[50]:


n=(a+b+c)/3
print(n)


# In[51]:


test="hlo i m vaishali hlo"
p=test.count('hlo')
print(p)


# In[52]:


test="hlo i m vaishali hlo"
len(test)


# In[53]:


input_string=input("enter any numbers ")
input_list=list(map(int,input_string.split()))
print(input_list)
maxno=max(input_list)
minno=min(input_list)
print(f"max number {maxno}")
print(f"min number {minno}")


# In[55]:


input_string=input("enter any numbers ")
input_list=list(input_string.split())
print(input_list)
len(input_list)


# In[ ]:


input_string=input("enter any numbers ")
input_list=list(map(int,input_string.split()))
for x in input_list:
    if x%2 == 0:
        print(x**3)
    else:
        print(x**2)

