#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_string=input("enter any numbers ")
input_list=list(map(int,input_string.split()))
for x in input_list:
    if x%2 == 0:
        print(x**3)
    else:
        print(x**2)


# In[ ]:


import math
a=36
print(math.sqrt(a))


# In[ ]:


import math

input_string = input("enter any numbers ")
input_list = list(map(int, input_string.split()))

prime_list = []

for x in input_list:
    if x > 1:
        is_prime = True
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(x)

print(prime_list)


# In[ ]:


rohit="rohit"
print(rohit[-1::-1])


# In[ ]:


sentence=["orange","dead","sinces"]
print(sentence)
for i in range(len(sentence)):
    sentence[i]=sentence[i][-1::-1]
    print(sentence[i])


# In[ ]:


sentence=["orange","dead","sinces"]
print(sentence)
in_list=[]
for i in range(len(sentence)):
    if ((sentence[i][0::-1])==(sentence[i][-1::])):
        in_list.append(sentence[i])
print(in_list)


# In[ ]:


sentence=["orango",'dead',"wood","happy"]
print(sentence)
for i in range(len(sentence)):
    if ((sentence[i][0::-1])==(sentence[i][-1::])):
        print(sentence[i])


# In[ ]:


sen=int(input())
sentence=sen.split()
print(sentence)
for i in range(len(sentence)):
    if ((sentence[i][0::])==(sentence[i][-1::-1])):
        print(sentence[i])
    else:
        print("number is not palindrome")


# In[ ]:


sen=input()
sentence=sen.split()
print(sentence)
in_list=[]
for i in range(len(sentence)):
    if ((sentence[i][0::])==(sentence[i][-1::-1])):
        in_list.append(sentence[i])
print(in_list)


# In[ ]:


k = int(input())
i = 1


# In[ ]:


while(i <= 10):
    
    t = k*i
    print(f"{k}*{i} = {t}")
    i += 1
  


# In[ ]:


n = int(input())
i = 0
while(i<n/2):
    i = i+1
    print(i)


# In[ ]:


n= int(input())
k = 0
while(n > 0):
    t= n%10
    k = t+k
    n = n//10
print(k)


# In[ ]:


k = 22+33+23+28+21+13+25+35+21+32+21+29+44+32+49+29+46+30+45+31+52+30+78+5
print(k)


# In[ ]:


for i in range(0,10,1):
    print(i)


# In[ ]:


for i in range(100,0,-1):
    print(i)


# In[ ]:


x='mohit'
for i in range(len(x)):
    print(x[i])


# In[ ]:


x='mohit'
for i in range(len(x)):
    if(i%2==0):
        print(x[i])


# In[ ]:


x='mohitoaaei'
sum=0
for i in range(len(x)):
    if(x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' 
    or x[i]=='u'):
        sum=sum+1
print(sum)


# In[1]:


for i in range(0,5):
    for j in range(0,5):
        print(j,end=" ")


# In[4]:


for i in range(0,5):
    for j in range(0,5):
        print(j,end=" ")
    print('\n')


# In[10]:


for i in range(0,5):
    for j in range(0,i):
        print('*',end=" ")
    print('\n')


# In[32]:


for i in range(5,0,-1):
    for j in range(0,i):
        print('*',end=" ")
    print('\n')


# In[63]:


for i in range(0,5):
    for j in range(0,5-i):
        print(' ',end='')
    for k in range(0,i+1):
        print("*",end='')
    print('\n')


# In[72]:


for i in range(0,5):
    for j in range(0,5):
        if(j==0 or j==4 or i==0 or i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('\n')  


# In[22]:


for i in range(0,5):
    for j in range(0,5):
        if( j==0 or j==4 or i==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('\n')


# In[112]:


n=int(input())

for i in range(0,n):
    for j in range(0,n):
        if( i==0 or i==n-1 or j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('\n')


# In[56]:


for i in range(0,5):
    for j in range(0,5-i):
        print(' ',end=" ")
    for k in range(0,5-j):
        print("  * ",end="")
    print('\n')


# In[152]:


for i in range(0,5):
    for j in range(5-i,0,-1):
        print(' ',end=" ")
    for k in range(0,1):
        print("*",end="")
    for l in range(0,i):
        if(i==3):
            print("*",end=" ")
        else:
            print(' ',end=" ")
        print(' ',end=" ")
    for m in range(0,1):
        print("*",end="")
    print('\n')


# In[125]:


n=int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==n-1 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print('\n')


# In[174]:


for i in range(0,5):
    for j in range(5-i,0,-1):
        print(' ',end=" ")
    for k in range(0,1):
        print("*",end="")
    for l in range(0,2*i):
        print(' ',end=" ")
    for m in range(0,1):
        print("*",end="")
    print('\n')


# In[6]:


a=50
b=200
c=300
d=100

if(a>b):
    if(a>c):
        if(a>d):
            print("a is greater")
        else:
            print("d is greater")
elif(b>c):
    if(b>d):
        print("b is greater")
    else:
        print("d is greater")
elif(c>a):
    if(c>d):
        print("c is greater")
    else:
        print("d is greater")


# In[7]:


list : element store order, index postion
       different datatype possible
       no continuous memory location
       mutable(changeable)


# In[11]:


mylist=['hello','hi',2,3,]
mylist[0:2]=[4,5,6]
print(mylist)


# In[13]:


mylist.append(100)
print(mylist)


# In[15]:


mylist.extend("hi")
print(mylist)


# In[16]:


mylist.extend(['hi'])
print(mylist)


# In[17]:


mylist.extend(4)
print(mylist)
because int is not iterable


# In[18]:


mylist.pop()


# In[19]:


mylist.pop(3)


# In[20]:


"""in pop we paas index
in remove we paas value
del remove memory address of given index"""

"""
clear
cp
count
len
extend
index
insert
reverse
sort """
help(mylist)


# In[21]:


myli=[10,20,30,40]
for var in myli:
    print(var)


# In[30]:


li=[10,20,30,40]
for x in li:
    if(x%2!=0):
        print(x)
    


# In[33]:


mylist=[10,20,30,40]
count=len(mylist)

for index in range(0,count):
    if(mylist[index] % 2 !=0):
        print(index, mylist[index])
        mylist[index]= mylist[index]+5
print(mylist)


# In[ ]:


new=[10,20,30,40]
i=0
while(i<len(new)):
    if(i%2==0):
        print(i,new[i])
    i=i+1
print(new)  


# In[ ]:


list=[10,'li',30,40.0,'hello',50]
new_list=[]
k=0
print(list)
for i in range(len(list)):
    if(type(list[i]) == int):
        k=list[i]*2
        new_list.append(k)  
    elif(type(list[i])==str):
        n=len(list[i])-1
        k=list[i][0:n]
        new_list.append(k)
    
print(new_list)


# In[ ]:





def identify_unique_and_duplicates(input_list):
    unique_elements = set()
    duplicate_elements = []

    for element in input_list:
        if element in unique_elements:
            duplicate_elements.append(element)
        else:
            unique_elements.add(element)

    return list(unique_elements), duplicate_elements

# Example usage
input_list = ["apple", "banana", "orange", "apple", "grape", "banana", "apple", "kiwi"]
unique_elements, duplicate_elements = identify_unique_and_duplicates(input_list)

print("Unique elements:", unique_elements)
print("Duplicate elements:", duplicate_elements)

