#!/usr/bin/env python
# coding: utf-8
write a program to print the sum of n numbers using while loop?

# In[2]:


n=int(input("enter the number:n"))
sum=0
while (n>0):
    sum=sum+n
    n=n-1
print(sum)

write a program to check whether the given number is prime or not?
# In[12]:


def prime(n):
    c=0
    for i in range(2,n+1):
        if(n%i==0):
            c=c+1
    if(c==1):
        print("%d is prime number"%(n))
        
    else:
        print("%d is not prime number"%(n))
n=int(input("enter the number:n "))
prime(n)


# In[ ]:





# In[ ]:




