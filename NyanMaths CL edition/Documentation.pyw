# -*-coding:utf-8 -*


"""
This module displays a little documentation of an object :
Attributes, operators, constructor...

Created by NY4N_M4THS
"""

from os.path import exists
from sys import argv

from tkinter import *


if len (argv) < 2:
    exit (1)

##########################################################

window = Tk ()

window.resizable (width = "False", height = "False")
window.title ("NyanMaths - Documentation of type {0}".format (argv[1]))

if exists ("Icon.ico"):
    window.iconbitmap ("Icon.ico")


##########################################################


class Interface (Frame):
    def __init__ (self, window):
        Frame.__init__ (self, window)
        self.pack (fill = BOTH)


        self.picture = PhotoImage ()
        self.canvas = Canvas (self, width = 512, height = 512, confine = False)

        self.description = Text (self, wrap = 'word', font = 'Helcavita 11', bd = 0, bg = '#f0f0f0')

        self.scrollBar = Scrollbar (self, orient = VERTICAL)
        self.description.config (yscrollcommand = self.scrollBar.set)
        self.scrollBar.config (command = self.description.yview)

        if exists ('Documentation/{}.txt'.format (argv[1])):
            self.description.insert (END, open ('Documentation/{}.txt'.format (argv[1]), 'r').read ())

        else:
            self.description.insert (END, "There's no documentation for this type, sorry...\nPlease wait a future update !")

        if exists ('Images/{}.png'.format (argv[1])):
            self.picture.config (file = 'Images/{}.png'.format (argv[1]))

            self.canvas.create_image (256, 256, image = self.picture)
            self.canvas.move (self.picture, 0, -256)

            self.canvas.grid (column = 0, row = 0)

        else:
            self.description.insert (END, "\n\nThere's no picture of this object type yet, sorry !")


        self.description.config (state = DISABLED)


        self.description.grid (column = 1, row = 0)
        self.scrollBar.grid (column = 2, row = 0, sticky = 'ns')


##########################################################


interface = Interface (window)

interface.mainloop ()
