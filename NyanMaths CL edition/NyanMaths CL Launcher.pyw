# coding: utf-8


"""
NyanMaths CL version - Created by MemeTech INC

In the documentation, you can see all fonctionnalities of this application.

Creator : NY4N_M4THS
"""


from os.path import exists

from os import system
from threading import Thread

import webbrowser

from tkinter import *
from time import sleep

import re


looper = 1
themesList = {'Dark':'07', 'Classic':'f0', 'Matrix':'0a', 'BSOD':'9f'}
themesList_ = {'07':'Dark', 'f0':'Classic', '0a':'Matrix', '9f':'BSOD'}

window = Tk ()
window.geometry ("328x648+{0}+{1}".format (window.winfo_screenwidth () // 2 - 166, window.winfo_screenheight () // 2 - 340))


################################  Classes  ################################


class Lanceur (Thread):
    def __init__ (self, name):
        Thread.__init__ (self)
        self._name = name

    def run (self):
        if self._name[0] == 'h':
            webbrowser.open_new_tab (self._name)

        else:
            system (re.sub (r'/', r'\\', self._name))


class Interface (Frame):
    def __init__ (self, fenetre):
        Frame.__init__ (self, fenetre)
        self.pack (fill = BOTH)

        self.initVars ()

        self.initWidgets ()

        self.initSettings ()

        self.packing ()


    def initVars (self):
        self.loadTools = IntVar ()
        self.loadObjects = IntVar ()
        
        self.needHelp = IntVar ()
        self.displayConstants = IntVar ()

        self.theme = StringVar ()
        self.version = StringVar ()


        self.versionFrame = Frame (self)
        
        self.themeFrame = Frame (self)


        self.tWelcome = PhotoImage (file = 'Welcome.png')
        self.tCatAnim = [PhotoImage (file = 'Anim/NyanCat0.png'), PhotoImage (file = 'Anim/NyanCat1.png'), PhotoImage (file = 'Anim/NyanCat2.png'), PhotoImage (file = 'Anim/NyanCat3.png'), PhotoImage (file = 'Anim/NyanCat4.png')]
        self.tLoading = PhotoImage (file = 'Loading.png')


    def initWidgets (self):
        self.home = Label (self, text = "\nHelloooooooo !\nWelcome to NyanMaths command line edition !\nYou can check on our website for updates.\nLet's go !", foreground = 'blue')
        self.themeLabel = Label (self.themeFrame, text = "Choose a colour theme :", foreground = 'green')
        self.versionLabel = Label (self.versionFrame, text = "Choose your NyanMaths version :", foreground = 'green')

        self.sepLaunch = Label (self, text = "\n------------ Start NyanMaths ------------\n", font = 'Helcavita 13')
        self.sepOptions = Label (self, text = "\n------------ Options ------------\n", font = 'Helcavita 13')

        self.welcome = Label (self, image = self.tWelcome)
        self.catAnimation = Label (self, image = self.tLoading)

        self.checkLoadAll = Checkbutton (self, text = "Load objects when you start", foreground = 'green', variable = self.loadObjects)
        self.checkLoadTools = Checkbutton (self, text = "Load mini-apps (since 3.10)", foreground = 'green', variable = self.loadTools)
        self.checkHelp = Checkbutton (self, text = "If you need help", foreground = 'green', variable = self.needHelp)
        self.checkDisplayConstants = Checkbutton (self, text = "Display constants values", foreground = 'green', variable = self.displayConstants)

        self.run = Button (self, text = "Click to launch the application !", foreground = 'red', background = '#E3E3E3', font = 'Helvetica 13 bold', cursor = 'hand2', command = self.launch)
        self.helpMe = Button (self, text = "Do you need any help ?", foreground = 'blue', background = '#E3E3E3', font = 'Helvetica 13 bold', cursor = 'hand2', command = self.Help)
        self.updateButton = Button (self, text = "Check for updates", background = '#E3E3E3', font = 'Helvetica 13 bold', cursor = 'hand2', command = self.update)

        self.themeMenu = OptionMenu (self.themeFrame, self.theme, "Classic", "Dark", "Matrix", "BSOD")

        self.versionMenu = OptionMenu (self.versionFrame, self.version, '4.1.1', '4.0.1', '3.11.1', '2.6.2', '1.0.2')


    def initSettings (self):
        if exists ('Startup configuration.pastouche'):
            data = open ('Startup configuration.pastouche', 'r').read ().split (' ')

            self.loadObjects.set (int (data[0]))
            self.loadTools.set (int (data[5]))

            self.needHelp.set (int (data[1]))
            self.displayConstants.set (int (data[4]))

            self.theme.set (themesList_[data[2]])

            self.version.set (data[3])


        else:
            self.loadObjects.set (1)
            self.loadTools.set (1)

            self.needHelp.set (1)
            self.displayConstants.set (0)

            self.theme.set ('Classic')

            self.version.set ('4.1.1')


    def packing (self):
        self.welcome.pack ()
        self.home.pack ()
        
        self.sepOptions.pack ()

        self.checkLoadAll.pack ()
        self.checkLoadTools.pack ()
        self.checkHelp.pack ()
        self.checkDisplayConstants.pack ()

        self.themeFrame.pack ()
        self.themeLabel.pack (side = LEFT)
        self.themeMenu.pack (side = RIGHT)

        self.versionFrame.pack ()
        self.versionLabel.pack (side = LEFT)
        self.versionMenu.pack (side = RIGHT)
        
        self.sepLaunch.pack ()

        self.run.pack (fill = X)
        self.helpMe.pack (fill = X)
        self.updateButton.pack (fill = X)

        self.catAnimation.pack ()


    def launch (self):
        open ('Startup configuration.pastouche', 'w').write ('{0} {1} {2} {3} {4} {5}'.format (self.loadObjects.get (), self.needHelp.get (), themesList[self.theme.get ()], self.version.get (), self.displayConstants.get (), self.loadTools.get ()))

        if self.version.get ()[0] == '4':
            self.launcher = Lanceur ('Versions/NyanMaths4xx.py')

        else:
            self.launcher = Lanceur ('Versions/NyanMaths{0}.py'.format (self.version.get ()))

        self.launcher.start ()


    def Help (self):
        self.help_launcher = Lanceur ('help.html')
        self.help_launcher.start ()


    def update (self):
        webbrowser.open_new_tab ('https://memetech-inc.weebly.com/nyanmaths-cl')


################################  Initialization  ################################


window.title ("NyanMaths command line launcher")

if exists ('Icon.ico'):
    window.iconbitmap ('Icon.ico')

window.resizable (width = 'False', height = 'False')

interface = Interface (window)


################################  Animation thread  ################################


class Animations (Thread):
    def __init__ (self):
        Thread.__init__ (self)

    def run (self):
        titleIndex = True

        while True:
            if titleIndex:
                window.title ("NyanMaths command line launcher")
                titleIndex = False

            else:
                window.title ("By MemeTech INC")
                titleIndex = True

            i_ = 0
            while i_ < 5:
                timeCount = 0

                while timeCount < 30:
                    sleep (0.02)

                    if not looper:
                        return 0

                    timeCount += 1

                interface.catAnimation.config (image = interface.tCatAnim[i_])
                i_ += 1


################################  Launching  ################################


anim = Animations ()
anim.start ()

interface.mainloop ()  # Starts the application

looper = 0
anim.join ()


################################  Save settings before closing  ################################


open ('Startup configuration.pastouche', 'w').write ('{0} {1} {2} {3} {4} {5}'.format (interface.loadObjects.get (), interface.needHelp.get (), themesList[interface.theme.get ()], interface.version.get (), interface.displayConstants.get (), interface.loadTools.get ()))

