#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def perfect(num):
    num_div=[]
    sum=0

    for i in range(1,num+1):
        if num%i==0:
            num_div.append(i)
    print("divisors of ", num," are ", num_div)

    for elem in num_div:
        sum= sum+elem
    if num==0.5*sum:
        print(num, " is a perfect number.")
    else:
        print(num, " is not a perfect number.")

num= int(input("enter a number to check whether its perfect: "))
perfect(num)


