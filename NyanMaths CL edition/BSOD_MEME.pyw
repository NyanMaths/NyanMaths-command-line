# -*-coding:Latin-1 -*

from os.path import exists

if not exists ("BSOD.png") or not exists ("BSOD_XD.png"):
    exit (1)
    
from threading import Thread

import winsound

from tkinter import *
from time import sleep

class Management (Thread):
    def __init__ (self):
        Thread.__init__ (self)

    def run (self):
        interface.image.config (image = interface.img0)

        winsound.Beep (500, 1500)
        sleep (3)

        interface.image.config (image = interface.img1)
        interface.config (cursor = '@Plz_wait.ani')
        sleep (3)

        interface.quit ()

class Interface (Tk):
    def __init__ (self):
        Tk.__init__ (self)
        
        self.wm_state (newstate = 'zoomed')
        self.overrideredirect (1)

        self.config (background = '#0000ac')
        self.config (cursor = 'none')
        
        self.img0 = PhotoImage (file = 'BSOD.png')
        self.img1 = PhotoImage (file = 'BSOD_XD.png')

        self.image = Label (self, borderwidth = 0)

        self.image.pack (expand = YES)

        self.manager = Management ()

interface = Interface ();
interface.manager.start ()

interface.mainloop ()
interface.destroy ()
