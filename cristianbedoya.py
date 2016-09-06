
# coding: utf-8

# In[5]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[11]:

g=np.arange(-5,5,0.3)


# $f(g)=g$
# 

# In[13]:

y=g


# In[15]:

plt.plot(g,y)
plt.grid()


# $f(h)=e^{h}-e^{-h}/e^{h}+e^{-h}$
# 

# In[17]:

h=np.linspace(-5,5)
e=np.e


# In[18]:

def f(h,e):
    return ((e**h)-(e**-h))/((e**h)+(e**-h))


# In[ ]:




# In[19]:

plt.plot(h, f(h,e))


# In[20]:

x=np.linspace(-5,5)
b=np.linspace(-4,4)


# In[21]:

def f(x,b):
    return np.piecewise(x,[x<-b, x > b],[0,1,5])


# In[25]:

plt.axis([x[0], x[-1], -0.1, 1.5])
plt.plot(x,f(x,b),linestyle='--',color='r')


# In[24]:

sigma=0.01
x=np.linspace(-10,10)
e=np.e
pi=np.pi


# $f(x)= 1 / \sqrt[2]{2\pi \sigma^2 }e^-(x^2/2 \sigma^2)$

# In[27]:

def f(x):
    return (1/np.sqrt(2*pi*sigma**2))*(e**-((x**2)/2*(sigma**2)))


# In[28]:

plt.plot(x,f(x),'--',color='g')


# In[ ]:



