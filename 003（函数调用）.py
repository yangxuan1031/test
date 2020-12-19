#!/usr/bin/python
# -*- coding: UTF-8 -*-
def hello():
    print('这是我们的世界')
def helloAgain():
    for i in range(2):
        hello()
if __name__=='__main__':
    helloAgain()