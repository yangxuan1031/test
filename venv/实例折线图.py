#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
df1=pd.read_excel('C:/Users/Administrator/Desktop/9132010566068652XY.xlsx',sheet_name=0)
plt.rcParams['font.family']='SimHei' # 设置中文字体
plt.rcParams['axes.unicode_minus']=False # 设置中文字体状态下负号（-）正常显示

x1=df1['invoice_date']
y1=df1['count(*)']
y2=df1['镇江']

figsize = 15,9
figure, ax = plt.subplots(figsize=figsize)
ax.yaxis.set_major_locator(MultipleLocator(50))
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['right'].set_position(('data',1))

# plt.xticks(rotation=90)
# plt.ylim(0, max(y1)) #设置x轴/y轴的范围。

# plt.plot(x1,y1,'o',label='9132010566068652XY')
# plt.plot(x1,y1,label='9132010566068652XY')
# plt.xlabel('9132010566068652XY')
# plt.ylabel('开票量')
# for x,y in enumerate(y1):
#     plt.text(x, y+10, "%s" %y,ha="center", va="bottom")

#第一图
ax1 = plt.subplot(121)
ax1.plot(x1,y1,'o')
plt.plot(x1,y1)
plt.xlabel('9132010566068652XY')
plt.ylabel('开票量')
for x,y in enumerate(y1):
    plt.text(x, y+10, "%s" %y,ha="center", va="bottom")
plt.xticks(rotation=90)
plt.ylim(0,350)
#箭头
plt.annotate('这是最大值',xy=('2020-05-23',335),xytext=('2020-05-15',300),arrowprops={'facecolor':'red','shrink':0.05})

#第二图
ax2 = plt.subplot(122)
ax2.plot(x1,y2,'o')
plt.plot(x1,y2)
plt.xlabel('9132101157143921XG')
plt.ylabel('开票量')
for x,y in enumerate(y2):
    plt.text(x, y+10, "%s" %y,ha="center", va="bottom")
plt.xticks(rotation=90)
plt.ylim(0,350)

plt.show()