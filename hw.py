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
                a[y,x]=255
            else:
                a[y,x]*=1.1
    plt.imshow(a,cmap='gray')
    plt.axis('off')
    plt.show()
    
print(lighten(array1))

#2
def flip(a):
    plt.imshow(a[0::,::-1],cmap='gray')
    plt.axis('off')
    plt.show()

print(flip(array1))
#3
def clip(maxval,a):
    b=len(a)
    l=[]
    for i in a:
        c=len(i)
        l.append(c)
    
    for y in range(b):
        for x in range(c):
            if a[y,x]>maxval:
                a[y,x]=maxval
    plt.imshow(a,cmap='gray')
    plt.axis('off')
    plt.show()
    
print(clip(200,array1))