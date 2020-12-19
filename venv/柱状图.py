#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import os.path
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def get_bar():
   df1=pd.read_excel('C:/Users/Administrator/Desktop/航信失败问题.xlsx',sheet_name=0)
   plt.rcParams['font.family']='SimHei' # 设置中文字体
   plt.rcParams['axes.unicode_minus']=False # 设置中文字体状态下负号（-）正常显示
   x1=df1['msg']
   y1=df1['汇总']
   figsize = 15,20
   figure, ax = plt.subplots(figsize=figsize)
   plt.xticks(rotation=90)
   plt.bar(x1, y1, label="问题统计", color='red')
   for x, y in enumerate(y1):
       plt.text(x, int(y)+1, "%s" %y, ha="center", va="bottom")
   plt.legend()
   # figsize = 25,10
   # figure, ax = plt.subplots(figsize=figsize)
   # b = ax.barh(range(len(x1)), y1, color='#6699CC')
   #为横向水平的柱图右侧添加数据标签。
   # for rect in b:
   #     w = rect.get_width()
   #     ax.text(w, rect.get_y()+rect.get_height()/2, '%d' %
   #          int(w), ha='left', va='center')
    #设置Y轴纵坐标上的刻度线标签。
   # ax.set_yticks(range(len(x1)))
   # ax.set_yticklabels(x1)
   # 不要X横坐标上的label标签。
   # plt.xticks(())
   aa=os.path.join(os.path.expanduser('~'),"Desktop")
   plt.savefig(aa+'\柱状图.png')
   plt.show()
if __name__ == '__main__':
    get_bar()
