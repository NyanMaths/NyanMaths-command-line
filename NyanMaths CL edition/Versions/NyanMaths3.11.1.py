# -*-coding:utf-8 -*


"""
NyanMaths CL version 3.xx (Main module) - Created by MemeTech INC

In the documentation, you can see all functionalities of this application.

Creator : NY4N_M4THS
"""


from os import system
from random import randint

from os.path import exists
from os import mkdir, remove
from shutil import rmtree
import glob

from time import sleep

from cmath import log

import re


if exists ('Startup configuration.pastouche'):
    _startupConf = open ('Startup configuration.pastouche').read ().split (' ')

else:
    _startupConf = ['1', '1', 'f0', '3.11.1', '1', '1']


system ("title NyanMaths  --  Loading...")

system ("cls")
system ("color {}".format (_startupConf[2]))


#######################  Constants  #####################


pi = 3.141592653589793238462
e = 2.71828182845904523536
phi = 1.618033988749894848204

h = 6.62607015e-34
G = 6.6743015e-11
E = 1.602176634e-19
A = 6.02214076e+23

i = 1j
j = 1j


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


#######################  Constants classes  #####################


def isReal (x):
    return type (x) is int or type (x) is float


class SpeedConstants:  # In m / s
    def __init__ (self):
        self._light = 299792458
        self._sound = 347


    def _getLight (self):
        return self._light

    def _getSound (self):
        return self._sound


    def _setSomething (self, nValue):
        print ("\n You aren't allowed to change a constant value !\n")


    def __getattr__ (self, name):
        print ("\n There's no constant named {} here ; maybe in another namespace (m or w) !\n".format (name))


    light = property (_getLight, _setSomething)
    sound = property (_getSound, _setSomething)


class GravitationalConstants:  # In m / s²
    def __init__ (self):
        self._moon = 1.622
        self._earth = 9.80665
        self._sun = 273.95


    def _getMoon (self):
        return self._moon

    def _getEarth (self):
        return self._earth

    def _getSun (self):
        return self._sun

    def _getMLG (self):
        BSOD (True)


    def _setSomething (self, nValue):
        print ("\n You aren't allowed to change a constant value !\n")


    def __getattr__ (self, name):
        print ("\n There's no constant named {} here ; maybe in another namespace (m or w) !\n".format (name))


    moon = property (_getMoon, _setSomething)
    earth = property (_getEarth, _setSomething)
    sun = property (_getSun, _setSomething)
    MLG = property (_getMLG, _setSomething)


class WeightConstants:  # In kg
    def __init__ (self):
        self._electron = 9.10938356e-31
        self._proton = 1.672649e-27
        self._neutron = 1.674927471e-27
        self._earth = 5.97237e+24
        self._moon = 7.342e+22
        self._sun = 1.9885e+30
        self._sgrA = 4.152 * 1.9885e+36


    def _getElectron (self):
        return self._electron

    def _getProton (self):
        return self._proton

    def _getNeutron (self):
        return self._neutron

    def _getMoon (self):
        return self._moon

    def _getEarth (self):
        return self._earth

    def _getSun (self):
        return self._sun

    def _getSgrA (self):
        return self._sgrA


    def _setSomething (self, nValue):
        print ("\n You aren't allowed to change a constant value !\n")


    def __getattr__ (self, name):
        print ("\n There's no constant named {} here ; maybe in another namespace (m or g) !\n".format (name))


    electron = property (_getElectron, _setSomething)
    proton = property (_getProton, _setSomething)
    neutron = property (_getNeutron, _setSomething)
    earth = property (_getEarth, _setSomething)
    moon = property (_getMoon, _setSomething)
    sun = property (_getSun, _setSomething)
    sgrA = property (_getSgrA, _setSomething)


class MeasuresConstants:  # In meters
    def __init__ (self):
        self._inch = 0.0254
        self._foot = 0.3048
        self._yard = 0.9144
        self._nauticalMile = 1852
        self._league = 4828.032
        self._ua = 149597870000
        self._ly = 9460730472580800
        self._parsec = 30856775670528308


    def _getInch (self):
        return self._inch

    def _getFoot (self):
        return self._foot

    def _getYard (self):
        return self._yard

    def _getNauticalMile (self):
        return self._nauticalMile

    def _getLeague (self):
        return self._league

    def _getUa (self):
        return self._ua

    def _getLy (self):
        return self._ly

    def _getParsec (self):
        return self._parsec


    def _setSomething (self, nValue):
        print ("\n You aren't allowed to change a constant value !\n")


    def __getattr__ (self, name):
        print ("\n There's no constant named {} here ; maybe in another namespace (g or w) !\n".format (name))


    inch = property (_getInch, _setSomething)
    foot = property (_getFoot, _setSomething)
    yard = property (_getYard, _setSomething)
    nauticalMile = property (_getNauticalMile, _setSomething)
    league = property (_getLeague, _setSomething)
    ua = property (_getUa, _setSomething)
    ly = property (_getLy, _setSomething)
    parsec = property (_getParsec, _setSomething)



g = GravitationalConstants ()
w = WeightConstants ()
m = MeasuresConstants ()
s = SpeedConstants ()


#######################  Other classes  #####################


class Coords:
    __type__ = "Coords"

    def __init__ (self, x, y):
        if isReal (x) and isReal (y):
            self._x = x
            self._y = y

        else:
            print ("\n Invalid coordinates, please stop making fun of me lil script kiddy !\n")
            self._x = 0
            self._y = 0


    def _getX (self):
        return self._x

    def _getY (self):
        return self._y


    def _setX (self, nX):
        if isReal (nX):
            self._x = nX

        else:
            print ("\n Please stop it now, slick character !\n")

    def _setY (self, nY):
        if isReal (nY):
            self._y = nY

        else:
            print ("\n Please stop it now, slick character !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        return "({0} ; {1})".format (trans (self.x), trans (self.y))


    def __eq__ (self, n):
        return self.x == n.x and self.y == n.y

    def __ne__ (self, n):
        return self.x != n.x or self.y != n.y


    x = property (_getX, _setX)
    y = property (_getY, _setY)


class Segment:
    __type__ = 'Segment'

    def __init__ (self, a, b, c = None, d = None):
        if (type (a) is Coords) and (type (b) is Coords) and (c is None) and (d is None):
            self._x1 = a.x
            self._y1 = a.y

            self._x2 = b.x
            self._y2 = b.y

        elif isReal (a) and isReal (b) and isReal (c) and isReal (d):
            self._x1 = a
            self._y1 = b

            self._x2 = c
            self._y2 = d

        else:
            print ("\n Invalid extremities : it must be coordinates !")
            self._x1 = 0
            self._y1 = 0

            self._x2 = 0
            self._y2 = 0


    def _getA (self):
        return Coords (self._x1, self._y1)

    def _getB (self):
        return Coords (self._x2, self._y2)

    def _getLength (self):
        return (((self._x2 - self._x1)**2 + (self._y2 - self._y1)**2)**0.5).real


    def _setA (self, n):
        if type (n) is not list and type (n) is Coords:
            self._x1 = n.x
            self._y1 = n.y

        elif isReal (n[0]) and isReal (n[1]):
            self._x1 = n[0]
            self._y1 = n[1]

        else:
            print ("\n Invalid new coordinates of a !\n")

    def _setB (self, n):
        if type (n) is not list and type (n) is Coords:
            self._x2 = n.x
            self._y2 = n.y

        elif isReal (n[0]) and isReal (n[1]):
            self._x2 = n[0]
            self._y2 = n[1]

        else:
            print ("\n Invalid new coordinates of b !\n")

    def _setLength (self, nLength):
        print ("\n Impossible to do this, I'm sorry !\n")


    def __repr__ (self):
        if self.a != self.b:
            return "\n Start point : {0}\n Finish point : {1}\n Length : {2}\n".format (self.a, self.b, trans (self.length))

        return "\n Only one point : {}\n".format (self.a)


    a = property (_getA, _setA)
    b = property (_getB, _setB)
    length = property (_getLength, _setLength)


def d (a, b):
    if type (a) is Coords and type (b) is Coords:
        return sqrt ((b.x - a.x)**2 + (b.y - a.y)**2)

    if a < b:
        return b - a

    return a - b


def middle (a, b = None):
    if type (a) is Segment and b is None:
        return Coords ((a._x1 + a._x2) / 2, (a._y1 + a._y2) / 2)

    elif type (a) is Coords and type (b) is Coords:
        return Coords ((a.x + b.x) / 2, (a.y + b.y) / 2)

    else:
        return (a + b) / 2


class Polynomial:
    def __init__ (self, a, b, c):
        if isReal (a) and isReal (b) and isReal (c):
            if not a:
                print ("\n You can't give me 0 for 'a' because it won't be second degree polynomial !\n")

            else:
                self._a = a
                self._b = b
                self._c = c

        else:
            print ("\n Invalid arguments : they must be real numbers (a != 0) !\n I'll initialize default values...\n")
            self._a = 1
            self._b = 0
            self._c = 0


    def _getA (self):
        return self._a

    def _getB (self):
        return self._b

    def _getC (self):
        return self._c

    def _getRoot1 (self):
        return (-self._b - (self._b * self._b - 4 * self._a * self._c)**0.5) / (2 * self._a)

    def _getRoot2 (self):
        return (-self._b + (self._b * self._b - 4 * self._a * self._c)**0.5) / (2 * self._a)

    def _getSummit (self):
        return Coords (-self._b / (2 * self._a), self.evaluate (-self._b / (2 * self._a)))

    def _getDsc (self):
        return self._b * self._b - 4 * self._a * self._c

    def _getReducedDsc (self):
        return (self._b * self._b / 4) - self._a * self._c


    def _setA (self, nA):
        if isReal (nA) and nA:
            self._a = nA

        else:
            print ("\n Please stop trying to make me crash !\n")

    def _setB (self, nB):
        if isReal (nB):
            self._b = nB

        else:
            print ("\n Invalid new value : it must be a real number !\n")

    def _setC (self, nC):
        if isReal (nC):
            self._c = nC

        else:
            print ("\n Invalid new value : it must be a real number !\n")


    def evaluate (self, x):
        return self._a * x * x + self._b * x + self._c


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        if not self.dsc:
            return "\n Type : Polynomial (2nd degree)\n Expression : {0}x² + {1}x + {2}\n Discriminant : {3}\n Root :  {4}\n Summit :  {5}\n Derivee : {6}x + {1}\n".format (trans (self.a), trans (self.b), trans (self.c), trans (self.dsc), trans (self.root1), self.summit, trans (self._a * 2))

        return "\n Type : Polynomial (2nd degree)\n Expression : {0}x² + {1}x + {2}\n Discriminant : {3}\n Reduced discriminant : {4}\n Root 1 :  {5}\n Root 2 :  {6}\n Summit :  {7}\n Derivee : {8}x + {1}\n".format (trans (self.a), trans (self.b), trans (self.c), trans (self.dsc), trans (self.reducedDsc), trans (self.root1), trans (self.root2), self.summit, trans (self._a * 2))


    a = property (_getA, _setA)
    b = property (_getB, _setB)
    c = property (_getC, _setC)

    root1 = property (_getRoot1)
    root2 = property (_getRoot2)

    summit = property (_getSummit)
    dsc = property (_getDsc)
    reducedDsc = property (_getReducedDsc)


#######################  Functions  #####################


def frequence (duration, t = 1):
    "Calculate the frequence of the phenomenol.\n If there's many periods in duration, you can specify how many in the second argument."

    return 1 / (duration / t)


def sRadius (x):
    "Compute the Schwarzschild radius of the object weighting x in meters"

    return (2 * 6.67408e-11 * x) / 299792458**2


def average (*params):
    "Returs the average of the values which you gave to the function"

    values = list (params)

    summ = 0
    i = len (values) - 1

    while i > -1:
        summ += values[i]
        i -= 1

    return summ / len (values)


def prime (x):
    "Says if x is a prime"

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
        sqrtx = int (x**0.5) + 1

        while div < sqrtx:
            if not x % div:
                return False

            div += 2

        return True


def divisible (n, x):
    "Says if x is a divider of n"

    if (type (n) is int) and (type (x) is int):
        return bool (not n % x)

    else:
        print ("\n Did you try to crash me ???\n Kill in 2 seconds...", end = '')
        sleep (2)
        BSOD (True)


def square (x):
    "Returns the square of x"

    return x * x


def cube (x):
    "Returns the cube of x"

    return x * x * x


def sqrt (x):
    "Returns the square root of x"

    return x**0.5


def power (x, y):
    "Returns x to the power y"

    return x**y


def exp (x):
    "Returns e to the power x"

    return e**x


def cuberoot (x):
    "Returns the cube root of x"

    return x**(1 / 3)


def root (x, y):
    "Returns x th root of y"

    return y**(1 / x)


def gcd (x, y):
    "Returns the greatest common divider between x and y"

    if x < 1 or y < 1 or (type (x) is not int) or (type (y) is not int):
        print ("\n Invalid argument : x and y must be positive integers !\n")

    else:
        if x == y:
            return x

        div = int (x / 2 + 1)

        if y > x:
            div = int (y / 2 + 1)

        while x % div or y % div:
            div -= 1

        return div


def fact (x):
    "Returns the factorial of x"

    if x < 0 or type (x) is not int:
        print ("\n Invalid parameter in fact (x) : x < 0 or x is decimal !\n")

    y = x
    r = 1

    while y > 1:
        r *= y
        y -= 1

    return r


def pythagore (a, b, c):
    "Returns the value of the side which you want to compute (put 0 insthead of it)\n or says if the triagle is right-angled if you give all values."

    if (a == 0) ^ (b == 0) ^ (c == 0):
        if not a:
            return (c * c - b * b)**0.5

        elif not b:
            return (c * c - a * a)**0.5

        else:
            return (a * a + b * b)**0.5

    if round (a * a + b * b, 10) == round (c * c, 10):
        print ("\n This triangle is right-angled !\n")

    else:
        print ("\n This triangle is not right-angled !\n")


def syracuse (x):
    "Displays the Collatz contiuation of x"

    if x < 1 or type (x) is not int:
        print ("\n Invalid argument : it must be a positive interger !\n")

    else:
        count = 0

        while x != 1:
            if x % 2:
                x = int (x * 3 + 1)

            else:
                x = int (x / 2)

            count += 1

            print ("\n", x, end = '')

        print ("\n ...\n\n The Collatz continuation of x is composed of {} numbers.\n".format (count))


def del_func ():
    name = input ("\n What is the name of the function which you want to delete ?  ")

    if exists ('User Functions/{}.mt_data'.format (name)):
        remove ('User Functions/{}.mt_data'.format (name))
        print ("\n Removed function !\n")

    else:
        print ("\n\n This function doesn't exist, sorry !\n")


def func ():
    "Allows you to create mathematical functions such as f(x) = x * x - 3\n You will be able to use it as others functions and delete it if you don't need it anymore."

    choice = input ("\n What do you want to do ?  Create a function (1) or delete a function (2) ?  ")

    if choice == '1':
        name = input ("\n Please give me the name of the function\n which you want create (only alphabetics characters and underscores _) :  ")

        if re.search ('^[a-zA-Z_]+$', name) is None:
            return "Please stop making fun of me..."

        expression = input ("\n Enter the expression (x is the parameter) :  ")
        doc = input ("\n Do you want to write a short desciption of your function ?\n Just press \"Enter\" if you're lazy...\n Description :  ")


        exec (name + " = lambda x : " + expression)
        print ("\n Let's test your function : {0} (3) = {1}".format (name, eval (name + "(3)")))


        funcfile = open ('User Functions/{}.mt_data'.format (name), 'w')
        funcfile.write ('def ' + name + ' (x):\n\t"Description : ' + doc + '\\n Expression : ' + expression + '"\n\treturn ' + expression)


        print ("\n\n Your function is saved !\n You have to restart the application to be able to call it.\n")

    elif choice == '2':
        del_func ()

    else:
        print ("\n I think it isn't too hard for you to input 1 or 2...\n")


def del_const ():
    name = input ("\n What is the name of the constant which you want to delete ?  ")

    if not exists ('User constants/{}.mt_data'.format (name)):
        print ("\n\n This const doesn't exist, sorry !")
        raise RuntimeError

    remove ('User constants/{}.mt_data'.format (name))
    print ("\n\n Removed constant !\n\n")


def const ():
    "You can create and edit you own consts with this little tool ; launch it to get more informations..."

    choice = input ("\n\n Do you want to create/edit a constant (1) or delete a constant (2) ?  ")

    if choice == '1':
        name = input ("\n What is the name of the constant which you want to create or edit (Only alphabetics characters and underscores _) ?  ")

        if re.search ('^[a-zA-Z_]+$', name) is None:
            print ("\n I said ONLY alphabetics characters and underscores...")
            raise RuntimeError

        value = input ("\n What is the value of your constant ?\n You can use functions or other consts :  ")

        with open ('User constants/{}.mt_data'.format (name), 'w') as constfile:
            constfile.write ('{}'.format (eval (value)))


        print ("\n\n Your constant is defined !\n You can delete it if you don't need it anymore.\n\n")


    elif choice == '2':
        del_const ()

    else:
        print ("\n Are you serious ?...\n\n")


def ln (x):
    "Returns the natural logarithm of x"

    return log (x)


def cis (x):
    "Returns e^(jx)"

    return e**(1j * x)

def sin (x):
    "Returns the sine of x (by default, x is in radians)"

    if _unit_ == 'rad':
        return (e**(x * 1j) - e**(-x * 1j)) / 2j

    return (e**(x / 180 * pi * 1j) - e**(-x / 180 * pi * 1j)) / 2j


def cos (x):
    "Returns the cosine of x (by default, x is in radians)"

    if _unit_ == 'rad':
        return (e**(x * 1j) + e**(-x * 1j)) / 2

    return (e**(x / 180 * pi * 1j) + e**(-x / 180 * pi * 1j)) / 2


def tan (x):
    "Returns the tangent of x (by default, x is in radians)"

    return sin (x) / cos (x)


def cot (x):
    "Returns the cotangent of x (by default, x is in radians)"

    return cos (x) / sin (x)


def sec (x):
    "Returns the secant of x (by default, x is in radians)"

    return 1 / cos (x)


def csc (x):
    "Returns the cosecant of x (by default, x is in radians)"

    return 1 / sin (x)


def sinh (x):
    "Returns the hyperbolic sine of x (by default, x is in radians)"

    if _unit_ == 'rad':
        return (e**(x) - e**(-x)) / 2

    return (e**(x / 180 * pi) - e**(-x / 180 * pi)) / 2


def cosh (x):
    "Returns the hyperbolic cosine of x (by default, x is in radians)"

    if _unit_ == 'rad':
        return (e**(x) + e**(-x)) / 2

    return (e**(x / 180 * pi) + e**(-x / 180 * pi)) / 2


def tanh (x):
    "Returns the hyperbolic tangent of x (by default, x is in radians, type setUnit (drg) to switch it)"

    return sinh (x) / cosh (x)


def coth (x):
    "Returns the hyperbolic cotangent of x (by default, x is in radians, type setUnit (drg) to switch it)"

    return cosh (x) / sinh (x)


def sech (x):
    "Returns the hyperbolic secant of x (by default, x is in radians, type setUnit (drg) to switch it)"

    return 1 / cosh (x)


def csch (x):
    "Returns the hyperbolic cosecant of x (by default, x is in radians, type setUnit (drg) to switch it)"

    return 1 / sinh (x)


def asin (x):
    "Returns the arcsine of x in radians by default"

    if _unit_ == 'rad':
        return -(1j * log (1j * x + sqrt (1 - x * x)))

    return -1j * log (1j * x + (1 - x * x)**0.5) * 180 / pi


def acos (x):
    "Returns the arccosine of x in radians by default"

    if _unit_ == 'rad':
        return pi / 2 - asin (x)

    return -1j * log (x + 1j * (1 - x * x)**0.5) * 180 / pi


def atan (x):
    "Returns the arctangent of x in radians by default"

    if _unit_ == 'rad':
        return (log (1 + 1j * x) - log (1 - 1j * x)) / 2j

    return (log (1 + 1j * x) - log (1 - 1j * x)) / 2j * 180 / pi


def acot (x):
    "Returns the arccotengent of x in radians by default"

    return atan (1 / x)


def asec (x):
    "Returns the arcsecant of x in radians by default"

    return acos (1 / x)


def acsc (x):
    "Returns the arccosecant of x in radians by default"

    return asin (1 / x)


def asinh (x):
    "Returns the hyperbolic arcsine of x in radians by default"

    if _unit_ == 'rad':
        return log (x + (x * x + 1)**0.5)

    return log (x + (x * x + 1)**0.5) * 180 / pi


def acosh (x):
    "Returns the hyperbolic arccosine of x in radians by default"

    if _unit_ == 'rad':
        return log (x + (x * x - 1)**0.5)

    return log (x + (x * x - 1)**0.5) * 180 / pi


def atanh (x):
    "Returns the hyperbolic arctangent of x in radians by default"

    if _unit_ == 'rad':
        return 0.5 * log ((1 + x) / (1 - x))

    return log ((1 + x) / (1 - x)) * 90 / pi


def acoth (x):
    "Returns the hyperbolic arccotengent of x in radians by default"

    if _unit_ == 'rad':
        return 0.5 * log ((x + 1) / (x - 1))

    return log ((x + 1) / (x - 1)) * 90 / pi


def asech (x):
    "Returns the hyperbolic arcsecant of x in radians by default"

    if _unit_ == 'rad':
        return log ((1 + (1 - x * x)**0.5) / x)

    return log ((1 + (1 - x * x)**0.5) / x) * 180 / pi


def acsch (x):
    "Returns the hyperbolic arccosecant of x in radians by default"

    if _unit_ == 'rad':
        return log (1 / x + (x**(-2) + 1)**0.5)

    return log (1 / x + (x**(-2) + 1)**0.5) * 180 / pi


#######################  Others  #####################


def _strType (x):
    if type (x) is int or type (x) is float or type (x) is complex:
        return 'number'

    elif type (x) is str:
        return 'string'

    if x.__doc__ is not None:
        return 'function'

    return x.__type__


def degrees (x):
    "Converts x to degrees"

    return x * 180 / pi


def radians (x):
    "Convert x to radians"

    return x / 180 * pi


def setPrecision (x):
    "Changes the display precision (from 0 to 12 decimals, 9 recommanded)"

    if x > -1 and x < 13:
        _precision_ = x
        open ('Versions/Conf.pastouche', 'w').write ('{0} {1}'.format (x, _unit_))

        print ("\n Precision changed ! Restart needed to apply.\n")

    else:
        print ("\n You had to input a number between 0 and 12 !\n ")


def setUnit (x):
    "Change the default angles unit (degrees or radians)"

    if x == 'drg' or x == 'rad':
        _unit_ = x
        open ('Versions/Conf.pastouche', 'w').write ('{0} {1}'.format (_precision_, x))

        print ("\n Unit changed ! Restart needed to apply.\n")

    else:
        print ("\n You had to input drg or rad !\n ")


def trans (x):
    if type (x) in [complex, float, int]:
        if type (x) is complex:
            if not x.real and not x.imag:
                return 0

            elif not x.real:
                return trans (x.imag) * 1j

            elif not x.imag:
                return trans (x.real)

            else:
                return complex (round (x.real, _precision_), round (x.imag, _precision_))

        if not abs (x) - abs (int (x)):
            return int (x)

        x = round (x, _precision_)

        if not abs (x) - abs (int (x)):
            return int (x)

    return x


def BSOD (ex = False):
    system ("BSOD_MEME.pyw")

    if ex:
        return 'quit'


def easter_egg (password):
    "Type this command to know the truth about life, universe and everything..."

    if password == open ('datHelp', 'r').read ():
        if exists ('_datHelp_'):
            print ("\n\n")
            system ('color 0a')
            
            message = open ('_datHelp_', 'r').read ().split ('\n')
            
            for line in message:
                for char in line:
                    print (char, end = '', flush = True)
                    sleep (randint (3, 30) / 100)
    
    
                sleep (1)
                print ("\n")
    
            sleep (2)
    
            BSOD (True)
            
        else:
            print ("\n Ooooooooooooooops...\n I miss one of my data files, sorry !\n\n")

    else:
        print ("\n Get out of my way, nasty character !\n\n")


def tools ():
    print ("\n Tools which you can use in this version :\n  primes\n  dividers\n  UIR\n  PUI\n  VDT\n  MVD\n  temperature\n")


def operations ():
    print ( "\n + : Addition"
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
              "\n\n For example :\n\n>>> 3 + 3 * 5\n18\n\n>>> 3 == sqrt (square (3))\nTrue\n\n" )


def displayHelp ():
    if exists ("Versions/help{}.pastouche".format (_startupConf[3])):
        helpText = open ("Versions/help{}.pastouche".format (_startupConf[3]), 'r').read ().split ('&')

        if int (_startupConf[1]):
            print (helpText[0])

        if int (_startupConf[4]):
            print (helpText[1])

    else:
        print ("\n My help file's missing in my folder : may I get it back ?\n If you have not touched anything, please reinstall this application to fix this issue !\n")


def doc (x):
    "Slick character...  :-D"

    typeOfX = _strType (x)

    if typeOfX == 'number':
        print ("\n It's just a number !\n It may be an integer, a float or a complex.\n")

    elif typeOfX == 'string':
        print ("\n You already know what's a string, slick character...\n")

    elif typeOfX == 'function':
        if x.__doc__ != None:
            print ("\n " + x.__doc__ + "\n")

        else:
            print ("\n There's no documentation for this function yet, sorry !\n Please wait coming updates...\n")

    else:
        system ("Documentation.pyw {}".format (_strType (x)))


def reset ():
    code = input ("\n Do you really want to remove all your settings and data ?\n Input 6942 if you really want to do this :  ")

    if code == '6942':
        rmtree ('User data')
        rmtree ('User Functions')
        rmtree ('User constants')
        rmtree ('Versions/Modules/__pycache__')
        rmtree ('Versions/Tools/__pycache__')

        mkdir ('User data')
        mkdir ('User Functions')
        mkdir ('User constants')

        open ('Versions/Conf.pastouche', 'w').write ('9 rad')

        print ("\n Settings reseted !\n Restart needed to apply.\n")

    else:
        print ("\n Alright, I won't do this !\n")


##########################################################
##########################    Loading    #########################
##########################################################


if int (_startupConf[1]) or int (_startupConf[4]):
    displayHelp ()

print ("\n Welcome to NyanMaths Command Line edition !\n If you don't know how to use it : RTFM !\n\n Unit : {0}\n Floating point precision : {1}".format (_unit_, _precision_))

if int (_startupConf[5]) == 1:
    from Tools.v3_11_1 import *   # Loads mini-apps

else:
    print ("\n\n You can load a few mathematical tools, type tools() for more informations...\n")


if int (_startupConf[0]):
    from Modules.v3_11_1 import *   # Loads objects module (Ball, Cube, Cone...)

else:
    print ("\n\n You can load objects at startup, if you are interested.\n Look into the documentation if you want to see more.\n")


constsList = ['pi', 'e', 'phi', 'h', 'G', 'E', 'A', 's', 'g', 'm', 'w', 'i', 'j', 'drg', 'rad', '_precision_', '_unit_', 'constsList']


############################################


for filename in glob.glob ('User Functions/*.mt_data'):

    end = len (filename) - 1
    while filename[end] != '.':
        end -= 1

    begin = end
    while not filename[begin - 1] in ['/', '\\']:
        begin -= 1

    print ("\n Importing {}(x)...".format (filename[begin:end]))
    exec (open (filename, 'r').read ())


for filename in glob.glob ('User constants/*.mt_data'):

    end = len (filename) - 1
    while filename[end] != '.':
        end -= 1

    begin = end
    while not filename[begin - 1] in ['/', '\\']:
        begin -= 1

    print ("\n Importing {}...".format (filename[begin:end]))

    exec (filename[begin:end] + '=' + open (filename, 'r').read ())
    constsList.append (filename[begin:end])


############################################


print ("\n\n You can check on our website for updates :\n https://memetech-inc.weebly.com/nyanmaths-cl \n\n\n")
system ("title Welcome to NyanMaths CL {} !".format (_startupConf[3]))


################################   Main code ##################################


cmd = ''
last = ''

while True:  # Main loop
    cmd = input (" > What can I do ?  ")
    cmd = re.sub (' ', '', cmd)

    _r = None  # The return-value of user's commands

    if cmd == 'last':
        cmd = str (last)

    if cmd in ['quit', 'exit']:
        break

    if cmd != '':  # If the user entered something
        try:
            if (('=' in cmd) and (not '==' in cmd)):  # If the user want to create an object

                for const in constsList:   # Make sure the user isn't trying to edit a constant
                    if re.search ('^' + const + '=', cmd):
                        print ("\n\n You aren't allowed to edit constant values, lil script kiddy !\n\n")
                        raise RuntimeError

                exec (cmd)
                print ("\n", end = '')

            else:
                _r = eval (cmd)   # If the user want the app to compute something

            if _r is not None:
                if (type (_r) is complex) or (type (_r) is int) or (type (_r) is float):   # If there's a result to display (number)
                    print ("\n", trans (_r), "\n")

                else:   # If the result is a string or a boolean
                    if _r == 'quit':
                        break

                    print ("\n ", _r, "\n")

            last = str (cmd)


        # Exceptions management

        except TypeError:
            print ("\n Invalid operand type !\n")

        except NameError:
            print ("\n This variable or type doesn't exist !\n Don't forget to capitalize object types !\n")

        except ZeroDivisionError:
            print ("\n Newbie's error #0 : division by zero !\n")

        except ValueError:
            print ("\n You gave an invalid value somewhere !\n")

        except KeyboardInterrupt:
            break

        except RuntimeError:  # If the exception was already managed
            pass

        except:
            print ("\n An unknown error has occurred, sorry !\n")
