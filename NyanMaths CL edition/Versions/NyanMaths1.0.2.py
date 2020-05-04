# -*-coding:utf-8 -*


"""
NyanMaths CL version 1.xx (Main module) - Created by MemeTech INC

In the documentation, you can see all functionalities of this application.

Creator : NY4N_M4THS
"""


from os import system

from os.path import exists

from time import sleep

import re


if exists ('Startup configuration.pastouche'):
    startupConf = open ('Startup configuration.pastouche').read ().split (' ')

else:
    startupConf = ['1', '1', 'f0', '3.10', '1']


system ("cls")
system ("color {}".format (startupConf[2]))
system ("title Welcome to NyanMaths (Version 1.0.2) !")


pi = 3.141592653589793238462


def prime (x):
    if x < 1 or x - int(x):
        print ("\n Invalid parameter in prime(x) : x < 1 or x is not interger\n")

    elif x == 1:
        return 0

    elif x < 4:
        return 1

    else:
        div = 2
        sqrtx = int(sqrt (x)) + 1

        while div < sqrtx:
            if not x % div:
                return 0
            div += 1

        return 1

def square (x):
    return x * x

def cube (x):
    return x * x * x

def power (x, y):
    return x ** y

def sqrt (x):
    return x ** 0.5

def fact (x):
    if x < 0 or x - int(x):
        print ("\n Invalid parameter in fact (x) : x < 0 or x is not interger !\n")

    elif x < 2:
        return 1

    else:
        y = x - 1
        while y > 1:
            x *= y
            y -= 1

        return x

def easter_egg (pss):
    r = input ("\n 3 + 3 = ")

    try:
        r = int (r)
        assert r == 6

    except:
        print ("\n Error !\n")

    else:
        if exists ("datHelp") and exists ("__datHelp__"):
            if open ("datHelp", 'r').read () == pss:
                print ("\n You are worthy to see that :\n")
                sleep (2)
                print (open ("__datHelp__", 'r').read ())

            else:
                print ("\n Nevermind, it is not the good password !")

        else:
            print ("\n Sorry, the easter egg is not available, please reinstall this application to fix it !")

def displayHelp ():
    if exists ("Versions/help{}.pastouche".format (startupConf[3])):
        helpFile = open ("Versions/help{}.pastouche".format (startupConf[3]), 'r')
        print (helpFile.read ())
        helpFile.close ()

    else:
        print ("\n My file help.pastouche is missing in my folder : may I recover it ?\n If you have not touched anything, please reinstall this application to fix this issue !")

##########################################################
######################   Main code   ############################
##########################################################

print ("\n Welcome to NyanMaths command line edition !\n If you don't know how to use it : RTFM !\n\n")

if int (startupConf[1]) == 1:
    displayHelp ()

if 1:
    if int (startupConf[0]) == 1:

        ##########################################################
        ######################   All fonctionnalities   #######################
        ##########################################################

        class Ball:
            def __init__ (self, radius):
                if radius > 0:
                    self._radius = radius

                else:
                    print ("\n Invalid radius : radius < 0 !\n")

            def _getRadius (self):
                return self._radius

            def _getDiameter (self):
                return self._radius * 2

            def _getVolume (self):
                return self._radius**3 * (4 / 3) * pi

            def _getSurface (self):
                return self._radius**2 * 4 * pi

            def _setRadius (self, nRadius):
                if nRadius > 0:
                    self._radius = nRadius

                else:
                    print ("\n Invalid new radius : radius < 0 !\n")

            def _setDiameter (self, nDiameter):
                if nDiameter > 0:
                    self._radius = nDiameter / 2

                else:
                    print ("\n Invalid new diameter : diameter < 0 !\n")

            def _setVolume (self, nVolume):
                if nVolume > 0:
                    self._radius = (nVolume / pi / (4 / 3))**(1 / 3)

                else:
                    print ("\n Invalid new volume : volume < 0 !\n")

            def _setSurface (self, nSurface):
                if nSurface > 0:
                    self._radius = (nSurface / 4 / pi)**0.5

                else:
                    print ("\n Invalid new surface : surface < 0 !\n")

            radius = property (_getRadius, _setRadius)
            diameter = property (_getDiameter, _setDiameter)
            volume = property (_getVolume, _setVolume)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Cone:
            def __init__ (self, radius, height):
                if radius > 0 and height > 0:
                    self._radius = radius
                    self._height = height

                elif radius > 0:
                    print ("\n Invalid height : height < 0 !\n")

                else:
                    print ("\n Invalid radius : height < 0 !\n")

            def _getRadius (self):
                return self._radius

            def _getDiameter (self):
                return self._radius * 2

            def _getHeight (self):
                return self._height

            def _getVolume (self):
                return self._radius**2 * pi * self._height * (1 / 3)

            def _setRadius (self, nRadius):
                if nRadius > 0:
                    self._radius = nRadius

                else:
                    print ("\n Invalid new radius : radius < 0 !\n")

            def _setDiameter (self, nDiameter):
                if nDiameter > 0:
                    self._radius = nDiameter / 2

                else:
                    print ("\n Invalid new diameter : diameter < 0 !\n")

            def _setHeight (self, nHeight):
                if nHeight > 0:
                    self._height = nHeight

                else:
                    print ("\n Invalid new height : height < 0 !\n")

            def _setVolume (self, nVolume):
                print ("\n Impossible to change it !\n")

            radius = property (_getRadius, _setRadius)
            diameter = property (_getDiameter, _setDiameter)
            height = property (_getHeight, _setHeight)
            volume = property (_getVolume, _setVolume)

        ##########################################################

        class Cube:
            def __init__ (self, edge):
                if edge > 0:
                    self._edge = edge

                else:
                    print ("\n Invalid edge : edge < 0 !\n")

            def _getEdge (self):
                return self._edge

            def _getVolume (self):
                return self._edge**3

            def _getSurface (self):
                return self._edge**2 * 6

            def _setEdge (self, nEdge):
                if nEdge > 0:
                    self._edge = nEdge

                else:
                    print ("\n Invalid new edge : edge < 0 !\n")

            def _setVolume (self, nVolume):
                if nVolume > 0:
                    self._edge = nVolume**(1 / 3)

                else:
                    print ("\n Invalid new volume : volume < 0 !\n")

            def _setSurface (self, nSurface):
                if nSurface > 0:
                    self._edge = (nSurface / 6)**0.5

                else:
                    print ("\n Invalid new surface : surface < 0 !\n")

            edge = property (_getEdge, _setEdge)
            volume = property (_getVolume, _setVolume)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Cuboid:
            def __init__ (self, length, width, height):
                if length > 0 and width > 0 and height > 0:
                    self._length = length
                    self._width = width
                    self._height = height

                else:
                    print ("\n Invalid values : measures must be positive and greater than 0 !\n")

            def _getLength (self):
                return self._length

            def _getWidth (self):
                return self._width

            def _getHeight (self):
                return self._height

            def _getVolume (self):
                return self._length * self._width * self._height

            def _getSurface (self):
                return 2 * (self._length * self._width + self._length * self._height + self._width * self._height)

            def _setLength (self, nLength):
                if nLength > 0:
                    self._length = nLength

                else:
                    print ("\n Invalid new length : length < 0 !\n")

            def _setWidth (self, nWidth):
                if nWidth > 0:
                    self._width = nWidth

                else:
                    print ("\n Invalid new width : width < 0 !\n")

            def _setHeight (self, nHeight):
                if nHeight > 0:
                    self._height = nHeight

                else:
                    print ("\n Invalid new height : height < 0 !\n")

            def _setVolume (self, nVolume):
                print ("\n Impossible to change it !\n")

            def _setSurface (self, nSurface):
                print ("\n Impossible to change it !\n")

            length = property (_getLength, _setLength)
            width = property (_getWidth, _setWidth)
            height = property (_getHeight, _setHeight)
            volume = property (_getVolume, _setVolume)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Cylinder:
            def __init__ (self, radius, height):
                if radius > 0 and height > 0:
                    self._radius = radius
                    self._height = height

                elif radius > 0:
                    print ("\n Invalid height : height < 0 !\n")

                else:
                    print ("\n Invalid radius : radius < 0 !\n")

            def _getRadius (self):
                return self._radius

            def _getDiameter (self):
                return self._radius * 2

            def _getHeight (self):
                return self._height

            def _getVolume (self):
                return self._radius**2 * pi * self._height

            def _getBaseSurface (self):
                return self._radius**2 * pi

            def _getSurface (self):
                return 2 * pi * self._radius * self._height + self._radius**2 * pi * 2

            def _setRadius (self, nRadius):
                if nRadius > 0:
                    self._radius = nRadius

                else:
                    print ("\n Invalid new radius : radius < 0 !\n")

            def _setDiameter (self, nDiameter):
                if nDiameter > 0:
                    self._radius = nDiameter / 2

                else:
                    print ("\n Invalid new diameter : diameter < 0 !\n")

            def _setHeight (self, nHeight):
                if nHeight > 0:
                    self._height = nHeight

                else:
                    print ("\n Invalid new height : height < 0 !\n")

            def _setVolume (self, nVolume):
                print ("\n Impossible to change it !\n")

            def _setBaseSurface (self, nBaseSurface):
                if nBaseSurface > 0:
                    self._radius = (nBaseSurface / pi)**0.5

                else:
                    print ("\n Invalid new base surface : base surface < 0 !\n")

            def _setSurface (self, nSurface):
                print ("\n Impossible to change it !\n")

            radius = property (_getRadius, _setRadius)
            diameter = property (_getDiameter, _setDiameter)
            height = property (_getHeight, _setHeight)
            baseSurface = property (_getBaseSurface, _setBaseSurface)
            volume = property (_getVolume, _setVolume)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Disk:
            def __init__ (self, radius):
                if radius > 0:
                    self._radius = radius

                else:
                    print ("\n Invalid radius : radius < 0 !\n")

            def _getRadius (self):
                return self._radius

            def _getDiameter (self):
                return self._radius * 2

            def _getPerimeter (self):
                return self._radius * 2 * pi

            def _getSurface (self):
                return self._radius**2 * pi

            def _setRadius (self, nRadius):
                if nRadius > 0:
                    self._radius = nRadius

                else:
                    print ("\n Invalid new radius : radius < 0 !\n")

            def _setDiameter (self, nDiameter):
                if nDiameter > 0:
                    self._radius = nDiameter / 2

                else:
                    print ("\n Invalid new diameter : diameter < 0 !\n")

            def _setPerimeter (self, nPerimeter):
                if nPerimeter > 0:
                    self._radius = nPerimeter / 2 / pi

                else:
                    print ("\n Invalid new perimeter : perimeter < 0 !\n")

            def _setSurface (self, nSurface):
                if nSurface > 0:
                    self._radius = (nSurface / pi)**0.5

                else:
                    print ("\n Invalid new surface : surface < 0 !\n")

            radius = property (_getRadius, _setRadius)
            diameter = property (_getDiameter, _setDiameter)
            perimeter = property (_getPerimeter, _setPerimeter)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Prism:
            def __init__ (self, baseSurface, height):
                if baseSurface > 0 and height > 0:
                    self._baseSurface = baseSurface
                    self._height = height

                elif baseSurface > 0:
                    print ("\n Invalid height : height < 0 !\n")

                else:
                    print ("\n Invalid base surface : base surface < 0 !\n")

            def _getBaseSurface (self):
                return self._baseSurface

            def _getHeight (self):
                return self._height

            def _getVolume (self):
                return self._baseSurface * self._height

            def _setBaseSurface (self, nBaseSurface):
                if nBaseSurface > 0:
                    self._baseSurface = nBaseSurface

                else:
                    print ("\n Invalid new base surface : base surface < 0 !\n")

            def _setHeight (self, nHeight):
                if nHeight > 0:
                    self._height = nHeight

                else:
                    print ("\n Invalid new height : height < 0 !\n")

            def _setVolume (self, nVolume):
                print ("\n Impossible to change it !\n")

            baseSurface = property (_getBaseSurface, _setBaseSurface)
            height = property (_getHeight, _setHeight)
            volume = property (_getVolume, _setVolume)

        ##########################################################

        class Pyramid:
            def __init__ (self, baseSurface, height):
                if baseSurface > 0 and height > 0:
                    self._baseSurface = baseSurface
                    self._height = height

                elif baseSurface < 0:
                    print ("\n Invalid base surface : base surface < 0 !\n")

                else:
                    print ("\n Invalid height : height < 0 !\n")

            def _getBaseSurface (self):
                return self._baseSurface

            def _getHeight (self):
                return self._height

            def _getVolume (self):
                return self._baseSurface * self._height * (1 / 3)

            def _setBaseSurface (self, nBaseSurface):
                if nBaseSurface > 0:
                    self._baseSurface = nBaseSurface

                else:
                    print ("\n Invalid new base surface : base surface < 0 !\n")

            def _setHeight (self, nHeight):
                if nHeight > 0:
                    self._height = nHeight

                else:
                    print ("\n Invalid new height : height < 0 !\n")

            def _setVolume (self, nVolume):
                print ("\n Impossible to change it !\n")

            baseSurface = property (_getBaseSurface, _setBaseSurface)
            height = property (_getHeight, _setHeight)
            volume = property (_getVolume, _setVolume)

        ##########################################################

        class Rectangle:
            def __init__ (self, length, width):
                if length > 0 and width > 0:
                    self._length = length
                    self._width = width

                elif length > 0:
                    print ("\n Invalid width : width < 0 !\n")

                else:
                    print ("\n Invalid length : length < 0 !\n")

            def _getLength (self):
                return self._length

            def _getWidth (self):
                return self._width

            def _getPerimeter (self):
                return 2 * (self._length + self._width)

            def _getSurface (self):
                return self._length * self._width

            def _setLength (self, nLength):
                if nLength > 0:
                    self._length = nLength

                else:
                    print ("\n Invalid new length : length < 0 !\n")

            def _setWidth (self, nWidth):
                if nWidth > 0:
                    self._width = nWidth

                else:
                    print ("\n Invalid new width : width < 0 !\n")

            def _setPerimeter (self, nPerimeter):
                print ("\n Impossible to change it !\n")

            def _setSurface (self, nSurface):
                print ("\n Impossible to change it !\n")


            length = property (_getLength, _setLength)
            width = property (_getWidth, _setWidth)
            perimeter = property (_getPerimeter, _setPerimeter)
            surface = property (_getSurface, _setSurface)

        ##########################################################

        class Square:
            def __init__ (self, side):
                if side > 0:
                    self._side = side

                else:
                    print ("\n Invalid side : side < 0 !\n")

            def _getSide (self):
                return self._side

            def _getPerimeter (self):
                return self._side * 4

            def _getSurface (self):
                return self._side**2

            def _setSide (self, nSide):
                if nSide > 0:
                    self._side = nSide

                else:
                    print ("\n Invalid new side : side < 0 !\n")

            def _setPerimeter (self, nPerimeter):
                if nPerimeter > 0:
                    self._side = nPerimeter / 4

                else:
                    print ("\n Invalid new perimeter : perimeter < 0 !\n")

            def _setSurface (self, nSurface):
                if nSurface > 0:
                    self._side = nSurface**0.5

                else:
                    print ("\n Invalid new surface : surface < 0 !\n")

            side = property (_getSide, _setSide)
            perimeter = property (_getPerimeter, _setPerimeter)
            surface = property (_getSurface, _setSurface)

        print ("\n\n Objects module is loaded !")

    else:
        print ("\n\n You can load objects module at when you start the app, if you are interested.\n Check the documentation if you want to see more.")

print ("\n")


########################################  Main code  #####################################

cmd = ''

while True:  # Main loop
    cmd = input (" >>> ")
    cmd = re.sub (' ', '', cmd)

    _r = None  # The return-value of user's commands


    if cmd in ['quit', 'exit']:
        break

    if cmd != '':  # If the user entered something
        try:
            if (('=' in cmd) and (not '==' in cmd)):  # If the user want to create an object
                exec (cmd)
                print ("\n", end = '')

            else:
                _r = eval (cmd)   # If the user want the app to compute something

            if _r is not None:
                if (type (_r) is complex) or (type (_r) is int) or (type (_r) is float):   # If there's a result to display (number)
                    print ("\n", _r, "\n")

                else:   # If the result is a string or a boolean
                    print ("\n ", _r, "\n")


        # Exceptions managment

        except TypeError:
            print ("\n Invalid operand type !\n")

        except NameError:
            print ("\n This variable or type doesn't exist !\n Don't forget to capitalize object types !\n")

        except ZeroDivisionError:
            print ("\n Newbie's error #0 : division by zero !\n")

        except ValueError:
            print ("\n You gave an invalid value somewhere !\n")

        except KeyboardInterrupt:
            exit (0)

        except RuntimeError:  # If the exception was already managed
            pass

        except:
            print ("\n An unknown error has occured, sorry !\n")
