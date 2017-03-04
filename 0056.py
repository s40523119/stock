# -*- coding: utf-8 -*-
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
close = re.findall('"c":\d*.\d*', day_volume) #用re擷取收盤價
high = re.findall('"h":\d*.\d*', day_volume) #用re擷取最高價
low = re.findall('"l":\d*.\d*', day_volume) ##用re擷取最低價
volume = re.findall('"v":\d*.\d*', day_volume) #用re擷取成交量
open = re.findall('"o":\d*.\d*', day_volume) #用re擷取開盤價
data = re.findall(r'{"t":\d{8},".":\d*.\d*,".":\d*.\d*,".":\d*.\d*,".":\d*.\d*,".":\d*.\d*}', day_volume) #用re擷取出json區段
date_list = [datetime.datetime.strptime(t, '%Y%m%d') for t in time] #用datetime將time 轉成 datetime
c = [close.replace('"c":', '') for close in close] #用.replace將"c":取代成空字串
h = [high.replace('"h":', '') for high in high] #用.replace將"h":取代成空字串
l = [low.replace('"l":', '') for low in low] #用.replace將"l":取代成空字串
v = [volume.replace('"v":', '') for volume in volume] #用.replace將"v":取代成空字串
o = [open.replace('"o":', '') for open in open] #用.replace將"o":取代成空字串

stock('0056', 'd') 

# 準備圖表資料
x = date_list
y = c

# 輸出html
#output_file("lines.html")

# 建立圖表
TOOLS="resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
p = figure( title="元大高股息日線", x_axis_label=u'日期', y_axis_label=u'收盤價')

# 加入變數
p.line(x, y, legend=u"元大高股息.", line_width=2) #圖例、線粗
p.xaxis.formatter=DatetimeTickFormatter(formats=dict(
        hours=["%Y年-%m月-%d日"],
        days=["%Y年-%m月-%d日"],
        months=["%Y年-%m月-%d日"],
        years=["%Y年-%m月-%d日"],
    )) #設定時間格式

p.xaxis.major_label_orientation = 180/4 #旋轉X軸

# 顯示結果
show(p)
        
    
    
    
    

