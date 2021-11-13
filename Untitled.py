#!/usr/bin/env python
# coding: utf-8

# In[2]:


#python dilinde kodları etkilemeyecek yorum satırı
print('hello world!')


# In[3]:


#python dilinde syntax
if(81<96):
    print('That is true.')


# In[5]:


#python değişkenler
x='Hello computer engineering b section group'
y=2
print(x,y)


# In[6]:


#Example of variable in python
studentnumber=26
print('There are',studentnumber,'students in b section.')


# In[7]:


#Variable types in python
x=int(8) #type of integer
y=str(8) #type of string
z=float(8) #type of float
print(x,y,z)


# In[10]:


#case sensitive
x='a'
X='A'
print('a,A')


# In[11]:


#describe function in python
def function():
    print('The function is working.')
function()


# In[12]:


# f(x) = x**2 fonksiyonunun f(1.2) değerini bulunuz
def f(x):
    return x**2
f(1.2)


# In[13]:


# Bakteri modeli olarak g(t)=3**t fonksiyonunu tanımlayın ve t=2.1 değerini hesaplayınız
def g(t):
    return 3**t
g(2.1)


# In[14]:


# İki sayının toplamını veren fonksiyonu yazınız
def f(x,y):
    return x+y
f(6,12)


# In[16]:


# İf yapısı örneği
# Senaryo: Fonksiyon parametresi 10'dan küçük ise doğru, değil ise yanlış

def  function(x):
    if(x>10):
        print(x,'is quarter than 10.')
    elif(x==10):
        print(x,'is equal to 10.')
    else:
        print(x,'is less than 10.')
              
function(9)


# In[17]:


# İki sayıyı karşılaştıran fonksiyon
def function(x,y):
    if(x<y):
        print(x,"<",y)
    elif(x==y):
        print(x,"=",y)
    else:
        print(x,">",y)
function(6,21)


# In[18]:


# İçine bir sayı girdiğinde tek ya da çift olduğunu bulan bir fonksiyon yazınız
# İpucu: % işareti iki sayıı bir birine bölümünden kalanı verir
def f(x):
    if(x%2==0):
        print('Bu sayı çift sayıdır.')
    else:
        print('Bu sayı tektir.')
        
f(9)        


# In[20]:


# f(x) = x**2 - 1
# g(x) = x**3 + 4
# (fog)(x) bileşke fonksiyonunu bulunuz

from sympy import *
x=Symbol('x')

def f(x):
    return x**2 - 1
def g(x):
    return x**3 + 4

expand(f(g(x)))


# In[21]:


expand(f(x)+g(x))


# In[22]:


expand(f(x)-g(x))


# In[23]:


expand(f(x)*g(x))


# In[24]:


expand(f(x) / g(x))


# In[25]:


#for döngüsü
dizi=[1,2,3,4]
for i in dizi:
    print(i)


# In[26]:


#range() komutu ile for döngüsü

for i in range(1,80,2):
    print(i)


# In[27]:


# 1'den 26'ya kadar olan tek ve çift sayıların toplamını bulunuz
# İpucu: += operatörü bir önceki değişkenin üzerine ekleyerek toplar
def cifttoplam():
    sonuccift=0
    for i in range(1,26):
        if(i%2==0):
            sonuccift +=i
    return sonuccift

cifttoplam()


# In[28]:


def tektoplam():
    sonuctek=0
    for i in range(1,26,2):
        sonuctek +=i
    return sonuctek
tektoplam()


# In[29]:


cifttoplam()+tektoplam()


# In[30]:


x=3
print(x)


# In[31]:



y='string is a variable'
print(y)


# In[32]:


def f(x):
    return x**2
f(4)


# In[33]:


def g(x):
    return x**3+1
g(4)


# In[34]:


f(g(4))


# In[35]:


import sympy as sp
x=sp.Symbol('x')

f(x+1)


# In[36]:


sp.expand(f(g(x)))

def f(a,islem):
    if(islem=='karesi'):
        return a**2
    elif(islem=='kupu'):
        return a**3
    else:
        return a
f(3,'kupu')


# In[40]:


#iki sayının +,-,*,/ işlemlerinin yapan tek bir fonksiyon yazınız
def f(x,y,islem):
    if(islem == 'toplama'):
        return x + y
    elif(islem == 'cıkartma'):
        return x - y
    elif(islem == 'carpma'):
        return x * y
    elif(islem == 'bolme'):
        return x / y
    


# In[42]:


f(9,3,'bolme')


# In[43]:


f(9,3,'toplama')


# In[46]:


f(9,3,'carpma')


# In[48]:


f(9,3,'cıkartma')


# In[49]:


(3*4)**(0.5)


# In[50]:


import math

def f(x,islem):
    if(islem=='faktöriyel'):
        return math.factorial(x)
f(3,'faktöriyel')


# In[61]:


def tctoplam(n):
    ttoplam=0
    ctoplam=0
    gtoplam=0
    for i in range(1,n+1):
        if(i % 2 == 0):
            ctoplam = ctoplam+i
        if(i % 2==10):
            ttoplam =ttoplam+i
            gtoplam =gtoplam+i
    return[gtoplam,ctoplam,ttoplam]
        
tctoplam(20)        


# In[62]:


def t(n):
    return (n*(n+1))/2
t(20)


# In[63]:


#bir sayının asal sayı olup olmadığını kontrol edecek fonksiyon yaz.
#break sonucu  bulduğunda dur demek

def asalmi(n):
  for i in range(1,n):
      if(math.gcd(n,i) != 1):
        print('Asal değil !')
        break
  else:
    print('Asal sayı !')

asalmi(17)


# In[ ]:




