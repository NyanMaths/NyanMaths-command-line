# -*-coding:utf-8 -*


"""
NyanMaths CL version 2.xx (Main module) - Created by MemeTech INC

In the documentation, you can see all functionalities of this application.

Creator : NY4N_M4THS
"""


from os import system
from os.path import exists

from threading import Thread

from time import sleep

from math import gcd
from cmath import log as log_

import re


if exists ('Startup configuration.pastouche'):
    startupConf = open ('Startup configuration.pastouche').read ().split (' ')

else:
    startupConf = ['1', '1', 'f0', '2.6.2', '1']


system ("title NyanMaths  --  Loading...")

system ("cls")
system ("color {}".format (startupConf[2]))


#######################  Constants  #####################

pi = 3.141592653589793238462
e = 2.71828182845904523536
phi = 1.618033988749894848204
G = 6.67408e-11

drg = 'drg'
rad = 'rad'

_precision_ = 3
_unit_ = rad

if exists ('Versions/Conf.pastouche'):
    config = open ('Versions/Conf.pastouche', 'r').read ().split (' ')

    _precision_ = int (config[0])

    _unit_ = config[1]

else:
    open ('Versions/Conf.pastouche', 'w').write ("{0} {1}".format (_precision_, _unit_))

moon, earth = "Moon", "Earth"
g = {"Moon" : 1.622, "Earth" : 9.80665}


#######################  Graphical objects representation  #####################


class GraphicalDescription (Thread):
    def __init__ (self, cmd):
        self.cmd = cmd

        self.start ()

    def start (self):
        system ('Graphics.pyw {}'.format (self.cmd))


#######################  Functions  #####################


def prime (x):
    if x < 1 or type (x) is float:
        print ("\n Invalid parameter in prime(x) : x < 1 or x is decimal !\n")

    elif x == 1:
        return False

    elif x < 4:
        return True

    elif not x % 2:
        return False

    else:
        div = 3
        sqrtx = int (sqrt (x)) + 1

        while div < sqrtx:
            if not x % div:
                return False

            div += 2

        return True

def divisible (n, x):
    if (type (n) is int) and (type (x) is int):
        return bool (not n % x)

    else:
        print ("\n Did you try to crash me ???\n Kill in 2 seconds...", end = '')
        sleep (2)
        BSOD ()

def square (x):
    return trans (x * x)

def cube (x):
    return trans (x * x * x)

def sqrt (x):
    if x != 0:
        return trans (e**(0.5 * log_ (x)))

    return 0

def power (x, y):
    return trans (pow (x, y))

def exp (x):
    return trans (e**x)

def cuberoot (x):
    if x != 0:
        return trans (e**(1 / 3 * log_ (x)))

    return 0

def root (x, y):
    if y != 0:
        return trans (e**(1 / x * log_ (y)))

    return 0

def fact (x):
    if x < 0 or type (x) is not int:
        print ("\n Invalid parameter in fact (x) : x < 0 or x is decimal !\n")

    y = x
    r = 1

    while y > 1:
        r *= y
        y -= 1

    return r

def pythagore (a, b, c):
    if (a == 0) ^ (b == 0) ^ (c == 0):
        if not a:
            return trans (sqrt (c * c - b * b))

        elif not b:
            return trans (sqrt (c * c - a * a))

        else:
            return trans (sqrt (a * a + b * b))

    else:
        if a * a + b * b == c * c:
            print ("\n This triangle is right-angled !\n")

        else:
            print ("\n This triangle is not right-angled !\n")

def syracuse (x):
    if x < 1 or type (x) is not int:
        print ("\n Invalid argument : it must be a positive interger !\n")

    else:
        while x != 1:
            if x % 2:
                x = x * 3 + 1

            else:
                x /= 2

            print ("\n", x, end = '')

        print ("\n ...\n")


def log (x):
    return trans (log_ (x))

def sin (x):
    if _unit_ == 'rad':
        return trans ((e**(x * 1j) - e**(-x * 1j)) / 2j)

    return trans ((e**(x / 180 * pi * 1j) - e**(-x / 180 * pi * 1j)) / 2j)

def cos (x):
    if _unit_ == 'rad':
        return trans ((e**(x * 1j) + e**(-x * 1j)) / 2)

    return trans ((e**(x / 180 * pi * 1j) + e**(-x / 180 * pi * 1j)) / 2)

def tan (x):
    return trans (sin (x) / cos (x))

def asin (x):
    if _unit_ == 'rad':
        return trans (-(1j * log_ (1j * x + sqrt (1 - x * x))))

    return trans (-1j * log_ (1j * x + sqrt (1 - x * x)) * 180 / pi)

def acos (x):
    if _unit_ == 'rad':
        return trans (pi / 2 - asin (x))

    return trans (-1j * log_ (x + 1j * sqrt (1 - x * x)) * 180 / pi)

def atan (x):
    if _unit_ == 'rad':
        return trans ((log_ (1 + 1j * x) - log_ (1 - 1j * x)) / 2j)

    return trans ((log_ (1 + 1j * x) - log_ (1 - 1j * x)) / 2j * 180 / pi)

#######################  Apps  #####################

def run (cmd):
    cmd ()

def app_prime ():
    n = input ("\n This application calculates all prime numbers\n from an odd positive non-zero number to... Another greater positive number !\n Beware : the last numbers will be deleted !\n\n Calculate the prime numbers from ")
    MAX = input ("\n To ")

    try:
        n = int (n)
        MAX = int (MAX)

        assert n % 2 == 1
        assert n > 0
        assert n < MAX
        assert MAX < 100000001

    except:
        print ("\n\n Do not try to crash me !\n")
        return 1

    else:
        MAX += 1

        open ("User data/Prime Numbers.txt", 'w').close ()

        with open ("User data/Prime Numbers.txt", 'a') as numbers_file:
            if n < 4:
                numbers_file.write ("2\n3\n")
                n = 5

            while n < MAX:
                div = 2
                sqrtn = n**0.5 + 1
                b = 1

                while div < sqrtn:
                    if not n % div:
                        b = 0
                        break

                    div += 1

                if b:
                    print (n, file = numbers_file)

                n += 1

        print ("\n\n The prime numbers are written in C:/MemeTech/NyanMaths CL Launcher/User data/Prime Numbers.txt\n Why not keep this file ?\n")

def dividers ():
    n = input ("\n What is the number of which you want to know the dividers :  ")

    try:
        print ("\n")
        n = int (n)

        assert n < 1000000001

    except:
        print ("\n Do not try to crash me !\n")
        return 1

    else:
        x = 0
        div = int (n / 2) + 1

        while div > 1:
            if n % div == 0:
                print (" By {0}       {1} times".format (div, int (n / div)))
                x += 1

            div -= 1

        if x > 0:
            print ("\n It is all !\n")

        else:
            print ("\n There is no divider : {} is prime !\n".format (n))

def UIR ():
    print ("\n Thanks to this application, you can calculate the relationship between intensity, electric tension and resistance.\n Give me 0 for the value you want to get.")

    try:
        u = float (input ("\n Input elecric tension :  "))
        r = float (input ("\n Resistance, please :  "))
        i = float (input ("\n To finish, intensity (Not \"please\") :  "))

        assert (u == 0) ^ (r == 0) ^ (i == 0)

    except:
        print ("\n\n Do not try to crash me !\n")

    else:
        if u == 0:
            print ("\n Electric tension :  {}\n".format (trans (i * r)))

        elif i == 0:
            print ("\n Intensity :  {}\n".format (trans (u / r)))

        else:
            print ("\n Resistance :  {}\n".format (trans (u / i)))

def VDT ():
    print ("\n Thanks to this application, you can calculate the relationship between speed, distance and time.\n Give me 0 for the value you want to get.")

    try:
        v = float (input ("\n Input speed :  "))
        d = float (input ("\n Distance, please :  "))
        t = float (input ("\n To finish, time (Not \"please\") :  "))

        assert (v == 0) ^ (d == 0) ^ (t == 0)

    except:
        print ("\n\n Do not try to crash me !\n")
        sleep (2)
        BSOD ()

    else:
        if v == 0:
            print ("\n Speed :  {}\n".format (trans (d / t)))

        elif d == 0:
            print ("\n Distance :  {}\n".format (trans (v * t)))

        else:
            print ("\n Time :  {}\n".format (trans (d / v)))

def MV ():
    print ("\n Thanks to this application, you can calculate the relationship between density, weight and volume.\n Give me 0 for the value you want to get.")

    try:
        r = float (input ("\n Input density :  "))
        m = float (input ("\n Weight, please :  "))
        v = float (input ("\n To finish, volume (Not \"please\") :  "))

        assert (r == 0) ^ (m == 0) ^ (v == 0)

    except:
        print ("\n\n Do not try to crash me !\n Kill in two seconds...")
        sleep (2)
        BSOD ()

    else:
        if r == 0:
            print ("\n Density :  {}\n".format (trans (m / v)))

        elif m == 0:
            print ("\n Weight :  {}\n".format (trans (r * v)))

        else:
            print ("\n Volume :  {}\n".format (trans (m / r)))

def temperature ():
    print ("\n Helloooooooo !\n Thanks to this application, you can convert temperature units :\n\n a) Celsius --> Fahreneit\n b) Celsius --> Kelvin\n c) Fahreneit --> Celsius\n d) Fahreneit --> Kelvin\n e) Kelvin --> Celsius\n f) Kelvin --> Fahreneit")

    c = input ("\n\n Choose the conversion : ")

    if c == 'a' or c == 'A':
        try:
            n = float (input ("\n Input the value in °C : "))

        except:
            BSOD ()

        print ("\n\n {0}°C = {1}°F\n".format (trans (n), trans ((1.8 * n) + 32)))

    elif c == 'b' or c == 'B':
        try:
            n = float (input ("\n Input the value in °C : "))

        except:
            BSOD ()

        print ("\n\n {0}°C = {1}°K\n".format (trans (n), trans (n + 273.15)))

    elif c == 'c' or c == 'C':
        try:
            n = float (input ("\n Input the value in °F : "))

        except:
            BSOD ()

        print ("\n\n {0}°F = {1}°C\n".format (trans (n), trans ((n - 32) / 1.8)))

    elif c == 'd' or c == 'D':
        try:
            n = float (input ("\n Input the value in °F : "))

        except:
            BSOD ()

        print ("\n\n {0}°F = {1}°K\n".format (trans (n), trans ((n - 32) / 1.8 + 273.15)))

    elif c == 'e' or c == 'E':
        try:
            n = float (input ("\n Input the value in °K : "))

        except:
            BSOD ()

        print ("\n\n {0}°K = {1}°C\n".format (trans (n), trans (n - 273.15)))

    elif c == 'f' or c == 'F':
        try:
            n = float (input ("\n Input the value in °K : "))

        except:
            BSOD ()

        print ("\n\n {0}°K = {1}°F\n".format (trans (n), trans ((n - 273.15) * 1.8 + 32)))

    else:
        BSOD (False)


#######################  Others  #####################


def degrees (x):
    return trans (x *180 / pi)

def radians (x):
    return trans (x / 180 * pi)

def setPrecision (x):
    if x > -1 and x < 13:
        _precision_ = x
        open ('Versions/Conf.pastouche', 'w').write ('{0} {1}'.format (x, _unit_))

        print ("\n Precision changed ! Restart needed to apply.\n")

    else:
        print ("\n You had to input a number between 0 and 12 !\n ")

def setUnit (x):
    if x == 'drg' or x == 'rad':
        _unit_ = x
        open ('Versions/Conf.pastouche', 'w').write ('{0} {1}'.format (_precision_, x))

        print ("\n Unit changed ! Restart needed to apply.\n")

    else:
        print ("\n You had to input drg or rad !\n ")

def trans (x):
    if type (x) is complex:
        if x.real == 0 and x.imag == 0:
            return 0

        elif x.real == 0:
            return trans (x.imag) * 1j

        elif x.imag == 0:
            return trans (x.real)

        else:
            return complex (round (x.real, _precision_), round (x.imag, _precision_))

    if (type (x) is float) and (not x - int (x)):
        return int (x)

    x = round (x, _precision_)

    if (type (x) is float) and (not x - int (x)):
        return int (x)

    return x

def BSOD (ex = True):
    system ("BSOD_MEME.pyw")

    if ex:
        exit (0)

def applications ():
    print ("\n You can launch in this version :\n\tapp_prime\n\tdividers\n\tUIR\n\tVDT\n\tDensity\n\ttemperature\n")

def operations ():
    print ("\n + : Addition"
           "\n - : Substraction"
           "\n * : Multiplication"
             "\n / : Division"
             "\n ** Power (3**2 = 3²)"
             "\n // : Integer division"
             "\n\n Logical operators :"
             "\n\n == : Equals to"
             "\n != : Not equals to"
             "\n < : Lesser than"
             "\n > : Greater than"
             "\n\n For example :\n\n>>> 3 + 3 * 5\n18\n\n>>> 3 == sqrt (square (3))\nFalse\n\n")

def displayHelp ():
    if exists ("Versions/help{}.pastouche".format (startupConf[3])):
        helpFile = open ("Versions/help{}.pastouche".format (startupConf[3]), 'r')
        print (helpFile.read ())
        helpFile.close ()

    else:
        print ("\n My file help.pastouche is missing in my folder : may I get it back ?\n If you have not touched anything, please reinstall this application to fix this issue !\n")


##########################################################
##########################   Classes   ##########################
##########################################################


if int (startupConf[1]) == 1:
    displayHelp ()

print ("\n Welcome to NyanMaths Command Line edition !\n If you don't know how to use it : RTFM !\n\n Unit : {0}\n Floating point precision : {1}".format (_unit_, _precision_))


if int (startupConf[0]) == 1:

    ##########################################################
    ######################   All Modules   ###########################
    ##########################################################


    class Ball:
        def __init__ (self, radius = 1):
            if radius > 0:
                self._radius = radius

            else:
                print ("\n Invalid radius : radius < 0 !\n")
                self._radius = 1

        def _getRadius (self):
            return trans (self._radius)

        def _getDiameter (self):
            return trans (self._radius * 2)

        def _getVolume (self):
            return trans (self._radius**3 * (4 / 3) * pi)

        def _getSurface (self):
            return trans (self._radius**2 * 4 * pi)

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
                self._radius = (nVolume / pi * 0.75)**(1 / 3)

            else:
                BSOD ()

        def _setSurface (self, nSurface):
            if nSurface > 0:
                self._radius = (nSurface / 4 / pi)**0.5

            else:
                print ("\n Invalid new surface : surface < 0 !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('ball {4} {0} {1} {2} {3}'.format (self.radius, self.diameter, self.volume, self.surface, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ball (self._radius * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ball (self._radius / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Ball:
                return self.radius == n.radius

            else:
                print ("\n Invalid operand type : they must be two balls !\n")

        def __ne__ (self, n):
            if type (n) is Ball:
                return self.radius != n.radius

            else:
                print ("\n Invalid operand type : they must be two balls !\n")

        radius = property (_getRadius, _setRadius)
        diameter = property (_getDiameter, _setDiameter)
        volume = property (_getVolume, _setVolume)
        surface = property (_getSurface, _setSurface)

    ##########################################################

    class Cone:
        def __init__ (self, radius = 1, height = 1):
            if radius > 0 and height > 0:
                self._radius = radius
                self._height = height

            elif radius > 0:
                print ("\n Invalid height : height < 0 !\n")
                self._height = 1
                self._radius = 1

            else:
                print ("\n Invalid base radius : base radius < 0 !\n")
                self._height = 1
                self._radius = 1

        def _getRadius (self):
            return trans (self._radius)

        def _getDiameter (self):
            return trans (self._radius * 2)

        def _getHeight (self):
            return trans (self._height)

        def _getBaseSurface (self):
            return trans (self._radius**2 * pi)

        def _getVolume (self):
            return trans (self._radius**2 * pi * self._height * (1 / 3))

        def _getLateralSurface (self):
            return trans (self._radius * pi * sqrt (self._height**2 + self._radius**2))

        def _setRadius (self, nRadius):
            if nRadius > 0:
                self._radius = nRadius

            else:
                print ("\n Invalid new base radius : base radius < 0 !\n")

        def _setDiameter (self, nDiameter):
            if nDiameter > 0:
                self._radius = nDiameter / 2

            else:
                print ("\n Invalid new base diameter : base diameter < 0 !\n")

        def _setHeight (self, nHeight):
            if nHeight > 0:
                self._height = nHeight

            else:
                print ("\n Invalid new height : height < 0 !\n")

        def _setBaseSurface (self, nBaseSurface):
            if nBaseSurface > 0:
                self._radius = (nBaseSurface / pi)**0.5

            else:
                print ("\n Invalid new base surface : base surface < 0 !\n")

        def _setVolume (self, nVolume):
            print ("\n Impossible to change it !\n")

        def _setLateralSurface (self, nLateralSurface):
            print ("\n Impossible to change it !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('cone {6} {0} {1} {2} {3} {4} {5}'.format (self.radius, self.diameter, self.height, self.baseSurface, self.volume, self.lateralSurface, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius *= n
                    self._height *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius /= n
                    self._height /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cone (self._radius * n, self._height * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cone (self._radius / n, self._height / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Cone:
                return self.radius == n.radius and self.height == n.height

            else:
                print ("\n Invalid operand type : they must be two cones !\n")

        def __ne__ (self, n):
            if type (n) is Ball:
                return self.radius != n.radius or self.height != n.height

            else:
                print ("\n Invalid operand type : they must be two cones !\n")

        radius = property (_getRadius, _setRadius)
        diameter = property (_getDiameter, _setDiameter)
        baseSurface = property (_getBaseSurface, _setBaseSurface)
        height = property (_getHeight, _setHeight)
        volume = property (_getVolume, _setVolume)
        lateralSurface = property (_getLateralSurface, _setLateralSurface)

    ##########################################################

    class Cube:
        def __init__ (self, edge = 1):
            if edge > 0:
                self._edge = edge

            else:
                print ("\n Invalid edge : edge < 0 !\n")
                self._edge = 1

        def _getEdge (self):
            return trans (self._edge)

        def _getVolume (self):
            return trans (self._edge**3)

        def _getSurface (self):
            return trans (self._edge**2 * 6)

        def _getDiagonale (self):
            return trans (self._edge * 1.732050807568878)

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

        def _setDiagonale (self, nDiadonale):
            if nDiadonale > 0:
                self._edge = nDiadonale / 1.732050807568878

            else:
                print ("\n Invalid new surface : surface < 0 !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('cube {4} {0} {1} {2} {3}'.format (self.edge, self.volume, self.surface, self.diagonale, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._edge *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._edge /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cube (self._edge * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cube (self._edge / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Cube:
                return self.edge == n.edge

            else:
                print ("\n Invalid operand type : they must be two cubes !\n")

        def __ne__ (self, n):
            if type (n) is Cube:
                return self.edge != n.edge

            else:
                print ("\n Invalid operand type : they must be two cubes !\n")

        edge = property (_getEdge, _setEdge)
        volume = property (_getVolume, _setVolume)
        surface = property (_getSurface, _setSurface)
        diagonale = property (_getDiagonale, _setDiagonale)

    ##########################################################

    class Cuboid:
        def __init__ (self, length = 1, width = 1, height = 1):
            if length > 0 and width > 0 and height > 0:
                self._length = length
                self._width = width
                self._height = height

            else:
                print ("\n Invalid values : the measures must be positive !\n")
                self._length = 1
                self._width = 1
                self._height = 1

        def _getLength (self):
            return trans (self._length)

        def _getWidth (self):
            return trans (self._width)

        def _getHeight (self):
            return trans (self._height)

        def _getVolume (self):
            return trans (self._length * self._width * self._height)

        def _getSurface (self):
            return trans (2 * (self._length * self._width + self._length * self._height + self._width * self._height))

        def _getDiagonale (self):
            return trans ((self._length * self._length + self._width * self._width + self._height * self._height)**0.5)

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

        def _setDiagonale (self, nDiagonale):
            print ("\n Impossible to change it !\n Kill in 2 seconds...")
            sleep (2)
            BSOD ()

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('cuboid {6} {0} {1} {2} {3} {4} {5}'.format (self.length, self.width, self.height, self.volume, self.surface, self.diagonale, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._length *= n
                    self._width *= n
                    self._height *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._length /= n
                    self._width /= n
                    self._height /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cuboid (self._length * n, self._width * n, self._height * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cuboid (self._length / n, self._width / n, self._height / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Cuboid:
                return self.length == n.length and self.width == n.width and self.height == n.height

            else:
                print ("\n Invalid operand type : they must be two cuboids !\n")

        def __ne__ (self, n):
            if type (n) is Cuboid:
                return self.length != n.length or self.width != n.width or self.height != n.height

            else:
                print ("\n Invalid operand type : they must be two cuboids !\n")

        length = property (_getLength, _setLength)
        width = property (_getWidth, _setWidth)
        height = property (_getHeight, _setHeight)
        volume = property (_getVolume, _setVolume)
        surface = property (_getSurface, _setSurface)
        diagonale = property (_getDiagonale, _setDiagonale)

    ##########################################################

    class Cylinder:
        def __init__ (self, radius = 1, height = 1):
            if radius > 0 and height > 0:
                self._radius = radius
                self._height = height

            elif radius > 0:
                print ("\n Invalid height : height < 0 !\n")
                self._radius = 1
                self._height = 1

            else:
                print ("\n Invalid radius : radius < 0 !\n")
                self._radius = 1
                self._height = 1

        def _getRadius (self):
            return trans (self._radius)

        def _getDiameter (self):
            return trans (self._radius * 2)

        def _getHeight (self):
            return trans (self._height)

        def _getVolume (self):
            return trans (self._radius**2 * pi * self._height)

        def _getBaseSurface (self):
            return trans (self._radius**2 * pi)

        def _getSurface (self):
            return trans (2 * pi * self._radius * self._height + self._radius**2 * pi * 2)

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

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('cylinder {6} {0} {1} {2} {3} {4} {5}'.format (self.radius, self.diameter, self.height, self.baseSurface, self.volume, self.surface, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius *= n
                    self._height *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius /= n
                    self._height /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cylinder (self._radius * n, self._height * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Cylinder (self._radius / n, self._height / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Cylinder:
                return self.radius == n.radius and self.height == n.height

            else:
                print ("\n Invalid operand type : they must be two cylinders !\n")

        def __ne__ (self, n):
            if type (n) is Cylinder:
                return self.radius != n.radius or self.height != n.height

            else:
                print ("\n Invalid operand type : they must be two cylinders !\n")

        radius = property (_getRadius, _setRadius)
        diameter = property (_getDiameter, _setDiameter)
        height = property (_getHeight, _setHeight)
        baseSurface = property (_getBaseSurface, _setBaseSurface)
        volume = property (_getVolume, _setVolume)
        surface = property (_getSurface, _setSurface)

    ##########################################################

    class Disk:
        def __init__ (self, radius = 1):
            if radius > 0:
                self._radius = radius

            else:
                print ("\n Invalid radius : radius < 0 !\n")
                self._radius = 1

        def _getRadius (self):
            return trans (self._radius)

        def _getDiameter (self):
            return trans (self._radius * 2)

        def _getPerimeter (self):
            return trans (self._radius * 2 * pi)

        def _getSurface (self):
            return trans (self._radius**2 * pi)

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

        def __getattr__ (self, name):
            print ("\n There's no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('disk {4} {0} {1} {2} {3}'.format (self.radius, self.diameter, self.perimeter, self.surface, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._radius /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Disk (self._radius * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Disk (self._radius / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Disk:
                return self.radius == n.radius

            else:
                print ("\n Invalid operand type : they must be two disk !\n")

        def __ne__ (self, n):
            if type (n) is Disk:
                return self.radius != n.radius

            else:
                print ("\n Invalid operand type : they must be two disk !\n")

        radius = property (_getRadius, _setRadius)
        diameter = property (_getDiameter, _setDiameter)
        perimeter = property (_getPerimeter, _setPerimeter)
        surface = property (_getSurface, _setSurface)

    ##########################################################

    class Prism:
        def __init__ (self, baseSurface = 1, height = 1):
            if baseSurface > 0 and height > 0:
                self._baseSurface = baseSurface
                self._height = height

            elif baseSurface > 0:
                print ("\n Invalid height : height < 0 !\n")
                self._baseSurface = 1
                self._height = 1

            else:
                print ("\n Invalid base surface : base surface < 0 !\n")
                self._baseSurface = 1
                self._height = 1

        def _getBaseSurface (self):
            return trans (self._baseSurface)

        def _getHeight (self):
            return trans (self._height)

        def _getVolume (self):
            return trans (self._baseSurface * self._height)

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

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('prism {3} {0} {1} {2}'.format (self.baseSurface, self.height, self.volume, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._baseSurface *= n * n
                    self._height *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._baseSurface /= n * n
                    self._height /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Prism (self._baseSurface * n * n, self._height * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Prism (self._radius / (n * n), self._height / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        baseSurface = property (_getBaseSurface, _setBaseSurface)
        height = property (_getHeight, _setHeight)
        volume = property (_getVolume, _setVolume)

    ##########################################################

    class Pyramid:
        def __init__ (self, baseSurface = 1, height = 1):
            if baseSurface > 0 and height > 0:
                self._baseSurface = baseSurface
                self._height = height

            elif baseSurface < 0:
                print ("\n Invalid base surface : base surface < 0 !\n")
                self._baseSurface = 1
                self._height = 1

            else:
                print ("\n Invalid height : height < 0 !\n")
                self._baseSurface = 1
                self._height = 1

        def _getBaseSurface (self):
            return trans (self._baseSurface)

        def _getHeight (self):
            return trans (self._height)

        def _getVolume (self):
            return trans (self._baseSurface * self._height * (1 / 3))

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

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('pyramid {3} {0} {1} {2}'.format (self.baseSurface, self.height, self.volume, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._baseSurface *= n * n
                    self._height *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._baseSurface /= n * n
                    self._height /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Pyramid (self._baseSurface * n * n, self._height * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Pyramid (self._baseSurface / (n * n), self._height / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        baseSurface = property (_getBaseSurface, _setBaseSurface)
        height = property (_getHeight, _setHeight)
        volume = property (_getVolume, _setVolume)

    ##########################################################

    class Rectangle:
        def __init__ (self, length = 1, width = 1):
            if length > 0 and width > 0:
                self._length = length
                self._width = width

            elif length > 0:
                print ("\n Invalid width : width < 0 !\n")
                self._length = 1
                self._width = 1

            else:
                print ("\n Invalid length : length < 0 !\n")
                self._length = 1
                self._width = 1

        def _getLength (self):
            return trans (self._length)

        def _getWidth (self):
            return trans (self._width)

        def _getPerimeter (self):
            return trans (2 * (self._length + self._width))

        def _getSurface (self):
            return trans (self._length * self._width)

        def _getDiagonale (self):
            return trans ((self._length * self._length + self._width * self._width)**0.5)

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

        def _setDiagonale (self, nDiagonale):
            print ("\n Impossible to change it !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('rectangle {5} {0} {1} {2} {3} {4}'.format (self.length, self.width, self.perimeter, self.surface, self.diagonale, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._length *= n
                    self._width *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._length /= n
                    self._width /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Rectangle (self._length * n, self._width * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Rectangle (self._length / n, self._width / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Rectangle:
                return self.length == n.length and self.width == n.width

            else:
                print ("\n Invalid operand type : they must be two rectangles !\n")

        def __ne__ (self, n):
            if type (n) is Rectangle:
                return self.length != n.length or self.width != n.width

            else:
                print ("\n Invalid operand type : they must be two rectangles !\n")

        length = property (_getLength, _setLength)
        width = property (_getWidth, _setWidth)
        perimeter = property (_getPerimeter, _setPerimeter)
        surface = property (_getSurface, _setSurface)
        diagonale = property (_getDiagonale, _setDiagonale)

    ##########################################################

    class Square:
        def __init__ (self, side = 1):
            if side > 0:
                self._side = side

            else:
                print ("\n Invalid side length : side < 0 !\n")
                self._side = 1

        def _getSide (self):
            return trans (self._side)

        def _getPerimeter (self):
            return trans (self._side * 4)

        def _getSurface (self):
            return trans (self._side**2)

        def _getApothem (self):
            return trans (self._side / 2)

        def _getDiagonale (self):
            return trans (self._side * sqrt (2))

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
                self._side = sqrt (nSurface)

            else:
                print ("\n Invalid new surface : surface < 0 !\n")

        def _setApothem (self, nApothem):
            if nApothem > 0:
                self._side = nApothem * 2

            else:
                print ("\n Invalid new apothem : apothem < 0 !\n")

        def _setDiagonale (self, nDiagonale):
            if nDiagonale > 0:
                self._side = nDiagonale / sqrt (2)

            else:
                print ("\n Invalid new apothem : apothem < 0 !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('square {5} {0} {1} {2} {3} {4}'.format (self.side, self.perimeter, self.surface, self.apothem, self.diagonale, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._side *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._side /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Square (self._side * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Square (self._side / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Square:
                return self.side == n.side

            else:
                print ("\n Invalid operand type : they must be two squares !\n")

        def __ne__ (self, n):
            if type (n) is Square:
                return self.side != n.side

            else:
                print ("\n Invalid operand type : they must be two squares !\n")

        side = property (_getSide, _setSide)
        perimeter = property (_getPerimeter, _setPerimeter)
        surface = property (_getSurface, _setSurface)
        apothem = property (_getApothem, _setApothem)
        diagonale = property (_getDiagonale, _setDiagonale)

    ##########################################################

    class Ellipsoid:
        def __init__ (self, a = 1, b = 1, c = 1):
            if a > 0 and b > 0 and c > 0:
                self._a = a
                self._b = b
                self._c = c

            else:
                print ("\n Invalid measures : a, b and c must be greater than 0 !\n")

                self._a = 1
                self._b = 1
                self._c = 1

        def _getA (self):
            return trans (self._a)

        def _getB (self):
            return trans (self._b)

        def _getC (self):
            return trans (self._c)

        def _getVolume (self):
            return trans (4 * pi * self._a * self._b * self._c / 3)

        def _setA (self, nA):
            if nA > 0:
                self._a = nA

            else:
                BSOD (False)

        def _setB (self, nB):
            if nB > 0:
                self._b = nB

            else:
                BSOD (False)

        def _setC (self, nC):
            if nC > 0:
                self._c = nC

            else:
                print ("\n Invalid value : it must be greater than 0 !\n")

        def _setVolume (self, nVolume):
            print ("\n Impossible to change it !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named {} in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('ellipsoid {4} {0} {1} {2} {3}'.format (self.a, self.b, self.c, self.volume, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._a *= n
                    self._b *= n
                    self._c *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._a /= n
                    self._b /= n
                    self._c /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ellipsoid (self._a * n, self._b * n, self._c * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ellipsoid (self._a / n, self._b / n, self._c / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Ellipsoid:
                return self.a == n.a and self.b == n.b and self.c == n.c

            else:
                print ("\n Invalid operand type : they must be two ellipsoids !\n")

        def __ne__ (self, n):
            if type (n) is Ellipsoid:
                return self.a != n.a or self.b != n.b or self.c != n.c

            else:
                print ("\n Invalid operand type : they must be two ellipsoids !\n")

        a = property (_getA, _setA)
        b = property (_getB, _setB)
        c = property (_getC, _setC)
        volume = property (_getVolume, _setVolume)

    ##########################################################

    class Ellipse:
        def __init__ (self, a = 1, b = 1):
            if a > 0 and b > 0:
                self._a = a
                self._b = b

            elif a > 0:
                print ("\n Invalid value : a must be greater than 0 !\n")
                self._a = 1
                self._b = 1

            else:
                print ("\n Invalid value : b <= 0 !\n")
                self._a = 1
                self._b = 1

        def _getA (self):
            return trans (self._a)

        def _getB (self):
            return trans (self._b)

        def _getPerimeter (self):
            return trans (2 * pi * ((self._a * self._a + self._b * self._b) / 2)**0.5)

        def _getSurface (self):
            return trans (self._a * self._b * pi)

        def _setA (self, nA):
            if nA > 0:
                self._a = nA

            else:
                BSOD (False)

        def _setB (self, nB):
            if nB > 0:
                self._b = nB

            else:
                print ("\n Invalid new value : it must be greater than 0 !\n")

        def _setPerimeter (self, nPerimeter):
            print ("\n You are not allowed to do it !\n")

        def _setSurface (self, nSurface):
            print ("\n You are not allowed to do it !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named {} in this object !\n".format (name))

        def __repr__ (self):
            print ("\n Loading resources...")
            GraphicalDescription ('ellipse {4} {0} {1} {2} {3}'.format (self.a, self.b, self.perimeter, self.surface, _precision_))

            return "\n Done !\n"

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._a *= n
                    self._b *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._a /= n
                    self._b /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ellipse (self._a * n, self._b * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Ellipse (self._a / n, self._b / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Ellipse:
                return self.a == n.a and self.b == n.b

            else:
                print ("\n Invalid operand type : they must be two ellipses !\n")

        def __ne__ (self, n):
            if type (n) is Ellipse:
                return self.a != n.a or self.b != n.b

            else:
                print ("\n Invalid operand type : they must be two ellipses !\n")

        a = property (_getA, _setA)
        b = property (_getB, _setB)
        perimeter = property (_getPerimeter, _setPerimeter)
        surface = property (_getSurface, _setSurface)

    ##########################################################

    class Polygon:
        types = {3 : 'Triangle',
                 4 : 'Square',
                 5 : 'Pentagon',
                     6 : 'Hexagon',
                     7 : 'Heptagon',
                     8 : 'Octagon',
                     9 : 'Nonagon',
                     10 : 'Decagon',
                     12 : 'Duodecagon',
                     15 : 'Pentadecagon'}

        def __init__ (self, nSides = 3, side = 1):
            if nSides > 2 and side > 0:
                self._nSides = nSides
                self._side = side

            else:
                print ("\n Do not try to crash me !\n")
                self._nSides = 3
                self._side = 1

            try:
                self._type = Polygon.types[self._nSides]

            except KeyError:
                self._type = 'Polygon'

        def _getNSides (self):
            return trans (self._nSides)

        def _getSide (self):
            return trans (self._side)

        def _getApothem (self):
            return trans (self._side / (2 * tan (pi / self._nSides)))

        def _getPerimeter (self):
            return trans (self._nSides * self._side)

        def _getSurface (self):
            return trans ((self._nSides * self._side**2 / (2 * tan (pi / self._nSides))) / 2)

        def _setNSides (self, nNSides):
            if nNSides > 2:
                self._nSides = nNSides

                try:
                    self._type = Polygon.types[self._nSides]

                except KeyError:
                    self._type = 'Polygon'

            else:
                print ("\n Invalid new number of sides : it must be greater than 2 !\n")

        def _setSide (self, nSide):
            if nSide > 0:
                self._side = nSide

            else:
                print ("\n Invalid new side : side < 0 !\n")

        def _setApothem (self, nApothem):
            if nApothem > 0:
                self._side = round (nApothem * (2 * tan (pi / self._nSides)), 3)

            else:
                print ("\n Invalid new apothem : apothem < 0 !\n")

        def _setPerimeter (self, nPerimeter):
            if nPerimeter > 0:
                self._side = nPerimeter / self._nSides

            else:
                print ("\n Invalid new perimeter : perimeter < 0 !\n")

        def _setSurface (self, nSurface):
            if nSurface > 0:
                self._side = round (4 * nSurface / (self._nSides * self._side) * tan (pi / self._nSides), 3)

            else:
                print ("\n Invalid new surface : surface < 0 !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            return "\n Type : {0}\n Number of sides : {1}\n Side measure : {2}\n Apothem : {3}\n Perimeter :  {4}\n Surface :  {5}\n".format (self._type, self.nSides, self.side, self.apothem, self.perimeter, self.surface)

        def __imul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._side *= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __itruediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    self._side /= n

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

            return self

        def __mul__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Polygon (self._nSides, self._side * n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __truediv__ (self, n):
            if (type (n) is float) or (type (n) is int):
                if n > 0:
                    return Polygon (self._nSides, self._side / n)

                else:
                    print ("\n Invalid coefficient : it must be greater than 0 !\n")

            else:
                print ("\n Invalid operand type : it must be a scalar !\n")

        def __rmul__ (self, n):
            return self * n

        def __eq__ (self, n):
            if type (n) is Polygon:
                return self.nSides == n.nSides and self.side == n.side

            else:
                print ("\n Invalid operand type : they must be two {} !\n".format (self._type))

        def __ne__ (self, n):
            if type (n) is Polygon:
                return self.nSides != n.nSides or self.side != n.side

            else:
                print ("\n Invalid operand type : they must be two {} !\n".format (self._type))

        nSides = property (_getNSides, _setNSides)
        side = property (_getSide, _setSide)
        apothem = property (_getApothem, _setApothem)
        perimeter = property (_getPerimeter, _setPerimeter)
        surface = property (_getSurface, _setSurface)

    ##########################################################
    ######################   Others   ##############################
    ##########################################################

    class Vector:
        def __init__ (self, x = 0, y = 0):
            self._x = x
            self._y = y

        def _getX (self):
            return trans (self._x)

        def _getY (self):
            return trans (self._y)

        def _getLength (self):
            return trans ((self._x * self._x + self._y * self._y)**0.5)

        def _setX (self, nX):
            self._x = nX

        def _setY (self, nY):
            self._y = nY

        def _setLength (self, nLength):
            print ("\n Impossible to change it !\n")

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            return "\n ({0} ; {1})\n Length : {2}\n".format (self.x, self.y, (self.x * self.x + self.y * self.y)**0.5)

        def __add__ (self, n):
            if type (n) is Vector:
                return Vector (self._x + n.x, self._y + n.y)

            else:
                print ("\n Error : You can not do it !\n")

        def __sub__ (self, n):
            if type (n) is Vector:
                return Vector (self._x - n.x, self._y - n.y)

            else:
                print ("\n Error : You can not do it !\n")

        def __mul__ (self, n):
            if type (n) is Vector:
                return self._x * n.x + self._y * n.y

            elif (type (n) is int) or (type (n) is float):
                return Vector (self._x * n, self._y * n)

            else:
                print ("\n Error : Impossible to do it !\n")

        def __rmul__ (self, n):
            if type (n) is Vector:
                return self._x * n.x + self._y * n.y

            elif type (n) is int or type (n) is float:
                return Vector (self._x * n, self._y * n)

            else:
                print ("\n Error : You can not do that !\n")

        def __truediv__ (self, n):
            if type (n) is int or type (n) is float:
                return Vector (self._x / n, self._y / n)

            else:
                print ("\n Impossible to do it !\n")

        def __iadd__ (self, n):
            if type (n) is Vector:
                self._x += n.x
                self._y += n.y

            else:
                print ("\n Impossible to do it !\n")

            return self

        def __isub__ (self, n):
            if type (n) is Vector:
                self._x -= n.x
                self._y -= n.y

            else:
                print ("\n Impossible to do it !\n")

            return self

        def __imul__ (self, n):
            if type (n) is Vector:
                return self._x * n.x + self._y * n.y

            elif type (n) is int or type (n) is float:
                self._x *= n
                self._y *= n

            else:
                print ("\n Impossible to do it !\n")

            return self

        def __itruediv__ (self, n):
            if type (n) is int or type (n) is float:
                self._x /= n
                self._y /= n

            else:
                print ("\n You can not do it !\n")

            return self

        def __eq__ (self, n):
            return self.x == n.x and self.y == n.y

        def __ne__ (self, n):
            return self.x != n.x or self.y != n.y

        def __gt__ (self, n):
            return self.length > n.length

        def __lt__ (self, n):
            return self.length < n.length

        def __ge__ (self, n):
            return self.length >= n.length

        def __le__ (self, n):
            return self.length <= n.length

        length = property (_getLength, _setLength)
        x = property (_getX, _setX)
        y = property (_getY, _setY)

    ##########################################################

    class Coordinates:
        def __init__ (self, x, y):
            self._x = x
            self._y = y

        def _getX (self):
            return trans (self._x)

        def _getY (self):
            return trans (self._y)

        def _setX (self, nX):
            self._x = nX

        def _setY (self, nY):
            self._y = nY

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            return "({0} ; {1})".format (self.x, self.y)

        x = property (_getX, _setX)
        y = property (_getY, _setY)

    ##########################################################

    class Polynomial:
        def __init__ (self, a, b, c):
            if a == 0:
                print ("\n You can't give me 0 for 'a' : it's useless !\n")

            self._a = a
            self._b = b
            self._c = c

        def _getA (self):
            return trans (self._a)

        def _getB (self):
            return trans (self._b)

        def _getC (self):
            return trans (self._c)

        def _setA (self, nA):
            self._a = nA

        def _setB (self, nB):
            self._b = nB

        def _setC (self, nC):
            self._c = nC

        def evaluate (self, x):
            return trans (self._a * x * x + self._b * x + self._c)

        def _getRoot1 (self):
            if self.dsc > 0:
                return trans ((-self._b - sqrt (self._b * self._b - 4 * self._a * self._c)) / (2 * self._a))

            return trans ((-self._b - sqrt (self._b * self._b - 4 * self._a * self._c)) / (2 * self._a))

        def _getRoot2 (self):
            if self.dsc > 0:
                return trans ((-self._b + sqrt (self._b * self._b - 4 * self._a * self._c)) / (2 * self._a))

            return trans ((-self._b + sqrt (self._b * self._b - 4 * self._a * self._c)) / (2 * self._a))

        def _getSummit (self):
            return Coordinates (-self._b / (2 * self._a), self.evaluate (-self._b / (2 * self._a)))

        def _getDsc (self):
            return trans (self._b * self._b - 4 * self._a * self._c)

        def _getReducedDsc (self):
            return trans ((self._b * self._b / 4) - self._a * self._c)

        def __getattr__ (self, name):
            print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

        def __repr__ (self):
            if self.dsc == 0:
                return "\n Type : Polynomial (2nd degree)\n Expression : {0}x² + {1}x + {2}\n Discriminant : {3}\n Root :  {4}\n Summit :  {5}\n Derivee : {6}x + {1}\n".format (self.a, self.b, self.c, self.dsc, self.root1, self.summit, trans (self._a * 2))

            return "\n Type : Polynomial (2nd degree)\n Expression : {0}x² + {1}x + {2}\n Discriminant : {3}\n Reduced discriminant : {4}\n Root 1 :  {5}\n Root 2 :  {6}\n Summit :  {7}\n Derivee : {8}x + {1}\n".format (self.a, self.b, self.c, self.dsc, self.reducedDsc, self.root1, self.root2, self.summit, trans (self._a * 2))


        a = property (_getA, _setA)
        b = property (_getB, _setB)
        c = property (_getC, _setC)

        root1 = property (_getRoot1)
        root2 = property (_getRoot2)

        summit = property (_getSummit)
        dsc = property (_getDsc)
        reducedDsc = property (_getReducedDsc)

        ##########################################################

    print ("\n\n All modules are loaded !")

else:
    print ("\n\n You can load all modules when you start me, if you are interessed.\n Check the documentation if you want to see more.")

print ("\n")

system ("title Welcome to NyanMaths CL 2.6.2 !")


####################################################################### MAIN CODE


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
