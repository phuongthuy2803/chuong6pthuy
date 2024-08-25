# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:11:34 2024

@author: Student
"""

import math
a= float(input("Nhập số a: "))
b= float(input("Nhập số b: "))
print("Giá trị biểu thức bằng ", ((math.sqrt(a)-math.sqrt(b))/((a**1/4)-(b**1/4)))-((math.sqrt(a)-((a*b)**1/4))/((a**1/4)+(b**1/4))))