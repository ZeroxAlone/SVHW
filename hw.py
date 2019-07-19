# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:07:05 2019

@author: translucky
"""

import matplotlib.pyplot as plt
import numpy as np



array1=np.array([[80,80,255,80,80,255,80,80],
              [80,80,255,80,80,255,80,80],
              [255,80,120,120,120,120,255,80],
              [255,80,255,255,255,255,80,80],
              [255,80,120,120,120,120,80,80]])


#1
def lighten(a):
    b=len(a)
    l=[]
    for i in a:
        c=len(i)
        l.append(c)
    
    for y in range(b):
        for x in range(c):
            if a[y,x]==255:
                a[y,x]=True
            else:
                a[y,x]*=1.1
    plt.imshow(a,cmap='gray')
    plt.axis('off')
print(lighten(array1))
#print(len(a[0]))
#2
'''上下翻转 
def flip(array):
    return array[::-1]
print(flip(a))
''' 
#3
def clip_the_image(maxval):
    vmax=maxval
