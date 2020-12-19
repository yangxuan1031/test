#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd


# python+pandas 保存list到本地
def deal():
    # 二维list
    company_name_list = [['腾讯', '北京'], ['阿里巴巴', '杭州'], ['字节跳动', '北京']]

	# list转dataframe
    df = pd.DataFrame(company_name_list, columns=['company_name', 'local'])

	# 保存到本地excel
    df.to_excel("C:/Users/Administrator/Desktop/b.xlsx", index=False)


if __name__ == '__main__':
    deal()