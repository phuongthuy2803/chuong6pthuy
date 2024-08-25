# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:56:52 2024

@author: Student
"""

cau= 'Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM'
print(cau.split(","))
a= cau.replace("P.", "").replace("Q.", "").replace("Tp.", "")
print(a.split(","))