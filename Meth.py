#содержит основные методы(блоки)
#
#
#

import sys
##import time
##from vec2d import *
##import math
##from Tkinter import * 
##import ttk
##import mlpy
##import numpy as np
##import matplotlib.pyplot as plt
##import DotsL
from math import trunc
from AdditionalTools import *
AnalizConteiner={}
FilterContainer={}
VisualContainer={}

class Container():
    def __init__(self):
        self.Name=''
        self.Params={}
        self.ParaNames=[]
        self.Input=[]
        self.Output=[]
        self.Descr=''
    def Method():
        pass
name=0
params=[]
descr=''
Input=['In']
Output=['Out']
def assemble(Type,Name=name,Method=0,Params=params,InPut=Input,OutPut=Output,Description=descr):
    a=Container()
    a.ParaNames=Params#list.copy(Params)
    for i in Params:
        a.Params[i]=0
    a.Input=Input
    a.Output=OutPut
    a.Method=Method
    a.Name=Name
    a.Descr=Description
    if Type==1:
        AnalizConteiner[Name]=a
    if Type==2:
       FilterContainer[Name]=a
    if Type==3:
        VisualContainer[Name]=a
######


name='PlusString'
descr='Add strint to Input'
params=['String']
Input=['In']
Output=['Out']
def method(self):
    OutPut=self.Get('In')+self.Params['String']
    self.Send('Out',OutPut)
assemble(2,name,method,params,Input,Output,descr)
######################################3
name='TripleConcatenation'
descr='Concatenatestrings'
Input=['In1','In2','In3']
Output=['Out']
def method(self):
    OutPut=self.Get('In1')+self.Get('In2')+self.Get('In3')
    self.Send('Out',OutPut)
assemble(2,name,method,params,Input,Output,descr)
######################################3
######################################
name='String Input'
descr='Stat Input with a string'
params=['String']
Output=['Out']
Input=[]
def method(self):
    OutPut=self.Params['String']
    self.Send('Out',OutPut)
assemble(1,name,method,params,Input,Output,descr)
########################################
name='StringVisualOutPut'
descr='Show you the Current Output. Takes str and int Input. You Can Change It'
params=[]
Input=['In']
Output=[]
def method(self):
    
    root = Tk()
    Text1=Text(root ,font=('times',10),width=50,height=1,wrap=WORD)
    Text1.insert(1.0,self.Get('In'))
    Text1.pack()
    root.mainloop()
assemble(3,name,method,params,Input,Output,descr)
###############################################
###############################################
name='Generating Array'
descr='Stat Input with a string'
params=['Dimensions','DotAmount']
Input=[]
Output=['Out']
def mDatageneration(self):
##    if self.Params['Seed']!=0:
##        np.random.seed(int(self.Params['Seed']))
##    else:
    np.random.seed()
    mean, cov=[],[]
    for i in range(int(self.Params['Dimensions'])):
        mean.append(random.randrange(1,5))
    for i in range(int(self.Params['Dimensions'])):
        c=[]
        for i in range(int(self.Params['Dimensions'])):
            c.append(random.randrange(1,5))
        cov.append(c)
    print ('aadad')
    print mean,cov
    #mean1, cov1, n1 = [2, 8], [[1,1],[1,2]], 250 # 200 points, mean=(1,5)
    x = np.random.multivariate_normal(mean, cov, int(self.Params['DotAmount']))
    print x

    self.Send('Out',copy.deepcopy(x))

assemble(1,name,mDatageneration,params,Input,Output,descr)    

###############################################
name='Clusterisation'
descr='Stat Input with a string'
params=['k']
Input=['Array']
Output=['OutArray','Groups']
def method(self):   
    x=self.Get('Array')
    k=int(self.Params['k'])
    cls, means, steps = mlpy.kmeans(x, k, plus=True)
    print cls
    self.Send('OutArray',copy.deepcopy(x))
    self.Send('Groups', cls)


assemble(2,name,method,params,Input,Output,descr)


##############################################
name='PCA'
descr='Stat Input with a string'
params=['k']
Input=['Array']
Output=['OutArray']
def method(self):
    x=self.Get('Array')
    k=int(self.Params['k'])
    PCA=mlpy.PCA()
    PCA.learn(x)
    coeff = PCA.coeff()
    z = PCA.transform(x, k) # transform x using the first PC
    print 'x:'
    print x
    print 'z:'
    print z
    xnew = PCA.transform_inv(z) # transform data back to its original space
    self.Send('OutArray', z)
assemble(2,name,method,params,Input,Output,descr)

name='DimensionalVisualisation'
descr='aafafaff'
params=[]
Input=['Array','ColorVec']
Output=['OutArray']
def method(self):
    x=self.Get('Array')
    x=NTAoL(x)
    DotsL.VisualProjection(x, self.Get('ColorVec'))
assemble(3,name,method,params,Input,Output,descr)

name='Classification'
descr='afff'
params=[]
Input=['Array','TrainingArray']
Output=['OutArray','Labels']
def method(self):
    x=self.Get('Array')

    y=self.Get('TrainingArray')
    print ('x')
    Group1=[]
    Group2=[]
    for i in range(len(y)):
        if y[i]==0:
            Group1.append(x[i])
        elif y[i]==1:
            Group2.append(x[i])
    X=[]
    Y=[]
    print 'G'
    print Group1
    print Group2
    for i in range(trunc(len(Group1)/10)+1):
        X.append(Group1[i])
        Y.append(0)
    for i in range(trunc(len(Group2)/10)+1):
        X.append(Group2[i])
        Y.append(1)
    print (X)
    print (Y)
    knn = mlpy.KNN(k=2)
    knn.learn(X, Y)
    print ('Res')
    print knn.pred(x)

assemble(2,name,method,params,Input,Output,descr)

