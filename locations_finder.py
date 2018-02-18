# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 12:23:54 2017

@author: IBM
"""
import numpy
import numpy as np
import scipy.io
mat = scipy.io.loadmat('cntmatrix.mat')
a=mat.values()
q=a[0]
newmat=numpy.zeros((28,28))
for i in range(0,28):
    for j in range(0,28):
        #print(i)
        newmat[i,j]=q[i,j]+q[j,i]
global locs
#locs=numpy.load('stora.npy')
locs=numpy.zeros([2L,28L])
locs[0]=alllocsx
locs[1]=alllocsy

import matplotlib.pyplot as plt
plt.figure()
plt.scatter(locs[0],locs[1])

        
def dists(x1,y1,x2,y2):
    dy=abs(y2-y1)
    dx=abs(x2-x1)
    out=math.sqrt(math.pow(dy,2)+math.pow(dx,2))
    return out
def ind2pnts():
    pass
def dist(i,j):
        x1=locs[0,i]
        x2=locs[0,j]
        y1=locs[1,i]
        y2=locs[1,j]
        dista=dists(x1,y1,x2,y2)
        return dista
summi=0
for i in range (0,28):
    for j in range(0,28):
        if i>j:
            summi=summi+newmat[i,j]*dist(i,j)


teninds=[0,10,6,5,13,1,27,15,14,2,25]
circ1x=locs[0,0:11]
circ1y=locs[1,0:11]
def summer(inds):
    out=0
    for i in range(len(inds)):
        for j in range(len(inds)):
            if i>j:
                out=out+newmat[inds[i],inds[j]]*dist(inds[i],inds[j])
                
    return out

summer(teninds)