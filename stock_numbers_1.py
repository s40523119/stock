
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2',encoding='big5hkscs')


# In[4]:

df2 = df[0]


# In[6]:

df2.columns = df2.iloc[0]


# In[8]:

df3 = df2.ix[2:]


# In[10]:

df4 = df3.drop([u'備註',u'國際證券辨識號碼(ISIN Code)',u'市場別','CFICode'],axis=1)


# In[16]:

df4.index = range(1, df4.index.size + 1)


# In[19]:

df4


# In[ ]:



