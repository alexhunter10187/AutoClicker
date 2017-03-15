from win32 import win32api
import win32con
from tkinter import *
from itertools import count
from builtins import int
from faulthandler import disable
import time
from _overlapped import NULL
import winsound
from time import sleep

'''Great Sources of information: 

http://timgolden.me.uk/pywin32-docs/win32api.html 
http://www.programcreek.com/python/index/475/win32con
http://www.asciitable.com/



'''
class Application(Frame):
    
    
    '''def lockPos(self):
       

        h_x, h_y = win32api.GetCursorPos()
        self.x.set(h_x)
        self.y.set(h_y)
        root.update_idletasks()
            
    '''
    
    
    def checkToggle(self):
        if(self.togglePosVal.get() == 0):
            self.xposEntry.configure(state ='disabled')
            self.yposEntry.configure(state ='disabled')
        elif(self.togglePosVal.get() == 1):
            self.xposEntry.configure(state ='normal')
            self.yposEntry.configure(state ='normal')
        
    
    def gotoXY(self):
        #Sets mouse on a position on screen.
        win32api.SetCursorPos((int(self.xposEntry.get()),int(self.yposEntry.get())))

    def closePrev(self):
        #Removes ALL things within window.
        
        self.xposEntry.pack_forget()
        self.xposEntryText.pack_forget()
        self.yposEntry.pack_forget()
        self.yposEntryText.pack_forget()
        self.numberOfClicks.pack_forget()
        self.clickButton.pack_forget()
        self.backButton.pack_forget()
        self.displayClicks.pack_forget()
        self.numberOfClicksText.pack_forget()
        self.togglePos.pack_forget()
        self.screenWidgets()
        
    def resetAutoClickEntryColor(self):
        self.xposEntry.config(background = '#FFFFFF')
        self.yposEntry.config(background = '#FFFFFF')

    
    def autoClick(self):
        self.resetAutoClickEntryColor()
        i=0
        count = StringVar()
        
        #Untoggled Position
        if(self.togglePosVal.get() == 0):
            self.displayClicks.pack_forget()
            print("Clicking " + self.numberOfClicks.get() + " times at NO DEFAULT POSITION")
           
            
            self.displayClicks = Label(textvariable = count)
            self.displayClicks.pack(side=LEFT)
            for i in range(0,int(self.numberOfClicks.get())):
                time.sleep(.005)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(self.xposEntry.get()),int(self.yposEntry.get()),0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(self.xposEntry.get()),int(self.yposEntry.get()),0,0)
                
                i = i + 1
                print(i)
                count.set("Clicks Completed: " + str(i))
                root.update_idletasks()
            
            
            
        #Toggled Position
        else:
            
            try:
                
                self.displayClicks.pack_forget()
        
                print("Clicking " + self.numberOfClicks.get() + " times at pos:("+ self.xposEntry.get() +","+ self.yposEntry.get() +")")
                self.displayClicks = Label(textvariable = count)
                self.displayClicks.pack(side=LEFT)
                for i in range(0,int(self.numberOfClicks.get())):
                    time.sleep(.005)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(self.xposEntry.get()),int(self.yposEntry.get()),0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(self.xposEntry.get()),int(self.yposEntry.get()),0,0)
                
                    i = i + 1
                    print(i)
                    count.set("Clicks Completed: " + str(i))
                    self.gotoXY()
                    root.update_idletasks()
                    
            except ValueError:
                print("A non-valid integer was submitted")
                self.xposEntry.config(background='#FFCCCC')
                self.yposEntry.config(background='#FFCCCC')
                winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)
                root.update_idletasks()
                
        
        
            
    def autoScreen(self):
        

        self.secondB.pack_forget()
        self.Start.pack_forget()
        print ("Auto Clicker Screen Launched")
        global nC
        nC = 0
        
        self.numberOfClicksToggle = Checkbutton(text = "")
        self.numberOfClicksToggle.pack(side = LEFT)
        
        
        self.numberOfClicksText = Label(text="Number Of Clicks ")
        self.numberOfClicksText.pack(side = LEFT)
        self.numberOfClicks = Entry(textvariable = nC)
        self.numberOfClicks['text'] = ""
        self.numberOfClicks.pack(side = LEFT)
        
        
        
        
        self.displayClicks = Label(textvariable = count)
        self.displayClicks.pack(side=LEFT)
        clickDuration = int;
        
        self.clickDuration = Entry(textvariable = clickDuration)
        self.clickDuration.pack()
        self.clickButton = Button(self)
        self.clickButton['text'] = "Click"
        self.clickButton['command'] = self.autoClick
        self.clickButton.pack(side = RIGHT)
        
        self.backButton = Button(self)
        self.backButton['text'] = "Previous"
        self.backButton['command'] = self.closePrev
        self.backButton.pack(side = RIGHT)
        
        x=int
        y=int
        
        
        self.xposEntryText = Label(self,text="X:")
        self.xposEntryText.pack(side=LEFT)
        
        self.xposEntry = Entry(self,textvariable=x,state = 'disabled')
        self.xposEntry['text'] = ""
        self.xposEntry.pack(side=LEFT)
        
        self.yposEntryText = Label(self,text="Y:")
        self.yposEntryText.pack(side=LEFT)
        
        self.yposEntry = Entry(self,textvariable=y, state = 'disabled')
        self.yposEntry['text'] = ""
        self.yposEntry.pack(side=LEFT)
        
        
        self.togglePosVal = IntVar()  
        self.togglePos = Checkbutton(self,text="Toggle XY Positions", variable = self.togglePosVal)
        self.togglePos['command'] = self.checkToggle
        self.togglePos.pack(side=LEFT)
        
        '''self.lockPos()'''
        
    def screenWidgets(self):
        
        self.Start = Button(self,height = 10, width = 30,compound = LEFT) 
        self.Start["text"] = "Auto Clicker"
        self.Start["command"] = self.autoScreen
        self.Start.pack(side=RIGHT)
        
        self.secondB = Button(self,height = 10, width = 30)
        self.secondB["text"] = "Another"
        self.secondB["command"] = self.autoScreen
        self.secondB.pack(side=LEFT)
        

    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.screenWidgets()
        
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()