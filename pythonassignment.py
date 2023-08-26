#!/usr/bin/env python
# coding: utf-8

# In[ ]:


break = 5
#reason -> break is a predefine keyword so we can't use as a variable name 


# In[ ]:


birth_year=2003
current_year=2023
age=current_year-birth_year
print(age)


# In[ ]:


first_name='Vaishali'
last_name='Sharma'
print(f'{first_name} {last_name}')


# In[ ]:


first_name='Vaishali '
last_name='Sharma'
print(first_name+last_name)


# In[ ]:


_nation=3
print(_nation)


# In[ ]:


1record=3
print(1record)


# In[ ]:


record^one=3


# In[ ]:


record-one=3


# In[ ]:


#You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
l,h=map(float,input().split())
area=l*h
print(area)


# In[ ]:


"""You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. 
Find out using python, how many dollars is the shopkeeper going to give you back?"""

packets=float(input())
price_of_one_packet=float(input())
given_price=float(input())
back_cost=(given_price-(packets*price_of_one_packet))
print(back_cost)


# In[ ]:


"""You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. 
If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. 
Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)"""

sq_length,cost_per_feet=map(float,input().split())
area_sq=sq_length*sq_length
finalcost=cost_per_feet*area_sq
print(finalcost)


# In[ ]:


num=int(input())
print(f'Binary of {num} is',format(num,'b'))


# In[ ]:


"""Create 3 variables to store street, city and country, now create address variable to store entire address. 
Use two ways of creating this variable, one using + operator and the other using f-string. 
Now Print the address in such a way that the street, city and country prints in a separate line."""

street,city,country=map(str,input().split())
address=street+'\n'+city+'\n'+country
print(address)


# In[ ]:


x="Earth revolves around the sun".split()
print(x[1])


# In[ ]:


x="Earth revolves around the sun".split()
print(x[-1])


# In[ ]:


"""Create two variables to store how many fruits and vegetables you eat in a day. 
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. 
Use python f string for this."""

fruits, vegetables=map(int,input().split())
print(f'I eat {vegetables} veggies and {fruits} fruits daily')


# In[ ]:


"""I have a string variable called s='maine 200 banana khaye'. 
This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line."""

'maine 200 banana khaye'.replace("200 banana", "10 samosa")


# In[ ]:


#string.replace(oldvalue, newvalue, count) here count=occurrences of the old value you want to replace.


# In[ ]:


li=[2200, 2350, 2600, 2130, 2190]
#    jan   feb  march april may


# In[ ]:


"""1. In Feb, how many dollars you spent extra compare to January?"""

extra=li[1]-li[0]
print(extra)


# In[ ]:


"""2. Find out your total expense in first quarter (first three months) of the year."""

quarter=li[0]+li[1]+li[2]
print(quarter)


# In[ ]:


"""3. Find out if you spent exactly 2000 dollars in any month"""

li=[2200, 2350, 2600, 2130, 2190]
for i,amount in enum(li):
    if(li[i]==2000):
        print(f 'you spent 2000 dollars in {i} month')
    else:
        print(f 'no, you does not spent 2000dollars in any month ')


# In[ ]:


"""4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list"""

li.append(1980)
print(li)


# In[ ]:


"""5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list based on this"""

li[3]=li[3]-200
print(li)


# In[ ]:


heros=['spider man','thor','hulk','iron man','captain america']


# In[ ]:


"""1. Length of the list"""
len(heros)


# In[ ]:


"""2. Add 'black panther' at the end of this list"""

heros.append('black panther')
print(heros)


# In[ ]:


"""3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk' """

heros.pop()
print(heros)


# In[ ]:


heros.insert(2,'black panther')
print(heros)


# In[ ]:


"""4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code."""

heros[1:3]=['doctor strange']
print(heros)


# In[ ]:


""" Sort the heros list in alphabetical order"""

heros.sort()
print(heros)


# In[ ]:


#a tuple containing sum and multiplication of two input numbers

tup=(2,3,4,5)
multi=tup[0]*tup[1]
add=tup[0]+tup[1]
print(multi)
print(add)


# In[ ]:


print(dir(tup))


# In[ ]:


n1=10
n2=20
n1.__add__(n2)


# In[ ]:


'''This program asks for person name and age and builds a dictionary using that
    Later on you can input person name and it will tell you the age of that person'''

d={'riya':20}
print(d['riya'])


# In[ ]:


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]


# In[ ]:


#1.Write a program that asks user to enter a city name and it should tell which country the city belongs to

city=input('enter city name')

if city in india:
    print(f"{city} is in india")
elif city in pakistan:
    print(f"{city} is in pakistan")
elif city in bangladesh:
    print(f'{city} is in bangladesh')
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")
    


# In[ ]:


"""Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India"
but if I enter mumbai and dhaka it should print "They don't belong to same country" """

city1=input("enter city1")
city2=input("enter city2")
if city1 in india:
    if city2 in india:
        print("Both cities are in india")
    else:
        print("They don't belong to same country")
elif city1 in pakistan:
    if city2 in pakistan:
        print("Both cities are in pakistan")
    else:
        print("They don't belong to same country")
elif city1 in bangladesh:
    if city2 in bangladesh:
        print("Both cities are in bangladesh")
    else:
        print("They don't belong to same country")


# In[ ]:


city1=input("enter city1")
city2=input("enter city2")
if city1 in india and city2 in india:
        print("Both cities are in india")

elif city1 in pakistan and city2 in pakistan:
        print("Both cities are in pakistan")

elif city1 in bangladesh and city2 in bangladesh:
        print("Both cities are in bangladesh")
        
else:
        print("They don't belong to same country")


# In[ ]:


"""Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100
1.Ask user to enter his fasting sugar level"""

sugar_level=int(input('Enter your fasting sugar level'))

"""2.If it is below 80 to 100 range then print that sugar is low
3.If it is above 100 then print that it is high otherwise print that it is normal"""

if(80 > sugar_level):
    print("sugar is low")
elif(sugar_level>100):
    print("sugar is high")
else:
    print("sugar is normal")


# In[ ]:


"""1.Using for loop figure out how many times you got heads"""

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in range(len(result)):
    if(result[i]=='heads'):
        count=count+1
print(count)


# In[ ]:


"""2.Print square of all numbers between 1 to 10 except even numbers"""
num=0
for i in range(1,11):
    if(i%2!=0):
        num=i**2
        print(num)


# In[ ]:


"""Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
If expense is not found then it should print that as well."""

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

expense = int(input("Enter an expense amount: "))

if expense in expense_list:
    month = expense_list.index(expense)
    print(f'You spent {expense} in {month_list[month]}.')
else:
    print(f'You didn\'t spend {expense} in any month.')


# In[ ]:


month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = int(input("Enter expense amount: "))

month = -1                                                              #month=0
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:                                                         #use this also if (n == expense_list[i]):
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')


# In[ ]:


# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations messagen = int(input())

for i in range(n,0,-1):
    if(i>0):
        print("are you tired..?")
        t = input()
        if(t == "yes"):
            print("you didn't finish the race")
            break
        else:
            continue
            
print("congratulation ! you finish the race")
    


# In[ ]:


"""Write a program that prints following shape

*
**
***
****
*****       """

n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    print('')


# In[ ]:


"""Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. 
Equation of an area of a triangle is area = (1/2)*base*height """

def area(base,height):
    are=(1/2)*base*height
    print(are)

area(2,4)


# In[ ]:


""" Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". 
Based on shape type it will calculate area. Equation of rectangle's area is rectangle area=length*width  """


def area(width,length,shape):
    if(shape=="triangle"):
        triangle_area=(1/2)*width*length
        return triangle_area
    elif(shape=="rectangle"):
        rectangle_area=length*width
        return rectangle_area
    else:
        return "the shape is neither the triangle nor rectangle shape" 
    
shape=input()
width,length=map(int,input().split())
area(width,length,shape)


# In[ ]:


"""Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***   Basically number of lines it prints is equal to that number."""

def print_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("")

n=int(input())
print_pattern(n)


# In[ ]:


"""Country	Population
China	    143
India	    136
USA	        32
Pakistan	21

Using above create a dictionary of countries and its population"""

dic={"China":143, "India":136, "USA":32, "Pakistan":21}
print(dic)
dic.keys()
dic.values()


# In[ ]:


for i in dic:
    print(f"{i} ==> {dic[i]}")


# In[ ]:


"""add: if user input add then it should further ask for a country name to add. 
    If country already exist in our dataset then it should print that it exist and do nothing. 
    If it doesn't then it asks for population and add that new country/population in our dictionary and print it"""

choice=input()

if(choice=="add"):
    cty=input("please enter country name ")
    if cty in dic:
        print("it exist")
    else:
        pp=input("enter population")
        dic[cty]=pp


# In[ ]:


"""remove: when user inputs remove it should ask for a country to remove. 
    If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). 
    Else print that country doesn't exist! """

choice=input()

if(choice=="remove"):
    cty=input("please enter country name ")
    if cty in dic:
        dic.pop(cty)
        print(dic)
    else:
        print("country doesn't exist!")


# In[ ]:


"""query: on this again ask user for which country he or she wants to query. 
    When user inputs that country it will print population of that country."""

choice=input()
if(choice=="query"):
    cty=input("please enter country name ")
    if cty in dic:
        print(dic[cty])


# In[ ]:


dic={"China":143, "India":136, "USA":32, "Pakistan":21}
print(dic)
choice=input()

for i in dic:
    print(f"{i} ==> {dic[i]}")

if(choice=="add"):
    cty=input("please enter country name ")
    if cty in dic:
        print("it exist")
    else:
        pp=input("enter population")
        dic[cty]=pp

elif(choice=="remove"):
    cty=input("please enter country name ")
    if cty in dic:
        dic.pop(cty)
        print(dic)
    else:
        print("country doesn't exist!")
        
elif(choice=="query"):
    cty=input("please enter country name ")
    if cty in dic:
        print(dic[cty])


# In[ ]:


"""You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril 	[1430,1490,1567]
mtl 	[234,180,160]

Write a program that asks user for operation. Value of operations could be,
1.print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33  """


# In[65]:


dic={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
r=0
n=len(dic[i])
print(n)
for i in dic:
    print(dic[i])
    sum=0
    for j in dic[i]:
        sum=j+sum
    print(sum)
    print(sum/n)


# In[71]:


"""add: When user enters 'add', it asks for stock ticker and price. 
    If stock already exist in your list (like info, ril etc) then it will append the price to the list. 
    Otherwise it will create new entry in your dictionary. 
    For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks. """

user=input()
if(user=="add"):
    stock=input()
    price=input()
    if stock in dic:
        print(stock)
        dic[i]=price
    else:
        dic.update({stock:price})
        print(dic)


# In[77]:


"""Write circle_calc() function that takes radius of a circle as an input from user and then it calculates 
and returns area, circumference and diameter. 
You should get these values in your main program by calling circle_calc function and then print them"""

import math

def circle_calc(radius):
    area_of_circle= math.pi*(radius**2)
    circumference= 2*math.pi*radius
    diameter= 2*radius
    return area_of_circle, circumference, diameter


radius=int(input())
circle_calc(radius)
    #print(f"Area:{} , Circumference:{}, Diameter:{})


# In[82]:


import math

def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area, circumference,diameter

if __name__=="__main__":
    r=input("Enter a radius:")
    r=float(r)
    area,c,d=circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")

