#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
df1=pd.read_excel('C:/Users/Administrator/Desktop/纳税主体.xlsx',sheet_name=0,converters={'identify_num':str,'telephone':str})
# print(df1.head())
a =[]
for aa in df1['纳税人性质']:
   if aa=='一般纳税人':
     a.append(1)
   else:
       a.append(0)
df1['e']=a
print(df1['e'])
# df1.to_excel('C:/Users/Administrator/Desktop/c.xlsx',index=False)


