#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
df1=pd.read_excel('C:/Users/Administrator/Desktop/test1.xlsx',sheet_name=0)
plt.rcParams['font.family']='SimHei' # 设置中文字体
plt.rcParams['axes.unicode_minus']=False # 设置中文字体状态下负号（-）正常显示
# plt.subplot(1,1,1)
# x=[1,2,3,4,5,6,7,8,9]
# y=[7,8,10,14,9,20,19,4,11]
# plt.ylabel('工单量')
# plt.title('sla数据')
# plt.plot(x,y)
# plt.show()
# df1.plot(x='税号',y=['电脑端','住这儿','黑猫二号','普通纸质','专用纸质'],title='东莞目前开票量',figsize=(12,4))
x1=df1['税号']
y1=df1['电脑端']
y2=df1['住这儿']
y3=df1['黑猫二号']
y4=df1['普通纸质']
y5=df1['专用纸质']
y6=df1['全部开票量']

figsize = 15,12
figure, ax = plt.subplots(figsize=figsize)
# xmajorLocator   = MultipleLocator(1) #将x主刻度标签设置为n的倍数
# xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式
# ax.xaxis.set_major_locator(xmajorLocator)
# ax.xaxis.set_major_formatter(xmajorFormatter)

ax.yaxis.set_major_locator(MultipleLocator(50))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['right'].set_position(('data',1))
plt.xticks(rotation=90)
# # xx = range(0,2000,100)
# # plt.yticks(xx)
# plt.xlim(min, max) / plt.ylim(min, max) 设置x轴/y轴的范围。
# plt.xticks(range(0, 23, 2))  # 设置X轴坐标点的值，为[0， 22]之间的以2为差值的等差数组

#折线图
plt.plot(x1,y1,label='电脑端开票量')
plt.plot(x1,y2,label='住这儿开票量')
plt.plot(x1,y3,label='黑猫二号开票量')
plt.plot(x1,y4,label='普通纸质开票量')
plt.plot(x1,y5,label='专用纸质开票量')
plt.xlabel('税号')
plt.ylabel('开票量')
for x,y in enumerate(y1):
    plt.text(x, y+1, "%s" %y,ha="center", va="bottom")
plt.legend()
#柱状图统计各税号的全部开票量
# plt.bar(x1,y6,align = 'center',color = 'y',edgecolor = 'r')
# plt.xlabel('税号')
# plt.ylabel('全部开票量')
# for x,y in enumerate(y6):
#     plt.text(x, y+30, "%s" %y,ha="center", va="bottom")
plt.savefig('C:/Users/Administrator/Desktop/g.png')
plt.show()


