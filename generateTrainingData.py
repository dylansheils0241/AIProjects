# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:50:49 2019

@author: Administrator
"""

import random

outFileNameA="C:\\Users\\Administrator\\Desktop\\AIProject\\XORdataX.txt"
outFileNameB="C:\\Users\\Administrator\\Desktop\\AIProject\\XORdataY.txt"
f=open(outFileNameA, "w+")
g=open(outFileNameB, "w+")


for i in range(1000):
    a = (random.randint(1, 100))
    b = (random.randint(1, 100))
    c = (a ^ b)
    f.write(str('{0:08b}'.format(a)) + str('{0:08b}'.format(b)) + "\r\n")
    g.write(str('{0:08b}'.format(a)) + "\r\n")
    
f.close()

print("Done")
