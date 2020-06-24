# -*- coding: utf-8 -*-
import csv
import numpy as np
import pandas as pd
#%%
rgb = list()
def RGB():
    levels = range(0,255)
    global rgb
    for r in levels:
        print(r)
        red = levels[r]
        for g in levels:
            green = levels[g]
            for b in levels:
                blue= levels[b]
                rgb.append(np.array([red, green,blue]))
    print('FIM RGB')

#%%
rgbN = rgb/256
def normal(color):
    for i in range(0,len(color)):
        print(i)
        rgbN[i][0] = float(color[i][0])/255.
        rgbN[i][1] = float(color[i][1])/255.
        rgbN[i][2] = float(color[i][2])/255.

#%%
rgbN.type = 'float32'
normal(rgbN)
rgbN
rgbN = rgb/255
RGB(0,256)
rgb = np.array(rgb)
rgb = pd.DataFrame(rgb,columns = ["R","G","B"])

#%%   
hexcd = list()    
def rgb2hex(color):
    global hexcd
    for i in range(0,len(color)):
        print(i)
        h = "{:02x}".format(color[i][0])
        e = "{:02x}".format(color[i][1])
        x = "{:02x}".format(color[i][2])
        new = "#" + str(h) + str(e) + str(x)
        hexcd.append(new)
    print('FIM HEX')
#%%
rgb2hex(rgb)
hexcd =  np.array(hexcd)
hexcd
#%%
cmyk=list()
cmyk = np.empty(shape = (16777216,4))
def rgb2cmyk(color):
    global rgb, cmyk
    for i in range(0,len(color)):
        print(i)
        r= round(color[i,0]/255, ndigits =4)
        g= round(color[i,1]/255, ndigits =4)
        b= round(color[i,2]/255, ndigits =4)
        k = min(r,g,b)
        if k  == 1. :
            cmyk[i,0] = 0.
            cmyk[i,1] = 0.
            cmyk[i,2] = 0.
            cmyk[i,3] = 1.
        else:
            cmyk[i,0]=(1-r)/1-k
            cmyk[i,1]=(1-g)/1-k
            cmyk[i,2]=(1-b)/1-k
            cmyk[i,3] = k
    print('FIM CMYK')
    
def twoCMYK(col):
    global rgbN, cmyk
    for i in range(0,len(col)):
        print(i)
        cp = 1 - col[i,0]
        mp = 1 - col[i,1]
        yp = 1 - col[i,2]
        kp = min(cp,mp,yp)
        cmyk[i,0] = min(1,max(0,cp-kp))
        cmyk[i,1] = min(1,max(0,mp-kp))
        cmyk[i,2] = min(1,max(0,yp-kp))
        cmyk[i,3] = min(1,max(0,kp))
#%%
twoCMYK(rgbN)
rgb2cmyk(rgb)
rgbN[16777216/2]
rgbN
rgb
cmyk
cmyk[([1000,10000,100000,1000000,10000000])]
cmyk = np.array(cmyk)
cmyk = np.delete(cmyk,(-0),axis=0)
cmykDb = pd.DataFrame(cmyk, columns=["C","M","Y","K"])

#%% Dataframing to join and export
rgb = pd.DataFrame(rgb, columns = ["R","G","B"])
rgb['hex'] = hexcd
cmyk = pd.DataFrame(cmyk, columns = ["C","M","Y","K"])
cmyk['hex'] = hexcd
ColorChart = rgb.merge(cmyk, on = 'hex', how = 'inner')
#%%    
#Function calling       
RGB(0,256)
rgb2hex(rgb)

#%%
with open('/home/luc/Dropbox/Academia/Python/hex.csv') as csvfile:
    hexdf = csv.reader(csvfile)
    hexcol = []    
    for row in hexdf:
        temp = row[0]
        hexcol.append(temp)
        hexcol = np.array(hexcol)
csvfile.close()
#%%
with open('/home/luc/Dropbox/Academia/Python/rgb.csv') as csvfile:
    rgbdf = csv.reader(csvfile)
    rgbcols = []    
    for row in rgbdf:
        r = row[0]
        g = row[1]
        b = row[2]
        rgbcols.append(np.array([r,g,b]))
        #rgbcols = np.array(rgbcols)
csvfile.close()
#%%
with open('/home/luc/Dropbox/Academia/Python/cmyk.csv') as csvfile:
    cmykdf = csv.reader(csvfile)
    cmykcols = []    
    for row in cmykdf:
        c = row[0:]
        m = row[1:]
        y = row[2:]
        k = row[3:]
        cmykcols.append(np.array([c,m,y,k]))
        #cmykcols = np.array(cmykcols)
csvfile.close()
#%% outputs

ColorChart = np.empty(shape=(16777216,0))
ColorChart[0:] = hexcol

np.savetxt('cmyk.csv',cmyk,delimiter=';', fmt='%s')
np.savetxt('rgbN.csv',rgbN,delimiter=';', fmt='%s')
np.savetxt('rgb.csv',rgb,delimiter=',', fmt='%s')
np.savetxt('hex.csv',hexcd,delimiter=',', fmt='%s')
ColorChart.to_csv('colorlist.csv', sep = ';', encoding = 'utf-8')