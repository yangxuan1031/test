#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 匹配excel表格里两列不同的数据
#导入xlrd模块
import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
 #读取excel文件
#括号中的字符串为你要比较的两个excel的路径，注意用“/”
wb_a = openpyxl.load_workbook('C:/Users/Administrator/Desktop/1.xlsx')
wb_b = openpyxl.load_workbook('C:/Users/Administrator/Desktop/3.xlsx')
#定义一个方法来获取表格中某一列的内容，返回一个列表
#在这里，我的表格中：IP是具有唯一性的，所以我用它来区分数据的差异，而IP这一列在我的表格中是第“G”列
def getIP(wb):
    sheet = wb['纳税主体信息']
    ip = []
    for cellobj in sheet['B']:
        ip.append(cellobj.value)
    return ip

#获得某列数据
ip_a = getIP(wb_a)
ip_b = getIP(wb_b)

# 将两个列表转换成集合
aa = list(ip_a)
bb = list(ip_b)
print('777')
print(aa)
print(bb)
# tmp1=list(aa.union(bb))                 #并集  |
# tmp2=list(aa.intersection(bb))            # 交  &
# tmp4=list(aa.symmetric_difference(bb))    # 对称差
#  tmp3=list(set(aa).difference(set(bb)))        差 ^  先转set集合，list集合没有difference属性


tmp3=list(set(aa).difference(set(bb)))
tmp5=list(set(bb).difference(set(aa)))


#打印出列表中的元素
#到这一步，两个表格中不同的数据已经被找出来了
for i in tmp3:
    print(i)

for i in tmp5:
    print(i)

#将不同行高亮显示
print ("开始第一张表" + "----" *10)
a = wb_a['纳税主体信息']['B']
for cellobj in a:
    if cellobj.value in tmp3:
        print(cellobj.value)
        cellobj.font = Font(color=colors.BLACK, italic=True, bold=True)
        cellobj.fill = PatternFill("solid", fgColor="DDDDDD")
print ("开始第二张表" + "----" *10)
b = wb_b['纳税主体信息']['B']
for cellobj in b:
    if cellobj.value in tmp5:
        print(cellobj.value)
        cellobj.font = Font(color=colors.BLACK, italic=True, bold=True)

        cellobj.fill = PatternFill("solid", fgColor="DDDDDD")
wb_a.save('C:/Users/Administrator/Desktop/c.xlsx')
wb_b.save('C:/Users/Administrator/Desktop/d.xlsx')

