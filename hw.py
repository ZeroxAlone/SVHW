from PIL import Image, ImageDraw
import numpy as np

value_color = 80

dic_color = {}

list_color_value = []
while value_color <= 255:
    list_color_value.append(int(value_color))
    value_color = value_color * 1.1

arr=np.array([80,80,255,80,80,255,80,80,
              80,80,255,80,80,255,80,80,
              255,80,120,120,120,120,255,80,
              255,80,255,255,255,255,80,80,
              255,80,120,120,120,120,80,80])


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

def dictionary_value_color(dic, name, value):
        dic[name] = value
    
        return dic
    
def fill(im,x,y,ar):
    xi=x
    draw = ImageDraw.Draw(im)
    s=x*y  
    for o in range(s):
        for p in list(ar):
            c=p
            for e in range((x-1)*100,x*100):
                for d in range((y-1)*100,y*100):
                        draw.point((e,d),c)
            dictionary_value_color(dic_color, str(x)+str(y), c)
            x-=1
            if x==0:
                y-=1
                x=xi
    return im.show()
print(fill(im,8,5,arr))
print(line(8,5))


#########################################################
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
                print("(",x,",",y,")",":",True)
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
