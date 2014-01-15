#Переделанный модуль многомерных проэкций, ужасно но все-же подогнан для работы в качестве метода(Блока)
#, дополнительная подгонка в Юните Meth.py
#
#
#
#
# -*- coding: cp1251 -*-

from pygamehelper import *
from pygame import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
import math
import random
from Gui import *

##

GrCol=((0,0,0),(255,0,0),(0,255,0),(0,0,255))
class Instruments():
    def __init__(self,screen):
        self.screen=screen
        self.Current=0
        self.Img=pygame.surface.Surface((100,300))
        self.Img.fill((255,255,255))
        self.Tools=[]
        self.Buttons=[]
    def Draw(self,pos):
        self.screen.blit(self.Img,(pos))
    def ReDraw(self):
        i=0
        for a in self.Tools:
            self.Img.blit(a.Img,(10,10+40*i))
            i+=1
            
class Instrument():
    def __init__(self,screen):
        self.screen=screen
        self.Img=pygame.image.load(self.IconPath)
        self.Colour=(0,0,0)
    def Draw(self,pos,but):
        pass
    def DrawOnCur(self,pos):
        pass
class NmerChoose(Instrument):
    def __init__(self,screen):
        self.Rang=10
        self.Descr=''
        self.IconPath='RectChoose.bmp'
        Instrument.__init__(self,screen)
    def Choose(self,pos):
        for i in s.agents:
            if (i.pos.x>pos.x-5) and (i.pos.x<pos.x+5) and (i.pos.y>pos.y-5) and (i.pos.y<pos.y+5):
                i.Group=2
                for a in s.agents:
                    Z=0
                    for q in range(len(a.Atributes)):
                        Z+=abs(a.Atributes[q]-i.Atributes[q])^2
                    Z=math.sqrt(Z)
                    if Z<self.Rang:
                        a.Group=1
                break
    def DrawOnCur(self,pos):
        if s.Keys!=0:
            if s.Keys[K_EQUALS]:
                self.Rang+=1
            if s.Keys[K_MINUS]:
                self.Rang-=1
        Pos=vec2d(pos)
        pygame.draw.circle(self.screen,self.Colour,(Pos),(self.Rang),1)
        Mouse=pygame.mouse.get_pressed()
        if Mouse[0]:
            self.Choose(Pos)

class Zoom(Instrument):
    def __init__(self,screen):
        self.Descr=''
        self.IconPath='Zoom.bmp'
        Instrument.__init__(self,screen)
        self.Zoom=2
        self.ZoomRang=vec2d(100,50)
    def Draw(self,pos,but):
        Pos=vec2d(pos-self.ZoomRang/2)
        pygame.draw.rect(self.screen,self.Colour,((Pos),(self.ZoomRang)),2)
        self.screen.fill((255,255,255),((Pos+self.ZoomRang),(self.ZoomRang*self.Zoom)))
        pygame.draw.rect(self.screen,self.Colour,((Pos+self.ZoomRang),(self.ZoomRang*self.Zoom)),2)
        for i in s.agents:
            if i.pos.x>Pos.x and i.pos.y>Pos.y:
                if i.pos.x<Pos.x+self.ZoomRang.x and i.pos.y<Pos.y+self.ZoomRang.y:
                    x=math.trunc(Pos.x+self.ZoomRang.x+(i.pos.x-Pos.x)*self.Zoom)
                    y=math.trunc(Pos.y+self.ZoomRang.y+(i.pos.y-Pos.y)*self.Zoom)
                    pygame.draw.circle(self.screen, GrCol[i.Group], (x,y), 2)
##        for i in s.Sagents:
##            if i.pos.x>Pos.x and i.pos.y>Pos.y:
##                if i.pos.x<Pos.x+self.ZoomRang.x and i.pos.y<Pos.y+self.ZoomRang.y:
##                    x=math.trunc(Pos.x+self.ZoomRang.x+(i.pos.x-Pos.x)*self.Zoom)
##                    y=math.trunc(Pos.y+self.ZoomRang.y+(i.pos.y-Pos.y)*self.Zoom)
##                    pygame.draw.circle(self.screen, GrCol[i.Group], (x,y), 2)
    def DrawOnCur(self,pos):
        if s.Keys!=0:
            if s.Keys[K_EQUALS]:
                self.ZoomRang+=vec2d(2,1)
            if s.Keys[K_MINUS]:
                self.ZoomRang-=vec2d(2,1)
        Pos=vec2d(pos-self.ZoomRang/2)
        pygame.draw.rect(self.screen,self.Colour,((Pos),(self.ZoomRang)),1)
        Mouse=pygame.mouse.get_pressed()
        if Mouse[0]:
            self.Draw(pos,Mouse[0])
class RectChoose(Instrument):
    def __init__(self,screen):
        self.Rang=vec2d(100,50)
        self.Descr=''
        self.IconPath='RectChoose.bmp'
        Instrument.__init__(self,screen)
    def Choose(self,pos):
        for i in s.agents:
            if (i.pos.x>pos.x) and (i.pos.x<pos.x+self.Rang.x) and (i.pos.y>pos.y) and (i.pos.y<pos.y+self.Rang.y):
                i.Group=1
    def UnChoose(self,pos):
        for i in s.agents:
            if (i.pos.x>pos.x) and (i.pos.x<pos.x+self.Rang.x) and (i.pos.y>pos.y) and (i.pos.y<pos.y+self.Rang.y):
                i.Group=0
    def DrawOnCur(self,pos):
        if s.Keys!=0:
            if s.Keys[K_EQUALS]:
                self.Rang+=vec2d(2,1)
            if s.Keys[K_MINUS]:
                self.Rang-=vec2d(2,1)
        Pos=vec2d(pos-self.Rang/2)
        pygame.draw.rect(self.screen,self.Colour,((Pos),(self.Rang)),1)
        Mouse=pygame.mouse.get_pressed()
        if Mouse[0]:
            self.Choose(Pos)
        elif Mouse[2]:
            self.UnChoose(Pos)
            
##

class ScrolAgent: #управляющие точки из положениякоторых определяются коэфиценты линейной комбинации исходных точек на графике
    
    def __init__(self):
        self.Pause=False
        self.pos= vec2d(0,0)
        self.target= vec2d(0,0)
    def Go(self):
        self.Pause=False
        direct= self.target-self.pos
        if direct.length<3:
            self.Pause=True
        if direct.length>3:
            direct.length= 3
            self.pos=self.pos+direct
        

class Agent:    #исходные точки на графике
    def __init__(self):
        self.pos= vec2d(0,0)
        self.Atributes=[]
        self.Group=0
        self.Visible=True
        self.InUse=0


class Starter(PygameHelper):
    def __init__(self,Width,Height):
        Artibutes=[]
        self.w, self.h = Width, Height #размеры экрана
        self.main_1=vec2d(10,10)
        self.main_2=vec2d(Width-220,Height-100)
        self.nav_1=vec2d(200,200)
        self.nav_2=vec2d(Width-225+20,10)
        self.circleCenter=vec2d(self.nav_2+self.nav_1/2)
        self.Keys=0
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        self.screen=pygame.display.set_mode((self.w, self.h),(pygame.RESIZABLE))
        self.agents= []
        #self.Sagents= []
        self.phases=[]

        n=0
        self.LeftUp=vec2d(0,0)
        self.RightDown=vec2d(0,0)
        self.Radius=0
        self.Chosen=[]
        self.CurrentTool=0
        #
        self.border=vec2d(0,0)
        self.Xdot=ScrolAgent()
        self.Ydot=ScrolAgent()
        self.Pause=False
        self.CX=[]
        self.CY=[]
        self.Center=vec2d(0,0)
        self.CirAtr=[]   #of Agent()
        self.NSA=1    
        self.ZoomPos=0 #111
        self.Instruments=Instruments(self.screen)
        self.Instruments.Tools.append(Zoom(self.screen))
        self.Instruments.Tools.append(RectChoose(self.screen))
        self.Instruments.Tools.append(NmerChoose(self.screen))
        self.Instruments.ReDraw()
        self.Instruments.Current=self.Instruments.Tools[1]
        
    def LoadBase(self,Input1,Input2):
        user='user1'
        paswd='USER1'
        ip='@10.1.75.168'
        sd='orcl'
        connectstr=user+'/'+paswd+ip+'/'+sd
        db1 = cx_Oracle.connect(connectstr)
        db2 = cx_Oracle.connect(connectstr)
        cur1=db1.cursor()
        cur2=db2.cursor()
        table='resultat'
        all='select * from '+table+' where rownum<1000'
        self.countq=2        
        if NSA==1:
            bad=Input
            cur2.execute(bad)
            
        good=Input2
        cur1.execute(good)
        
        for i in cur1:
            a=Agent()
            self.agents.append(a)
        print('Agents Loaded!')
        if NSA==1:
            for i in cur2:
                a=Agent()
                self.Sagents.append(a)
            print('SAgents Loaded!')


        for i in range(len(self.agents[0].Atributes)):
            self.CX.append(0)
            self.CY.append(0)
            self.CirAtr.append(Agent())
        print(self.CX,self.CY)
        self.initText()
        
        

    def NormalizeAtributes(self,Target,MaxSize):
        maxx=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
        for i in range(len(Target[0].Atributes)):           
            for j in Target:
                if maxx[i]<j.Atributes[i]:
                    maxx[i]=j.Atributes[i]
        print(maxx)
        for i in range(len(Target[0].Atributes)):           
            for j in Target:
                j.Atributes[i]/=maxx[i]/MaxSize 
               
    def initText(self):
        self.font=pygame.font.Font(None,20)
        self.text=[]
        self.Xtext=0
        self.Ytext=0
        for i in range(len(self.agents[0].Atributes)):
            self.text.append(self.font.render('a'+str(i),True,(66,130,225)))
        self.Xtext=self.font.render('X=',True,(0,255,0))
        self.Ytext=self.font.render('Y=',True,(255,0,0))

    def CoefNormalize(self):
        summX=0.0
        summY=0.0
        for i in range(len(self.CX)):
            summX+=self.CX[i]
            summY+=self.CY[i]
        for i in range(len(self.CX)):
            if summX>0:
                self.CX[i]/=summX
                self.CX[i]=round(self.CX[i],4)
            if summY>0:
                self.CY[i]/=summY
                self.CY[i]=round(self.CY[i],4)

    def keyDown(self, key):
        if key-49<len(self.Instruments.Tools):
            self.Instruments.Current=self.Instruments.Tools[key-49]


    def SetCoeffs(self):
        n=0
        for i in self.CirAtr:         
            if i.Group==2:
                self.CX[n]=1/(vec2d(i.pos-self.Xdot.pos).get_length())
                self.CY[n]=0
            elif i.Group==3:
                self.CY[n]=1/(vec2d(i.pos-self.Ydot.pos).get_length())
                self.CX[n]=0
            elif i.Group<2:
                self.CY[n]=0
                self.CX[n]=0
            n+=1
        self.CoefNormalize()
        
    

    def GetDot(self,position,Range):  #position=поз курсора  range радиус от точки в котором проверять
        closest=0
        ClRange=10000
        CurDis=0
        for i in self.Agent:  #Dots?
            CurDis=len(position-i.pos)
            if (CurDis<Range) and (CurDis<ClRange):
                closest=i
                ClRange=CurDis
        return closest

    def ReviewCoord(self):
        for i in self.agents:
                x=10
                y=510     ####!!!Optimizirivat pod const
                for j in range(len(i.Atributes)):
                    x+=i.Atributes[j]*self.CX[j]#*self.screen.get_width()
                    y+=-i.Atributes[j]*self.CY[j]#*self.screen.get_height()
                i.pos.x=x
                i.pos.y=y
        

        

    def mouseUp(self,button,pos):
        Z=1
        Guu.GetInput(pos,button)
        self.Radius=25
        if vec2d(pos).x>self.nav_2.x and vec2d(pos).y<self.nav_2.y+self.nav_1.y:
            for i in self.CirAtr:
                    if vec2d(i.pos-pos).get_length()<15 and self.Keys[K_LCTRL]==False:
                        if button==1:
                            i.Group=2  #2=x,3=y
                            print(self.Chosen)
                        if button==3:
                            i.Group=3
                            print(self.Chosen)
                        if button==2:
                            i.Group=1
                            print(self.Chosen)
                        if button ==2 and self.Keys[K_RIGHT]:
                            i.InUse=1
                            Z=0
                    else:
                        if button==1:
                            self.Xdot.target=vec2d(pos)
                        elif button==3:
                            self.Ydot.target=vec2d(pos)                 
            if button==2 and self.Keys[K_RIGHT] and Z!=0:
                for i in self.CirAtr:
                    if i.InUse==1:
                        i.pos=vec2d(pos[0],pos[1])
                        i.InUse=0
                        break
        elif button==1 and  self.Keys[K_z]:
                self.ZoomPos=pos-vec2d(50,25)
##            if button==1:
##                self.CircleFixedChose(pos)
##            if button==3:
##                self.CircleFixedUnChose(pos)
        
               

    def draw(self):
       
        
        self.screen.fill((255,255,255))
        Guu.DrawButtons()
        pygame.draw.line(self.screen,(0,0,0),((self.main_2[0]-self.main_1[0])/2,self.main_1[1]),((self.main_2[0]-self.main_1[0])/2,self.main_2[1]+10),1)
        pygame.draw.line(self.screen,(0,0,0),(self.main_1[0],(self.main_2[1]-self.main_1[1])/2),(self.main_2[0]+10,(self.main_2[1]-self.main_1[1])/2),1)
        pygame.draw.rect(self.screen,(0,0,0),(self.main_1,self.main_2),2)
        pygame.draw.rect(self.screen,(0,0,0),(self.nav_2,self.nav_1),3)
        pygame.draw.circle(self.screen, (0,0,0), self.circleCenter, self.nav_1.x/2-10, 2)
        i=-1
        for a in self.CirAtr:
            i+=1
            if a.Group==2:
                Color=(30,200,30)
                TextCol=(30,200,30)
            elif a.Group==3:
                Color=(200,30,30)
                TextCol=(200,30,30)
            else:
                Color=(30,30,30)
            pygame.draw.circle(self.screen, Color, (a.pos.x,a.pos.y) , 10)
            self.screen.blit(self.text[i],(a.pos.x,a.pos.y))
            
        
        for a in self.agents:
            x=+300+math.trunc(a.pos.x)
            y=-300+math.trunc(a.pos.y)
            pygame.draw.circle(self.screen, GrCol[a.Group], (x,y), 3)


    
        self.Ydot.Go()
        self.Xdot.Go()
        self.SetCoeffs()
        self.ReviewCoord()
        x=math.trunc(self.Xdot.pos.x)
        y=math.trunc(self.Xdot.pos.y)            
        pygame.draw.circle(self.screen, (30,200,30), (x,y) , 6)
        x=math.trunc(self.Ydot.pos.x)
        y=math.trunc(self.Ydot.pos.y) 
        pygame.draw.circle(self.screen, (200,30,30), (x,y) , 6)
        Xstr='X='
        Ystr='Y='
        if self.Xdot.Pause==False:
            for i in range(len(self.agents[1].Atributes)):
                Xstr+='a'+str(i)+'*'+str(self.CX[i])+' + '
            self.Xtext=self.font.render(Xstr,True,(0,255,0))
            
        if self.Ydot.Pause==False:
            for i in range(len(self.agents[1].Atributes)):
                Ystr+='a'+str(i)+'*'+str(self.CY[i])+' + '
            self.Ytext=self.font.render(Ystr,True,(255,0,0))
        self.screen.blit(self.Xtext,(20,525))
        self.screen.blit(self.Ytext,(20,555))
        
        if self.ZoomPos!=0 and self.Keys[K_z]:
            self.Zoom(self.ZoomPos,3,(50,50))
            
        self.Instruments.Draw((840,212))
        mouse=pygame.mouse.get_pos()
        if mouse[0]<self.w-220:
            self.Instruments.Current.DrawOnCur(vec2d(pygame.mouse.get_pos()))     
        
    def Resize(self):
        if self.WasResized!=0:
            self.h=self.WasResized[1]
            self.w=self.WasResized[0]
            #print(self.w)
            self.screen=pygame.display.set_mode((self.w, self.h),(pygame.RESIZABLE))
    
    def InitSirAtr(self):
        self.CirAtr=[]
        self.CX=[]
        self.CY=[]
        for i in range(len(self.agents[0].Atributes)):
            self.CX.append(0)
            self.CY.append(0)
            self.CirAtr.append(Agent())
        print(self.CX,self.CY)
        self.initText()
        Dlin=len(self.CirAtr)
        dFi=6.28/Dlin
        Fi=0.0
        for a in range(len(self.CirAtr)):
            self.CirAtr[a].pos=self.circleCenter+vec2d((self.nav_1.x/2-10)*math.cos(Fi),(self.nav_1.x/2-10)*math.sin(Fi))
            print(self.CirAtr[a].pos)
            self.CirAtr[a].pos.x=math.trunc(self.CirAtr[a].pos.x)
            self.CirAtr[a].pos.y=math.trunc(self.CirAtr[a].pos.y)
            Fi+=dFi
        
                     


def RandomFill(target,AmountChar):
    chars=[]
    for a in target:
        for j in range(AmountChar):
            chars.append(random.randrange(0,500))
        a.Atributes=chars
        chars=[]

def LoadRand(target,AmountDots,AmountAtr):
    for i in range(AmountDots):
        target.agents.append(Agent())
    RandomFill(target.agents,AmountAtr)
    print('Ok! Filled')
    
    for i in range(len(target.agents[0].Atributes)):
            target.CX.append(0.0)
            target.CY.append(0.0)
            target.CirAtr.append(Agent())

      		
##s = Starter(900,600)                                   #ну это понятно
##Guu=Gui(s.screen) 
##Guu.Buttons.append(UniButton(vec2d(s.h+150,220),(80,40),s.InitSirAtr,'Reset'))
##Guu.Buttons.append(UniButton(vec2d(s.h+150,280),(80,40),s.Resize,'Resize'))
##LoadRand(s,150,4)                               #загружает случайными атрибутами массив агентов("массив","Колво точек")
##s.NormalizeAtributes(s.agents,200)              #нормализует поданный массив агентов к определенной длинне
##
##s.initText()                                    #инициализирует текст(тоже проверяет NSA хотя нет не проверяет кожфиценты дл запросов одинаковы) )
##s.mainLoop(90)                                  #

def FromArrayToAgents(Array):
    agents=[]
    for i in Array:
        a=Agent()
        a.Atributes=i
        agents.append(a)
    return agents
def VisualProjection(Array, Colors=[]):
    global GrCol
    s = Starter(900,600)                                   #ну это понятно
    s.agents=FromArrayToAgents(Array)
    print Colors
    if type(Colors)==list:
        for i in range(len(Colors)): 
            s.agents[i].Group=Colors[i]
    Guu=Gui(s.screen)
    global Guu
    global s
    s.InitSirAtr()
    Guu.Buttons.append(UniButton(vec2d(s.h+150,220),(80,40),s.InitSirAtr,'Reset'))
    Guu.Buttons.append(UniButton(vec2d(s.h+150,280),(80,40),s.Resize,'Resize'))
    s.NormalizeAtributes(s.agents,150)
    print('Norm:')
    print s.agents[4].Atributes
    s.initText()                                    
    s.mainLoop(90)






