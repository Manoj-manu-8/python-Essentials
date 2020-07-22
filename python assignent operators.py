#!/usr/bin/env python
# coding: utf-8
 **TOPIC OPERATORS**
what is operator ?
operator means simlpy performing some operation on two things.
what do we need for perfoming operation?
In the operator defination we have discussed i.e we want two things(two things are nothing but we want two operands)
ex:a+b ....here a and b are called operands and '+' is  called operator..
ARITHMETIC OPERATORS 
operator      meaning                ex:               result
1.'+'        addition               a+b=2+3             5
2.'-'        subtraction            a-b=3-2             1
3.'*'        multiplication         a*b=3*2             6
4.'/'        divison                a/b=3/2             1.5
5.'%'        modulus                a%b=3%2             1
6.'//'       floor divison          a//b=3//2           1
7. '**'      power                  a**b=2**3           8
 a= 10 b= 4
print(a+b)   output=14            addition
print(a-b)   output=6             subtraction
print(a*b)   output=40            multipication
print(a/b)   output=2.5           provides the quotient
print(a%b)   output=2             provides the remainder
print(a//b)   output=2            provides the quotient in integer value
print(a**b)   output=10,000       power of 10 to 4 times gives==>>>10*10*10*10   
now we check the operators one by one with example...
# In[1]:


# programs 

a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

some of you  have a dout such that if we have all the operators in a same expression then how to perform..
1.() if we have this parenthesis in the expression then the sub expression inside the brackets () will be evalutaed first
2.*,/,%  after the brackets () then if we have these three '*','/','%'  follow order from left to right
3.+,-    after the 1st and 2nd process if we have '+','-', then follow order left to right
exaple:(20+30)+12+8/4*3
explation first take (20*30) gives== 1st value =600
next 8/4 gives == 2nd =2
next 8/4 we got 2 so 2*3 gives== using 2nd and 3 (2*3)=2rd value=6
#next add 12 3rd value
#finaly 600+6+12=618
#hey what is this you got there 618.0 then why here u got 618?????
#bcz '/' gives float value if perfect divisor is not there so we use '//' floor division to give integer value



#for integer output use '//'
print(4+4*3//6) 
# In[5]:


print((19-3)*(2+2)/4) 
print((19-3)*(2+2)//4) 
print(10/2 - 3%2 + (3 + 2) * 5)
print(10//2 - 3%2 + (3 + 2) * 5)


# In[2]:


print((19-3)*(2+2)/4) 
print((19-3)*(2+2)//4) 
print(10/2 - 3%2 + (3 + 2) * 5)
print(10//2 - 3%2 + (3 + 2) * 5)




#for integer output use '//'
print(4+4*3//6) 


# In[ ]:




