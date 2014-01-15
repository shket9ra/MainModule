#Canvas он же главный модуль
#Содржит основное окно и методы управления, так же он осуществляет построение и обход диаграммы
#
#
#


# -*- coding: utf-8 -*-
import sys
import time
from Tkinter import * 
import ttk
from vec2d import *
import math
import Meth
import copy
from PIL import ImageTk,Image
curdir="C:\Users\admin\Desctop\Working"
def DoNothing(a):
    pass

def partcount(agent):
        n=0
        for i in agent.name:
            if i=="\n" :
                n+=1
        return n

class Keeper():
        def __init__(self,Parent,Analiz,Flter,Visual):
            self.Analis=Analiz
            self.Filter=Flter
            self.Visual=Visual
            self.Parent=Parent
            self.Texts=[]
            self.LeftWin=0
            self.MadeMenu()
            self.Type=0
            self.MethList=[]
            self.CurBlock=0
            self.ChosenRect=0
            
            
        def MadeMenu(self):
            self.Chosens=[]
            self.Main=Canvas(self.Parent, width=200, height=150, bg="grey", relief="raised", borderwidth=5)
            self.LeftWin=Canvas(self.Main, width=200, height=60, bg="grey", relief="raised", borderwidth=0)
            self.LeftWin.bind("<Button-1>",self.Choose2)
            self.LeftDownWin=Canvas(self.Main, width=200, height=450, bg="grey", relief="raised", borderwidth=0)
            self.LeftDownWin.bind("<Button-1>",self.Choose1)
            #self.Blocks.create_text(10, , text=u"ЮРИДИЧЕСКОЕ ЛИЦО", anchor=NW)
            for i in range(3):
                self.Chosens.append(self.LeftWin.create_polygon(2+66*i,2, 2+66*i,60, 66+66*i,60, 66+66*i,2, outline="black",fill="grey"))
            i=0
            self.Chosens.append(self.LeftWin.create_polygon(3+66*i,3, 3+66*i,59, 65+66*i,59, 65+66*i,3, outline="red",fill="grey"))
            self.LeftWin.create_polygon(13,30, 33,10, 53,30, 33,50,   outline="black",fill="grey")
            self.LeftWin.create_oval(80,10,120,50,outline="black",fill="grey")
            self.LeftWin.create_rectangle(146,10,186,50,outline="black",fill="grey")
            for i in range(22):
                self.LeftDownWin.create_rectangle(5,5+20*i,200,27+20*i,outline="black",fill="grey")

            self.Main.grid(column=0,row=1)
            self.LeftWin.grid(column=0,row=1)
            self.LeftDownWin.grid(column=0,row=2)
                

        
        def Choose1(self, event):
                self.LeftDownWin.delete(self.ChosenRect)
                n=event.y+11
                n=n/20
                print n
                if n>0:
                    if self.Type==1:
                        if n<=len(self.Analis):
                            self.ChosenRect=self.LeftDownWin.create_rectangle(6,6+20*(n-1),199,26+20*(n-1),outline="red",fill="grey")
                            self.FillFrom(self.Type)
                            n=self.MethList[n-1][1]
                            self.CurBlock=self.Analis[n]
                    if self.Type==2:
                        if n<=len(self.Visual):
                            self.ChosenRect=self.LeftDownWin.create_rectangle(6,6+20*(n-1),199,26+20*(n-1),outline="red",fill="grey")
                            self.FillFrom(self.Type)
                            n=self.MethList[n-1][1]
                            self.CurBlock=self.Visual[n]
                    if self.Type==3:
                        if n<=len(self.Filter):
                            
                            self.ChosenRect=self.LeftDownWin.create_rectangle(6,6+20*(n-1),199,26+20*(n-1),outline="red",fill="grey")
                            self.FillFrom(self.Type)
                            n=self.MethList[n-1][1]
                            self.CurBlock=self.Filter[n]
                print(self.CurBlock)
##            
        def Choose2(self,event):
            if event.x<66 and event.y<60:
                    self.FillFrom(1)
            elif event.x<132 and event.y<60:
                    Cont.FillFrom(2)
            elif event.x<200 and event.y<60:
                    Cont.FillFrom(3)

                    
        def FillFrom(self,tip):
            for i in self.Texts:
                self.LeftDownWin.delete(i)
            c=0
            if tip==1:
                self.Type=1
                self.MethList=list(enumerate(self.Analis))
                for i in self.Analis:  
                    c+=1
                    
                    self.Texts.append(self.LeftDownWin.create_text(10, -16+c*20,fill="blue", text=unicode(i),anchor=NW, font=("Helvectica", "16")))
            if tip==2:
                self.MethList=list(enumerate(self.Visual))
                self.Type=2
                for i in self.Visual:
                    c+=1
                    a=self.LeftDownWin.create_text(10, -16+c*20,fill="blue", text=unicode(i),anchor=NW, font=("Helvectica", "16"))
                    self.Texts.append(a)
            if tip==3:
                self.Type=3
                self.MethList=list(enumerate(self.Filter))
                for i in self.Filter:
                    c+=1
                    a=self.LeftDownWin.create_text(10, -16+c*20,fill="blue", text=unicode(i),anchor=NW, font=("Helvectica", "16"))
                    self.Texts.append(a)
            for i in self.Chosens:
                self.LeftWin.delete(i)
            for i in range(3):
                self.Chosens.append(self.LeftWin.create_polygon(2+66*i,2, 2+66*i,60, 66+66*i,60, 66+66*i,2, outline="black",fill="grey"))
            i=tip-1
            self.Chosens.append(self.LeftWin.create_polygon(3+66*i,3, 3+66*i,59, 65+66*i,59, 65+66*i,3, outline="red",fill="grey"))
            self.LeftWin.create_polygon(13,30, 33,10, 53,30, 33,50,   outline="black",fill="grey")
            self.LeftWin.create_oval(80,10,120,50,outline="black",fill="grey")
            self.LeftWin.create_rectangle(146,10,186,50,outline="black",fill="grey")
            



def colorconvert(r, g, b): #Конвертация ЦВЕТОВ
        s='#'+str(int(r/256.0*1000))+str(int(g/256.0*1000))+str(int(b/256.0*1000))
        
        return s
class Agent: #КЛАСС ЭЛЕМЕНТОВ РАССЛЕДОВАНИЯ
    def __init__(self):
        self.pos= vec2d(0,0)
        self.target= vec2d(0,0)
        self.drawid=0
        self.type=0
        self.status=1
        self.time=0
        self.textid=0
        self.name=""
        self.ConOut=0
        self.ConDraw=0
        self.Outs=[]
        self.OutAm=1
        self.Start=0
        self.Params={}
        self.Container=0

        
class Out:#КЛАСС СВОЙСТВ ЭЛЕМЕНТОВ
    def __init__(self,In):
        self.start=In
        self.end=0
        self.drawid=0
        self.Line=0
        self.Used=0

class NewAgent():  #ОН НАМНОГО УМНЕЕ
    def __init__(self, Container):
        self.pos= vec2d(0,0)
        self.drawid=0
        self.Start=0
        self.InNames=Container.Input
        self.OutNames=Container.Output
        self.Params={}
        self.InPin={}
        self.OutPin={}
        for i in Container.ParaNames:
            self.Params[i]=0
        self.Container=Container
        for i in Container.Input:
            self.InPin[i]=Pin(self)
        for i in Container.Output:
            self.OutPin[i]=Pin(self)
        self.Method=Container.Method
    def Send(self,Name,Data):
        a=self.OutPin[Name]
        a.Data=Data
        if a.Out!=None:
            a.Out.Data=Data
        print a.Data
    def Get(self,Name):
        a=self.InPin[Name]
        print a.Data
        if type(a.Data)!=None:
            return a.Data
        else:
            print("Нету данных на входе")

    def Draw():
        pass
    def Method():
        pass
class Pin:
    def __init__(self,agent):
        self.In=0
        self.Out=0
        self.Data=None
        self.DrawId=0
        self.Line=0
        self.pos=(0,0)
        self.agent=agent
        

        
class Starter(Tk):#ОСНОВНОЙ КЛАСС
    def __init__(self):#КОНСТРУКТОР
        #menu
        Tk.__init__(self)
        self.__menu__()
        self.__tools__()
        self.__views__()
        #self.__time__()
        self.__agents__()
        self.__packs__()
        self.draw()
        #bindings c
        self.views[0].bind("<Button-1>",self.NewButton1)
        self.views[0].bind("<Button-3>",self.cButton2)
        self.bind("<Key>",self.typing )
        #bindings tools
        self.ctools.bind("<Button-3>",self.ctButton2)
        #self.timescale.bind("<Leave>", self.update())
    
    def __menu__(self):#МЕНЮ
        main_menu = Menu(self)
        self.config(menu=main_menu)
        file_menu = Menu(main_menu)
        file_menu.add_command(label="Выход", command=self.destroy)    
    def __tools__(self):#ИНСТРУМЕНТЫ
        self.ctools=Canvas(self, width=200, height=480, bg="grey", relief="raised", borderwidth=5)
                
    def __views__(self):#СОЗДАНИЕ ОБРАЗОВ
        self.views=[]
        #self.notebook=ttk.Notebook(self)
        self.views.append(Canvas(self, width=640, height=500, bg="white", relief=RIDGE, borderwidth=5))
        #for c in self.views:
        #self.notebook.add(self.views[0])
 
    def __info__(self):# ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ И МЕНЮ УПРАВЛЕНИЯ ЛОКАЛЬНОЙ БАЗОЙ
        pass
    def __time__(self):# ШКАЛА ДЛЯ АНИМАЦИИ ЭТАПОВ РАЗВИТИЯ СХЕМЫ/РАССЛЕДОВАНИЯ
        self.time=IntVar(self)
        self.timefrom=0
        self.timeto=10
        self.timescale=Scale(self.views[0], orient=HORIZONTAL, label=u"Время", relief="raised", borderwidth=5, from_=self.timefrom, to=self.timeto, variable=self.time)
        self.timescale.place(x=7, y=414)
    def __agents__(self): #ИНИЦИАЦИЯ ЭЛЕМЕНТОВ РАССЛЕДОВАНИЯ 
        self.agents= []
        self.links=[]
        self.selected=0# self.agents[0]
        self.selOut=0#Out(self.agents[0])
        self.Starts=[]
    def __packs__(self):  #РАЗМЕЩЕНИЕ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
        #self.notebook.grid(column=2,row=2)
        self.views[0].grid(column=2,row=2)
        

    def open(self):
        pass
    def ctButton2(self, event):#МЕТОДЫ УПРАВЛЕНИЯ ИНТЕРФЕЙСОМ
           for a in self.agents:
            if a==self.selected:
                a.type=self.typeselected(event.y)
                
            self.update()
        
    def typeselected(self, y):#ОБРАБОТКА ТИПА ЭЛЕМЕНТА РАССЛЕДОВАНИЯ
        if y<50:
            return 0
        elif y<90:
            return 1
        elif y<130:
            return 2
        else:
            return 3

    def cButton1(self,event):#МЕТОДЫ УПРАВЛЕНИЯ ИНТЕРФЕЙСОМ
        self.bind("<Key>",self.typing )
        Rm.But.focus()
        if len(self.agents)>0 and self.agents[0].Outs==[] :
            self.agents.remove(self.agents[0])
        f=True
        foo=[[-5],[-15,5],[-25,-5,15],[-35,-15,5,25],[-45,-25,-5,15,35]]
        for a in self.agents:
            if a.pos.get_distance(vec2d(event.x,event.y)) < 45:
                self.selected=a
                if len(self.selected.OutPin)>0:
                    self.selOut=self.selected.OutPin[0]
                else:
                    self.selOut=self.selected.InPin[0]
                l=len(a.InPin)
                for i in self.InPin:
                    if i.get_distance(vec2d(event.x,event.y)) < 15:
                        self.selOut=i
                for i in self.OutPin:
                    if i.get_distance(vec2d(event.x,event.y)) < 15:
                        self.selOut=i
                print(self.selOut)
                Rm.Remade(self.selected)
                f=False
        if f and Cont.CurBlock!=0:
            a= Agent()
            a.type=Cont.Type
            a.pos= vec2d((event.x,event.y))
            a.target= vec2d((event.x,event.y))
            a.time=self.time.get()
            a.Outs.append(Out(a))
            a.Container=Cont.CurBlock
            for i in range(len(a.Container.ParaNames)):
                a.Params[a.Container.ParaNames[i]]='0'
            self.agents.append(a)
            self.selected= a
            self.selOut=self.selected.Outs[-1]
        self.update()
        
    def NewButton1(self,event):#МЕТОДЫ УПРАВЛЕНИЯ ИНТЕРФЕЙСОМ
        self.bind("<Key>",self.typing )
        Rm.But.focus()
        foo=[[-5],[-15,5],[-25,-5,15],[-35,-15,5,25],[-45,-25,-5,15,35]]
##        if len(self.agents)>0 and self.agents[0].Outs==[] :
##            self.agents.remove(self.agents[0])
        f=True
        for a in self.agents:
            if a.pos.get_distance(vec2d(event.x,event.y)) < 45:
                self.selected=a
                print a.InPin
                if len(self.selected.OutPin)>0:
                    self.selOut=self.selected.OutPin[self.selected.OutNames[0]]
                else:
                    self.selOut=self.selected.InPin[self.selected.InNames[0]]
                l=len(a.InPin)
                
                for i in a.InNames:
                    q=a.InPin[i]
                    if q.pos.get_distance(vec2d(event.x,event.y)) < 15:
                        self.selOut=q
                for i in a.OutNames:
                    q=a.OutPin[i]
                    if q.pos.get_distance(vec2d(event.x,event.y)) < 15:
                        self.selOut=q
                Rm.Remade(self.selected)
                f=False
                
        if f and Cont.CurBlock!=0:
            a= NewAgent(Cont.CurBlock)
            a.type=Cont.Type
            a.pos= vec2d((event.x,event.y))
            #a.time=self.time.get()
            a.Container=Cont.CurBlock
            self.agents.append(a)
            self.selected=a
            if len(a.OutNames)>0:
                self.selOut=a.OutPin[a.OutNames[0]]
            #self.selOut=self.selected.OutPin[self.selected.OutNames[0]]
        self.update()
            
            
    def cButton2(self,event):#МЕТОДЫ УПРАВЛЕНИЯ ИНТЕРФЕЙСОМ
        match=self.selected        
        #match=self.selected   
        for a in self.agents:
            if a.pos.get_distance(vec2d((event.x,event.y))) < 40:
                match=a
        if (match<>self.selected):
            for i in match.InNames:
                a=match.InPin[i]
                if a.pos.get_distance(vec2d(event.x,event.y))<10:
                    if self.selOut.Out!=0:
                        self.selOut.Out.In=0
                    if a.In!=0:
                        a.In.Out=0
                    self.selOut.Out=a
                    a.In=self.selOut

        else:
            self.selected.pos= vec2d((event.x,event.y))
        self.update()
    def typing(self, event):
        
####        if event.char in ('1','2','3','4'):
####            if self.selected.OutAm<int(event.char):
####                for i in range(int(event.char)-self.selected.OutAm):
####                    self.selected.Outs.append(Out(self.selected))
####                self.selected.OutAm=int(event.char)
####                self.selOut=self.selected.Outs[-1]
####                
##                
##            if self.selected.OutAm>int(event.char):
##                a=self.selected.OutAm-int(event.char)
##                for i in range(len(self.selected.Outs)):
##                    
##                    if i>-1 and i<len(self.selected.Outs) and self.selected.Outs[i].end==0:
##                        self.selected.Outs.remove(self.selected.Outs[i])
##                        self.selected.OutAm=self.selected.OutAm-1
##                        i-=1
##                        a-=1
##                    if a==0: break
##                self.selOut=self.selected.Outs[-1]
                


        if event.char in ('d','D') and len(self.agents)>0:
            ss=self.selected
            for i in self.selected.InNames:
                self.views[0].delete(ss.InPin[i].drawid)
                self.views[0].delete(ss.InPin[i].Line)
                if ss.InPin[i].In!=0:
                    ss.InPin[i].In.Out=0
            for i in self.selected.OutNames:
                self.views[0].delete(ss.OutPin[i].drawid)
                self.views[0].delete(ss.OutPin[i].Line)
                if ss.OutPin[i].Out!=0:
                    ss.OutPin[i].Out.In=0
                
            self.views[0].delete(ss.drawid)

##            for a in self.agents:
##                if a.ConOut==ss:
##                    a.ConOut=0
##                for i in a.Outs:
##                    if i.end==ss:
##                        self.views[0].delete(i.Line)
##                        i.end=0
            self.agents.remove(self.selected)

        if event.char in ('s','S'):
            ss=self.selected
            f=0
            for i in self.Starts:
                if ss==i:
                    f=1
            if f==1:
                self.Starts.remove(ss)
            else:
                self.Starts.append(ss)
                

        if event.char in ('z','Z'):
            global Rm
            Rm.But.focus()

        if event.char in ('b','B'):
            self.RunIt()
            
                

                
                       
        self.update() 
    def update(self):#ФУНКЦИИ ДЛЯ ВИЗУАЛИЗАЦИИ СХЕМЫ
        self.delete()
        self.draw()
    def delete(self):#УДАЛЕНИЕ СХЕМЫ
        self.views[0].delete('all')
    def intime(self, a):#ФУНКЦИЯ ПРОВЕРКИ НА СУЩЕСТВОВАНИЯ ОБЬЕКТА В ЗАДАННОМ ВРЕМЕНИ
        n=False
        if a.time<=self.time.get():
            n=True
        return n
    def DrawAgentPins(self,Agent):
        SOA=30
        foo=[[-5],[-15,5],[-25,-5,15],[-35,-15,5,25],[-45,-25,-5,15,35]]
        i=0
        colo=colorconvert(200, 120, 100)
        color=col=colorconvert(155, 247, 249)
        for k in Agent.InNames:
            a=Agent.InPin[k]
            l=len(Agent.InPin)-1
            a.pos=vec2d(Agent.pos.x+foo[l][i]+5,Agent.pos.y-SOA)
            
            a.drawid=self.views[0].create_oval(a.pos.x-5, a.pos.y-5, a.pos.x+5, a.pos.y+5,outline="black",fill=col)
            if self.selOut==a:
                a.drawid=self.views[0].create_oval(a.pos.x-5, a.pos.y-5, a.pos.x+5, a.pos.y+5,outline="black",fill=colo)
            i+=1
        i=0
        for k in Agent.OutNames:
            a=Agent.OutPin[k]
            l=len(Agent.OutPin)-1
            a.pos=vec2d(Agent.pos.x+foo[l][i]+5,Agent.pos.y+SOA)
            a.drawid=self.views[0].create_oval(a.pos.x-5, a.pos.y-5, a.pos.x+5, a.pos.y+5,outline="black",fill=col)
            if self.selOut==a:
                a.drawid=self.views[0].create_oval(a.pos.x-5, a.pos.y-5, a.pos.x+5, a.pos.y+5,outline="black",fill=colo)
            i+=1
            
    def draw(self):#ФУНКЦИИ ДЛЯ ВИЗУАЛИЗАЦИИ СХЕМЫ
        foo=[[-5],[-15,5],[-25,-5,15],[-35,-15,5,25],[-45,-25,-5,15,35]]
        SOA=30
        for a in self.agents:
            color=colorconvert(155, 100, 140)
##            for i in range(len(a.InPin)):
##                if a.InPin[i].end!=0:
##                    a.Outs[i].Line=self.views[0].create_line(a.pos.x+foo[l][i]+5,a.pos.y+SOA,  a.Outs[i].end.pos.x, a.Outs[i].end.pos.y, width=2)
        
        for a in self.agents:
           
            color=col=colorconvert(155, 247, 249)
            if a==self.selected:
                    color=colorconvert(100, 100, 249)
            if a.type==2:
                a.drawid=self.views[0].create_oval(a.pos.x-SOA, a.pos.y-SOA, a.pos.x+SOA, a.pos.y+SOA,outline="black",fill=color)
            elif a.type==3:
                a.drawid=self.views[0].create_rectangle(a.pos.x-SOA,a.pos.y-SOA,a.pos.x+SOA,a.pos.y+SOA,outline="black",fill=color)
            elif a.type==1:
                a.drawid=self.views[0].create_polygon(a.pos.x-SOA, a.pos.y
                                                      ,a.pos.x, a.pos.y-SOA
                                                      ,a.pos.x+SOA, a.pos.y
                                                      ,a.pos.x,a.pos.y+SOA
                                                      ,outline="black",fill=color)
            if a.Start!=0:
                color=colorconvert(155, 28,30)
                a.Start=self.views[0].create_oval(a.pos.x-15, a.pos.y-15, a.pos.x+15, a.pos.y+15,outline="black",fill=color)
            self.DrawAgentPins(a)
        for a in self.agents:    
            for k in a.OutNames:
                q=a.OutPin[k]
                if q.Out!=0:
                    q.Line=self.views[0].create_line(q.pos.x,q.pos.y,  q.Out.pos.x,q.Out.pos.y, width=2)
        #self.notebook.grid(column=2,row=1)
        for a in self.Starts:
            color=col=colorconvert(200, 100, 100)
            self.views[0].create_oval(a.pos.x-SOA/2, a.pos.y-SOA/2, a.pos.x+SOA/2, a.pos.y+SOA/2,outline="black",fill=color)

        self.views[0].grid(column=2,row=1)
    def RunIt(self):
        self.CurUse=0
        Cur=self.agents[0]
        Return=self.Starts
        if len(self.Starts)>0:
            Cur=self.Starts.pop()
        Order=[]
        CurData=0
        view=0
        a=0
        color=colorconvert(155, 28,30)
        Stop=False
        Num=0
        while(not Stop):
            Num+=1
            print('Current:',Cur.Container.Name)
            Cur.Method(Cur)
            #self.CurUse=self.views[0].create_oval(Cur.pos.x-15, Cur.pos.y-15, Cur.pos.x+15, Cur.pos.y+15,outline="black",fill=color)
            a=0
            for n in Cur.OutNames:
                i=Cur.OutPin[n]
                if i.Out!=0:
                    a+=1
            print a
            if a==0:
                if len(Return)!=0:
                    Order.append(Cur)
                    Ret=Return.pop()
                    Cur=Ret
                else:
                    Stop=True
                    Order.append(Cur)
                    #CurData=Cur.Container.Method(CurData,Params=Cur.Params)
            if a==1:
                Order.append(Cur)
                for n in Cur.OutNames:
                    i=Cur.OutPin[n]
                    
                    if i.Out!=0:
                        bol=True
                        for j in i.Out.agent.InNames:
                            s=i.Out.agent.InPin[j]
                            if type(s.Data)==int:
                                if s.Data==0 and s.In!=0:
                                    bol=False
                        if bol==True:
                            Cur=i.Out.agent
                        else:
                            if len(Return)!=0:
                                Ret=Return.pop()
                                Cur=Ret
                            else:
                                Stop=True
    
            if a>1:
                Order.append(Cur)
                for n in Cur.OutNames:
                    i=Cur.OutPin[n]
                    if i.Out!=0:
                        bol=True
                        for j in i.Out.agent.InNames:
                            s=i.Out.agent.InPin[j]
                            if type(s.Data)==int:
                                if s.Data==0 and s.In!=0:
                                    bol=False
                        if bol==True:
                            Return.append(i.Out.agent)
                if len(Return)!=0:
                    Ret=Return.pop()
                    Cur=Ret
                else:
                    Stop=True
                    
            #time.sleep(0)
            print('==========')
            print('Maded')
            for i in Order:
                print ('-',i.Container.Name)
            print('Returns')
            for i in Return:
                print ('-',i.Container.Name)
            print('==========')
            
            
        

class RightMenu():
    def __init__(self,Parent):
        self.Texts=[]
        self.Results=[]
        self.Parent=Parent
        self.Menu=Canvas(self.Parent, width=300, height=500,relief=GROOVE , bd=0)
        self.ImageBorder=Canvas(self.Menu, width=210, height=160,relief=GROOVE , bd=2, bg="white")
        self.Img=ImageTk.PhotoImage(file ="C:\Users\Admin\Desktop\Working\Ifes.jpg")
        self.ImageBorder.create_image((107,75), image=self.Img)
        self.ImageBorder.grid(row=0,column=0 ,columnspan=2,)
        self.Menu.grid(sticky=W+E+N+S ,row=1,column=3,columnspan=2 )
        self.DTexts=Text( self.Menu ,font=('times',10),width=35,height=10,wrap=WORD, bd=2)
        self.But = Button (self.Menu,width=29,text ="Apply")
        self.But.bind("<Button-1>",self.RemadeStats)

    def RemadeStats(self,Self):
        for i in range(len(self.Agent.Container.ParaNames)):
            self.Agent.Params[self.Agent.Container.ParaNames[i]]=str(self.Results[i].get(1.0, END)).replace('\n', '')
    def GetIn(self,In):
        print (self,In)
        s.bind("<Key>",DoNothing)
    def Remade(self,Agent):
        
        self.Agent=Agent
        for i in self.Texts:
            i.destroy()
        for i in self.Results:
            i.destroy()
        self.Texts,self.Results=[],[]
        Names=Agent.Container.ParaNames
        for i in range(len(Names)):
            
            w = Label(self.Menu, text=Names[i],anchor=W,bg=None)
            w.grid(column=0,row=1+2*i,sticky=W+E,padx=5, pady=0)
            self.Texts.append(w)
            tx = Text( self.Menu ,font=('times',10),width=10,height=1,wrap=WORD)
            tx.insert(1.0,Agent.Params[Names[i]])
            tx.grid(column=1,row=1+2*i)
            tx.bind("<Button-1>", self.GetIn)
            self.Results.append(tx)
        
        self.DTexts.delete(1.0,END)
        self.DTexts.insert(1.0,'Method Name: \n')
        self.DTexts.insert(2.0,Agent.Container.Name+'\n')
        self.DTexts.insert(3.0,'Description: \n')
        self.DTexts.insert(4.0,Agent.Container.Descr+'\n') 
        self.DTexts.insert(5.0,'Remarks: '+'\n')
        self.DTexts.tag_add('Name','1.0','1.11')
        self.DTexts.tag_config('Name',font=('Dejavu',10,'bold'))
        self.DTexts.tag_add('Desc','3.0','3.11')
        self.DTexts.tag_config('Desc',font=('Dejavu',10,'bold'))
        self.DTexts.tag_add('Desc','5.0','5.11')
        self.DTexts.tag_config('Desc',font=('Dejavu',10,'bold'))
        self.DTexts.grid(column=0,row=1+len(self.Texts)*2,columnspan=2,rowspan=2)        
        self.But.grid(column=0,row=2+len(self.Texts)*2+1,columnspan=2, rowspan=2)
          
        
s = Starter()
Rm=RightMenu(s)
Cont=Keeper(s,Meth.AnalizConteiner, Meth.FilterContainer,Meth.VisualContainer)
Cont.FillFrom(1)

s.mainloop()

