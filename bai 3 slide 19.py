# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:10:00 2024

@author: Student
"""

N= int(input("Nhập số nguyên dương N có 2 chữ số: "))
if N>=10 and N<=99:
    x= N//10
    y= N%10
    print("Tổng các chữ số của N là ", x+y)
else:
    print("Nhập lại số nguyên dương N có 2 chữ số!")