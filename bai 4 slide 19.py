# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:18:41 2024

@author: Student
"""

x= int(input("Nhập giờ:"))
y= int(input("Nhập phút: "))
z= int(input("Nhập giây: "))
if 0<=x<=24 and 0<=y<=60 and 0<=z<=60:
    print("Tổng số giây là ", (x*3600)+(y*60)+z)
else:
    print("Thời gian không xác định")