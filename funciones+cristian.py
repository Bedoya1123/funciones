
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# $f(g) = (e^ {g}-e^ {-g})/(e^{g}+e^{-g})$

# In[6]:

g= np.linspace (-3,3)
e= np.e


# In[7]:

def f(g, e):
    return ((e**g)-(e**-g))/((e**g)+(e**-g))


# In[8]:

plt.plot(g, f(g, e))


# In[9]:

def c(g, e):
    return np.piecewise(g, (g<-e, g>e, g==0),(0, 2 , 5))


# In[10]:

plt.plot(g c(g, e))


# In[11]:

datos= np.arange(0,100)


# In[14]:

plt.plot(datos)


# In[17]:

trigo= np.arange(0,360)
trigo= np.radians(trigo)
trigo= np.sin(trigo)


# In[ ]:




# In[18]:

plt.plot(trigo)


# In[19]:

trigo= np.cos(trigo)


# In[20]:

plt.plot(trigo)


# In[ ]:



