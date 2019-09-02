# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:35:38 2019

@author: lisa_
"""

from PIL import Image, ImageDraw
import numpy as np
import random

value_color = 80

dic_color = {}
def lighten(list1):
    list_color_value = []
    for i in list1:
        list_color_value.append(i*1.1)
    return list_color_value
    
l=[80,80,255,80,80,255,80,80,
   80,80,255,80,80,255,80,80,
   255,80,120,120,120,120,255,80,
   255,80,255,255,255,255,80,80,
   255,80,120,120,120,120,80,80]

im=Image.new('L',(801,501),255)

def line(x,y):
    draw = ImageDraw.Draw(im)
    cx=0
    cy=0
    for i in range(y+1):
        draw.line((cx,cy,x*100,cy),0)
        cy+=100
    cy=0
    for o in range(x+1):
        draw.line((cx,cy,cx,y*100),0)
        cx+=100
    cx=0
    return im

def fill(im,x,y):
    xi=x
    draw = ImageDraw.Draw(im)
    s=x*y  
    for o in range(s):
        c=random.choice(l)
        for e in range((x-1)*100,x*100):
            for d in range((y-1)*100,y*100):
                    draw.point((e,d),c)
        x-=1
        if x==0:
            y-=1
            x=xi
    return im

print(fill(im,8,5))
print(line(8,5))
im.show()
lighten(l)
print(fill(im,8,5))
print(line(8,5))
im.show()