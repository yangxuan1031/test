#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")

if __name__ == '__main__':
    print(get_desk_p())