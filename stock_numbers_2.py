
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

url = ('http://isin.twse.com.tw/isin/C_public.jsp?strMode=4')


# In[4]:

df = pd.read_html(url)


# In[10]:

df2 = df[0]


# In[17]:

df2.columns = df2.iloc[0]


# In[27]:

df3 = df2.ix[2:]


# In[29]:

df4 = df3.drop([u'備註',u'國際證券辨識號碼(ISIN Code)',u'市場別','CFICode',u'產業別'],axis=1)


# In[31]:

df4.index = range(1, df4.index.size + 1)


# In[32]:

df4


# In[33]:

df4.to_excel('stock_numers_2.xlsx')


# In[ ]:



