
# coding: utf-8

# In[377]:


import requests 
import re
import numpy as np
import datetime 
import json
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
#載入所需模組
def stock(stock_id, cycle): #自訂股票函式
    cycle = 'https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=' + cycle +'&mkt=10&sym=' + stock_id
    r = (requests.get(cycle).text) #透過requests的get，抓取目標網頁
    global day_volume #宣告 day_volume 為全域變數
    day_volume = r[563:-4] #利用slice擷取需要的部分
    #print(day_volume)
time = re.findall('\d\d\d\d\d\d\d\d', day_volume)[1:] #用re擷取日期 
close = re.findall('"c":\d*.\d*', day_volume)
high = re.findall('"h":\d*.\d*', day_volume)
low = re.findall('"l":\d*.\d*', day_volume)
volume = re.findall('"v":\d*.\d*', day_volume)
open = re.findall('"o":\d*.\d*', day_volume)
data = re.findall(r'{"t":\d{8},".":\d*.\d*,".":\d*.\d*,".":\d*.\d*,".":\d*.\d*,".":\d*.\d*}', day_volume)
date_list = [datetime.datetime.strptime(t, '%Y%m%d') for t in time]
c = [close.replace('"c":', '') for close in close]
h = [high.replace('"h":', '') for high in high]
l = [low.replace('"l":', '') for low in low]
v = [volume.replace('"v":', '') for volume in volume]
o = [open.replace('"o":', '') for open in open]

stock('0056', 'd')

# prepare some data
x = [datetime.datetime.strptime(t, '%Y%m%d') for t in time]
y = c

# output to static HTML file
#output_file("lines.html")

# create a new plot with a title and axis labels
TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
p = figure( title="元大高股息日線", x_axis_label=u'日期', y_axis_label=u'收盤價')

# add a line renderer with legend and line thickness
p.line(x, y, legend=u"元大高股息.", line_width=2)
p.xaxis.formatter=DatetimeTickFormatter(formats=dict(
        hours=["%Y-%m-%d"],
        days=["%Y-%m-%d"],
        months=["%Y-%m-%d"],
        years=["%Y-%m-%d"],
    ))

p.xaxis.major_label_orientation = 180/4

# show the results
show(p)
        
    
    
    
    


