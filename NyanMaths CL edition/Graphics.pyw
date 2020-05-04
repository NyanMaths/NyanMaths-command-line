# -*-coding:Latin-1 -*

"""
This module can display a description of your objects.

Creator : NY4N_M4THS
"""

from os.path import exists
from sys import argv

from tkinter import *


if len (argv) < 4:
    exit (1)

##########################################################

window = Tk ()

window.resizable (width = "False", height = "False")
window.title ("NyanMaths - Informations about object {0}".format (argv[1]))

if exists ("Icon.ico"):
    window.iconbitmap ("Icon.ico")


_decimals_ = int (argv[2])

pi = 3.141592653589793238462


##########################################################


def f (x):
    if type (x) is complex:
        if not x.real and not x.imag:
            return 0

        elif not x.real:
            return f (x.imag) * 1j

        elif not x.imag:
            return f (x.real)

        else:
            return f (complex (round (x.real, _decimals_), round (x.imag, _decimals_)))

    if abs (x) > 1 / 10**(_decimals_ + 1):
        if not abs (x) - abs (int (x)):
            return int (x)
    
        x = round (x, _decimals_)
    
        if not abs (x) - abs (int (x)):
            return int (x)

    return x


class Interface (Frame):
    def __init__ (self, fenetre):
        Frame.__init__ (self, fenetre)
        self.pack (fill = BOTH)

        self.mainFrame = Frame (self)

        self.picture = PhotoImage ()

        self.canvas = Canvas (self.mainFrame, width = 512, height = 512, confine = False)
        self.canvas.create_image (256, 256, image = self.picture)
        self.canvas.move (self.picture, 0, -256)

        self.description = Label (self.mainFrame, font = 'Helcavita 20',  justify = 'left')
        self.warning = Label (self, text = "The illustration doesn't have the same proportions than your {}".format (argv[1]), font = 'Helcavita 9', foreground = 'red')

        self.canvas.pack (side = LEFT)
        self.description.pack (side = RIGHT)

        self.mainFrame.pack ()

        self.values = ''

        i = 3
        while i < len (argv) - 1:
            self.values += '{}, '.format (f (float (argv[i])))

            i += 1

        self.values += '{}'.format (f (float (argv[i])))

        try:
            exec ('self.{0} ({1})'.format (argv[1], self.values))

        except:
            self.description.config (text = "Loading error !\nSome files are missing in my folder.")



    def square (self, side, permimeter, surface, apothem, diagonale):
        self.picture.config (file = 'Images/Square.png')

        self.description.config (text = "Side : {0}\nPerimeter : {1}\nSurface : {2}\nApothem : {3}\nDiagonale : {4}".format (side, permimeter, surface, apothem, diagonale))


    def rectangle (self, length, width, perimeter, surface, diagonale):
        if length == width:
            self.picture.config (file = 'Images/Square.png')
            self.description.config (text = "Side : {0}\nPerimeter : {1}\nSurface : {2}\nDiagonale : {3}".format (length, perimeter, surface, diagonale))

        else:
            self.picture.config (file = 'Images/Rectangle.png')
            self.warning.pack ()

            self.description.config (text = "Length : {0}\nWidth : {1}\nPerimeter : {2}\nSurface : {3}\nDiagonale : {4}".format (length, width, perimeter, surface, diagonale))


    def cube (self, edge, volume, surface, diagonale):
        self.picture.config (file = 'Images/Cube.png')

        self.description.config (text = "Edge : {0}\nVolume : {1}\nSurface : {2}\nDiagonale : {3}".format (edge, volume, surface, diagonale))


    def cuboid (self, length, width, height, volume, surface, diagonale):
        if length == width == height:
            self.picture.config (file = 'Images/Cube.png')

            self.description.config (text = "Edge : {0}\nVolume : {1}\nSurface : {2}\nDiagonale : {3}".format (length, volume, surface, f (diagonale)))

        else:
            self.picture.config (file = 'Images/Cuboid.png')
            self.warning.pack ()

            self.description.config (text = "Length : {0}\nWidth : {1}\nHeight : {2}\nVolume : {3}\nSurface : {4}\nDiagonale : {5}".format (length, width, height, volume, surface, f (diagonale)))


    def disk (self, radius, diameter, perimeter, surface):
        self.picture.config (file = 'Images/Disk.png')

        self.description.config (text = "Radius : {0}\nDiameter : {1}\nPerimeter : {2}\nSurface : {3}".format (radius, diameter, perimeter, surface))


    def ellipse (self, a, b, perimeter, surface):
        if a == b:
            self.picture.config (file = 'Images/Disk.png')
            self.description.config (text = "Radius : {0}\nDiameter : {1}\nPerimeter : {2}\nSurface : {3}".format (a, f (2 * a), perimeter, surface))

        else:
            self.picture.config (file = 'Images/Ellipse.png')
            self.warning.pack ()

            self.description.config (text = "A : {0}\nB : {1}\nPerimeter : {2}\nSurface : {3}".format (a, b, perimeter, surface))


    def pyramid (self, baseSurface, height, volume):
        self.picture.config (file = 'Images/Pyramid.png')
        self.warning.pack ()

        self.description.config (text = "Base surface : {0}\nHeight : {1}\nVolume : {2}".format (baseSurface, height, volume))


    def ball (self, radius, diameter, volume, surface):
        self.picture.config (file = 'Images/Ball.png')

        self.description.config (text = "Radius : {0}\nDiameter : {1}\nVolume : {2}\nSurface : {3}".format (radius, diameter, volume, surface))


    def ellipsoid (self, a, b, c, volume):
        if a == b == c:
            self.picture.config (file = 'Images/Ball.png')
            self.description.config (text = "Radius : {0}\nDiameter : {1}\nVolume : {2}\nSurface : {3}".format (a, f (2 * a), volume, f (4 * pi * a * a)))

        else:
            self.picture.config (file = 'Images/Ellipsoid.png')
            self.warning.pack ()

            self.description.config (text = "A : {0}\nB : {1}\nC : {2}\nVolume : {3}".format (a, b, c, volume))


    def cone (self, radius, diameter, height, baseSurface, volume, lateralSurface):
        if height != 0:
            self.picture.config (file = 'Images/Cone.png')
            self.warning.pack ()
    
            self.description.config (text = "Radius : {0}\nDiameter : {1}\nHeight : {2}\nBase surface : {3}\nVolume : {4}\nLateral surface : {5}".format (radius, diameter, height, baseSurface, volume, lateralSurface))

        else:
            self.picture.config (file = 'Images/Disk.png')
            self.description.config (text = "Radius : {0}\nDiameter : {1}\nPerimeter : {2}\nSurface : {3}".format (radius, diameter, f (pi * 2 * radius), baseSurface))            

    def cylinder (self, radius, diameter, height, baseSurface, volume, surface):
        if height != 0:
            self.picture.config (file = 'Images/Cylinder.png')
            self.warning.pack ()

            self.description.config (text = "Radius : {0}\nDiameter : {1}\nHeight : {2}\nBase surface : {3}\nVolume : {4}\nSurface : {5}".format (radius, diameter, height, baseSurface, volume, surface))

        else:
            self.picture.config (file = 'Images/Disk.png')
            self.description.config (text = "Radius : {0}\nDiameter : {1}\nPerimeter : {2}\nSurface : {3}".format (radius, diameter, f (pi * 2 * radius), baseSurface))


    def prism (self, baseSurface, height, volume):
        self.picture.config (file = 'Images/Prism.png')
        self.warning.pack ()

        self.description.config (text = "Base surface : {0}\nHeight : {1}\nVolume : {2}\n".format (baseSurface, height, volume))



##########################################################


interface = Interface (window)

interface.mainloop ()

