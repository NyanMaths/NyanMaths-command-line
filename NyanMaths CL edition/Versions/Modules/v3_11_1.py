# -*-coding:Latin-1 -*


###################  Initialization  ###################


from os import system
from os.path import exists
from cmath import tan as stan
from cmath import sin as ssin


_decimals_ = 3
if exists ('Versions/Conf.pastouche'):
    _decimals_ = int (open ('Versions/Conf.pastouche').read ().split (' ')[0])


pi = 3.141592653589793238462


###################  Functions  ###################


def isOK (x, MIN = 0):
    return (type (x) is int or type (x) is float or (type (x) is complex and x.imag == 0)) and x > MIN


def isIntegral (x, MIN = 0):
    return not (x - int (x)) and x > MIN


def formated (x):
    if type (x) in [complex, float, int]:
        if type (x) is complex:
            if not x.real and not x.imag:
                return 0

            elif not x.real:
                return formated (x.imag) * 1j

            elif not x.imag:
                return formated (x.real)

            else:
                return complex (round (x.real, _decimals_), round (x.imag, _decimals_))

        if not abs (x) - abs (int (x)):
            return int (x)

        x = round (x, _decimals_)

        if not abs (x) - abs (int (x)):
            return int (x)

    return x


def BSOD (ex = False):
    system ("BSOD_MEME.pyw")

    if ex:
        exit (0)


###################  Classes  ###################


class Ball:
    __type__ = "Ball"
    
    def __init__ (self, radius = 1):
        if isOK (radius):
            self._radius = radius

        else:
            print ("\n Invalid radius : it must be a positive non-zero real number !\n Initialization of default value...\n Done\n")
            self._radius = 1


    def _getRadius (self):
        return self._radius

    def _getDiameter (self):
        return self._radius * 2

    def _getVolume (self):
        return self._radius**3 * (4 / 3) * pi

    def _getSurface (self):
        return self._radius**2 * 4 * pi


    def _setRadius (self, nRadius):
        if isOK (nRadius):
            self._radius = nRadius

        else:
            print ("\n Invalid new radius : it must be a positive non-zero real number !\n")

    def _setDiameter (self, nDiameter):
        if isOK (nDiameter):
            self._radius = nDiameter / 2

        else:
            print ("\n Invalid new diameter : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        if isOK (nVolume):
            self._radius = (nVolume / pi * 0.75)**(1 / 3)

        else:
            BSOD ()

    def _setSurface (self, nSurface):
        if isOK (nSurface):
            self._radius = (nSurface / 4 / pi)**0.5

        else:
            print ("\n Invalid new surface : it must be a positive non-zero real number !\n")


    def __getattr__ (self, name):
        print ("\n There's no attribute named \"{}\" in this object, sorry !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw ball {4} {0} {1} {2} {3}'.format (self.radius, self.diameter, self.volume, self.surface, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._radius *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._radius /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Ball (self._radius * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n

    def __truediv__ (self, n):
        if isOK (n):
            return Ball (self._radius / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n

    def __eq__ (self, n):
        if type (n) is Ball:
            return self.radius == n.radius

        print ("\n Invalid operands : they must be two balls !\n")

    def __ne__ (self, n):
        if type (n) is Ball:
            return self.radius != n.radius

        print ("\n Invalid operands : they must be two balls !\n")


    radius = property (_getRadius, _setRadius)

    diameter = property (_getDiameter, _setDiameter)
    volume = property (_getVolume, _setVolume)
    surface = property (_getSurface, _setSurface)


##########################################################


class Cone:
    __type__ = "Cone"
    
    def __init__ (self, radius, height):
        if isOK (radius) and isOK (height):
            self._radius = radius
            self._height = height
            
        else:
            print ("\n Invalid arguments : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._height = 1
            self._radius = 1


    def _getRadius (self):
        return self._radius

    def _getDiameter (self):
        return self._radius * 2
    
    def _getHeight (self):
        return self._height

    def _getBaseSurface (self):
        return self._radius**2 * pi

    def _getVolume (self):
        return self._radius**2 * pi * self._height * (1 / 3)

    def _getLateralSurface (self):
        return self._radius * pi * (self._height**2 + self._radius**2)**0.5


    def _setRadius (self, nRadius):
        if isOK (nRadius):
            self._radius = nRadius

        else:
            print ("\n Invalid new base radius : it must be a positive non-zero real number !\n")

    def _setDiameter (self, nDiameter):
        if isOK (nDiameter):
            self._radius = nDiameter / 2

        else:
            print ("\n Invalid new base diameter : it must be a positive non-zero real number !\n")

    def _setHeight (self, nHeight):
        if isOK (nHeight):
            self._height = nHeight

        else:
            print ("\n Invalid new height : it must be a positive non-zero real number !\n")

    def _setBaseSurface (self, nBaseSurface):
        if isOK (nBaseSurface):
            self._radius = (nBaseSurface / pi)**0.5

        else:
            print ("\n Invalid new base surface : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")

    def _setLateralSurface (self, nLateralSurface):
        print ("\n You aren't allowed to do this, sorry !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw cone {6} {0} {1} {2} {3} {4} {5}'.format (self.radius, self.diameter, self.height, self.baseSurface, self.volume, self.lateralSurface, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._radius *= n
            self._height *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._radius /= n
            self._height /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Cone (self._radius * n, self._height * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Cone (self._radius / n, self._height / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Cone:
            return self.radius == n.radius and self.height == n.height

        print ("\n Invalid operands : they must be two cones !\n")

    def __ne__ (self, n):
        if type (n) is Cone:
            return self.radius != n.radius or self.height != n.height

        print ("\n Invalid operands : they must be two cones !\n")


    radius = property (_getRadius, _setRadius)
    height = property (_getHeight, _setHeight)

    diameter = property (_getDiameter, _setDiameter)
    baseSurface = property (_getBaseSurface, _setBaseSurface)
    volume = property (_getVolume, _setVolume)
    lateralSurface = property (_getLateralSurface, _setLateralSurface)


##########################################################


class Cube:
    __type__ = "Cube"
    
    def __init__ (self, edge):
        if isOK (edge):
            self._edge = edge

        else:
            print ("\n Invalid edge : it must be a positive non-zero real number !\n Initialization of default values...\n Done\n")
            self._edge = 1


    def _getEdge (self):
        return self._edge

    def _getVolume (self):
        return self._edge**3

    def _getSurface (self):
        return self._edge**2 * 6

    def _getDiagonale (self):
        return self._edge * 1.732050807568878


    def _setEdge (self, nEdge):
        if isOK (nEdge):
            self._edge = nEdge

        else:
            print ("\n Invalid new edge : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        if isOK (nVolume):
            self._edge = nVolume**(1 / 3)

        else:
            print ("\n Invalid new volume : it must be a positive non-zero real number !\n")

    def _setSurface (self, nSurface):
        if isOK (nSurface):
            self._edge = (nSurface / 6)**0.5

        else:
            print ("\n Invalid new surface : it must be a positive non-zero real number !\n")

    def _setDiagonale (self, nDiadonale):
        if isOK (nDiagonale):
            self._edge = nDiadonale / 1.732050807568878

        else:
            print ("\n Invalid new diagonale : it must be a positive non-zero real number !\n")


    def __getattr__ (self, name):
        print ("\n I'm so sorry, but there's no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw cube {4} {0} {1} {2} {3}'.format (self.edge, self.volume, self.surface, self.diagonale, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._edge *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._edge /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Cube (self._edge * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Cube (self._edge / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Cube:
            return self.edge == n.edge

        print ("\n Invalid operands : they must be two cubes !\n")

    def __ne__ (self, n):
        if type (n) is Cube:
            return self.edge != n.edge

        print ("\n Invalid operands : they must be two cubes !\n")


    edge = property (_getEdge, _setEdge)

    volume = property (_getVolume, _setVolume)
    surface = property (_getSurface, _setSurface)
    diagonale = property (_getDiagonale, _setDiagonale)


###############################################################################


class Cuboid:
    __type__ = "Cuboid"
    
    def __init__ (self, length, width = None, height = None):
        if width is None:
            width = length
            height = length

        if isOK (length) and isOK (width) and isOK (height):
            self._length = length
            self._width = width
            self._height = height

        else:
            print ("\n Invalid values : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._length = 1
            self._width = 1
            self._height = 1


    def _getLength (self):
        return self._length

    def _getWidth (self):
        return self._width

    def _getHeight (self):
        return self._height

    def _getEdge (self):
        if self._length == self._width == self._height:
            return self._length

        print ("\n You can't access to this property because length must be equals to width and height !\n")
        raise RuntimeError

    def _getVolume (self):
        return self._length * self._width * self._height

    def _getSurface (self):
        return 2 * (self._length * self._width + self._length * self._height + self._width * self._height)

    def _getDiagonale (self):
        return (self._length * self._length + self._width * self._width + self._height * self._height)**0.5


    def _setLength (self, nLength):
        if isOK (nLength):
            self._length = nLength

        else:
            print ("\n Invalid new length : it must be a positive non-zero real number !\n")

    def _setWidth (self, nWidth):
        if isOK (nWidth):
            self._width = nWidth

        else:
            print ("\n Invalid new width : it must be a positive non-zero real number !\n")

    def _setHeight (self, nHeight):
        if isOK (nHeight):
            self._height = nHeight

        else:
            print ("\n Invalid new height : it must be a positive non-zero real number !\n")

    def _setEdge (self, nEdge):
        if isOK (nEdge):
            self._length = nEdge
            self._width = nEdge
            self._height = nEdge

        else:
            print ("\n Invalid new edge : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")

    def _setSurface (self, nSurface):
        print ("\n Impossible to change it !\n")

    def _setDiagonale (self, nDiagonale):
        print ("\n Impossible to change it !\n Kill in 2 seconds...")
        sleep (2)
        BSOD ()


    def __getattr__ (self, name):
        print ("\nI'm sorry, there's no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw cuboid {6} {0} {1} {2} {3} {4} {5}'.format (self.length, self.width, self.height, self.volume, self.surface, self.diagonale, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._length *= n
            self._width *= n
            self._height *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._length /= n
            self._width /= n
            self._height /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Cuboid (self._length * n, self._width * n, self._height * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Cuboid (self._length / n, self._width / n, self._height / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Cuboid:
            return self.length == n.length and self.width == n.width and self.height == n.height

        print ("\n Invalid operands : they must be two cuboids !\n")

    def __ne__ (self, n):
        if type (n) is Cuboid:
            return self.length != n.length or self.width != n.width or self.height != n.height

        print ("\n Invalid operands : they must be two cuboids !\n")


    length = property (_getLength, _setLength)
    width = property (_getWidth, _setWidth)
    height = property (_getHeight, _setHeight)

    edge = property (_getEdge, _setEdge)

    volume = property (_getVolume, _setVolume)
    surface = property (_getSurface, _setSurface)
    diagonale = property (_getDiagonale, _setDiagonale)


##########################################################


class Cylinder:
    __type__ = "Cylinder"
    
    def __init__ (self, radius, height):
        if isOK (radius) and isOK (height):
            self._radius = radius
            self._height = height

        else:
            print ("\n Invalid radius : it must be a positive non-zero real number !\n Initialization of default value...\n Done\n")
            self._radius = 1
            self._height = 1


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
        if isOK (nRadius):
            self._radius = nRadius

        else:
            print ("\n Invalid new radius : it must be a positive non-zero real number !\n")

    def _setDiameter (self, nDiameter):
        if isOK (nDiameter):
            self._radius = nDiameter / 2

        else:
            print ("\n Invalid new diameter : it must be a positive non-zero real number !\n")

    def _setHeight (self, nHeight):
        if isOK (nHeight):
            self._height = nHeight

        else:
            print ("\n Invalid new height : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")

    def _setBaseSurface (self, nBaseSurface):
        if isOK (nBaseSurface):
            self._radius = (nBaseSurface / pi)**0.5

        else:
            print ("\n Invalid new base surface : it must be a positive non-zero real number !\n")

    def _setSurface (self, nSurface):
        print ("\n Impossible to change it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw cylinder {6} {0} {1} {2} {3} {4} {5}'.format (self.radius, self.diameter, self.height, self.baseSurface, self.volume, self.surface, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._radius *= n
            self._height *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._radius /= n
            self._height /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Cylinder (self._radius * n, self._height * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Cylinder (self._radius / n, self._height / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Cylinder:
            return self.radius == n.radius and self.height == n.height

        print ("\n Invalid operands : they must be two cylinders !\n")

    def __ne__ (self, n):
        if type (n) is Cylinder:
            return self.radius != n.radius or self.height != n.height

        print ("\n Invalid operands : they must be two cylinders !\n")


    radius = property (_getRadius, _setRadius)
    height = property (_getHeight, _setHeight)
    
    diameter = property (_getDiameter, _setDiameter)
    baseSurface = property (_getBaseSurface, _setBaseSurface)
    volume = property (_getVolume, _setVolume)
    surface = property (_getSurface, _setSurface)


##########################################################


class Disk:
    __type__ = "Disk"
    
    def __init__ (self, radius):
        if isOK (radius):
            self._radius = radius

        else:
            print ("\n Invalid radius : it must be a positive non-zero real number !\n Initialization of default value...\n Done\n")
            self._radius = 1


    def _getRadius (self):
        return self._radius

    def _getDiameter (self):
        return self._radius * 2

    def _getPerimeter (self):
        return self._radius * 2 * pi

    def _getSurface (self):
        return self._radius**2 * pi


    def _setRadius (self, nRadius):
        if isOK (nRadius):
            self._radius = nRadius

        else:
            print ("\n Invalid new radius : it must be a positive non-zero real number !\n")

    def _setDiameter (self, nDiameter):
        if isOK (nDiameter):
            self._radius = nDiameter / 2

        else:
            print ("\n Invalid new diameter : it must be a positive non-zero real number !\n")

    def _setPerimeter (self, nPerimeter):
        if isOK (nPerimeter):
            self._radius = nPerimeter / 2 / pi

        else:
            print ("\n Invalid new perimeter : it must be a positive non-zero real number !\n")

    def _setSurface (self, nSurface):
        if isOK (nSurface):
            self._radius = (nSurface / pi)**0.5

        else:
            print ("\n Invalid new surface : it must be a positive non-zero real number !\n")


    def __getattr__ (self, name):
        print ("\n There's no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw disk {4} {0} {1} {2} {3}'.format (self.radius, self.diameter, self.perimeter, self.surface, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._radius *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._radius /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Disk (self._radius * n)

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Disk (self._radius / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n

    def __eq__ (self, n):
        if type (n) is Disk:
            return self.radius == n.radius

        print ("\n Invalid operands : they must be two disks !\n")

    def __ne__ (self, n):
        if type (n) is Disk:
            return self.radius != n.radius

        print ("\n Invalid operands : they must be two disks !\n")


    radius = property (_getRadius, _setRadius)

    diameter = property (_getDiameter, _setDiameter)
    perimeter = property (_getPerimeter, _setPerimeter)
    surface = property (_getSurface, _setSurface)


##########################################################


class Prism:
    __type__ = "Prism"
    
    def __init__ (self, baseSurface, height):
        if isOK (baseSurface) and isOK (height):
            self._baseSurface = baseSurface
            self._height = height
            
        else:
            print ("\n Invalid measures : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._baseSurface = 1
            self._height = 1


    def _getBaseSurface (self):
        return self._baseSurface

    def _getHeight (self):
        return self._height

    def _getVolume (self):
        return self._baseSurface * self._height


    def _setBaseSurface (self, nBaseSurface):
        if isOK (nBaseSurface):
            self._baseSurface = nBaseSurface

        else:
            print ("\n Invalid new base surface : it must be a positive non-zero real number !\n")

    def _setHeight (self, nHeight):
        if isOK (nHeight):
            self._height = nHeight

        else:
            print ("\n Invalid new height : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw prism {3} {0} {1} {2}'.format (self.baseSurface, self.height, self.volume, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._baseSurface *= n * n
            self._height *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._baseSurface /= n * n
            self._height /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Prism (self._baseSurface * n * n, self._height * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Prism (self._radius / (n * n), self._height / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    baseSurface = property (_getBaseSurface, _setBaseSurface)
    height = property (_getHeight, _setHeight)

    volume = property (_getVolume, _setVolume)


##########################################################


class Pyramid:
    __type__ = "Pyramid"
    
    def __init__ (self, baseSurface, height):
        if isOK (baseSurface) and isOK (height):
            self._baseSurface = baseSurface
            self._height = height

        else:
            print ("\n Invalid arguments : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._baseSurface = 1
            self._height = 1


    def _getBaseSurface (self):
        return self._baseSurface

    def _getHeight (self):
        return self._height

    def _getVolume (self):
        return self._baseSurface * self._height / 3


    def _setBaseSurface (self, nBaseSurface):
        if isOK (nBaseSurface):
            self._baseSurface = nBaseSurface

        else:
            print ("\n Invalid new base surface : it must be a positive non-zero real number !\n")

    def _setHeight (self, nHeight):
        if isOK (nHeight):
            self._height = nHeight

        else:
            print ("\n Invalid new height : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw pyramid {3} {0} {1} {2}'.format (self.baseSurface, self.height, self.volume, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._baseSurface *= n * n
            self._height *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._baseSurface /= n * n
            self._height /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Pyramid (self._baseSurface * n * n, self._height * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Pyramid (self._baseSurface / (n * n), self._height / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    baseSurface = property (_getBaseSurface, _setBaseSurface)
    height = property (_getHeight, _setHeight)

    volume = property (_getVolume, _setVolume)


##########################################################


class Rectangle:
    __type__ = "Rectangle"

    def __init__ (self, length, width = None):
        if width is None:
            width = length

        if isOK (length) and isOK (width):
            if length > width:
                self._length = length
                self._width = width

            else:
                self._length = width
                self._width = length

                print ("\n Length must be greater than width, I inverted them !\n")

        else:
            print ("\n Invalid arguments : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._length = 1
            self._width = 1


    def _getLength (self):
        return self._length

    def _getWidth (self):
        return self._width

    def _getSide (self):
        if self._length == self._width:
            return self._length

        print ("\n You can't access to this property because length != width\n")
        raise RuntimeError

    def _getPerimeter (self):
        return 2 * (self._length + self._width)

    def _getSurface (self):
        return self._length * self._width

    def _getDiagonale (self):
        return (self._length * self._length + self._width * self._width)**0.5

    def _getCircumcircle (self):
        return Disk (self.length / 2)


    def _setLength (self, nLength):
        if isOK (nLength) and nLength >= self.width:
            self._length = nLength

        else:
            print ("\n Invalid new length : it must be a positive non-zero real number greater or equals than width !\n")

    def _setWidth (self, nWidth):
        if isOK (nWidth) and nWidth <= self.length:
            self._width = nWidth

        else:
            print ("\n Invalid new width : it must be a positive non-zero real number lesser or equals than length !\n")

    def _setSide (self, nSide):
        if isOK (nSide):
            self._length = nSide
            self._width = nSide

        else:
            print ("\n Invalid new side : it must be a positive non-zero real number !\n")

    def _setPerimeter (self, nPerimeter):
        print ("\n Impossible to change it !\n")

    def _setSurface (self, nSurface):
        print ("\n Impossible to change it !\n")

    def _setDiagonale (self, nDiagonale):
        print ("\n Impossible to change it !\n")

    def _setCircumcircle (self, nCircumcircle):
        print ("\n You aren't allowed to do this, sorry !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw rectangle {5} {0} {1} {2} {3} {4}'.format (self.length, self.width, self.perimeter, self.surface, self.diagonale, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._length *= n
            self._width *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._length /= n
            self._width /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Rectangle (self._length * n, self._width * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Rectangle (self._length / n, self._width / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Rectangle:
            return self.length == n.length and self.width == n.width

        print ("\n Invalid operands : they must be two rectangles !\n")

    def __ne__ (self, n):
        if type (n) is Rectangle:
            return self.length != n.length or self.width != n.width

        print ("\n Invalid operands : they must be two rectangles !\n")


    length = property (_getLength, _setLength)
    width = property (_getWidth, _setWidth)

    side = property (_getSide, _setSide)

    perimeter = property (_getPerimeter, _setPerimeter)
    surface = property (_getSurface, _setSurface)
    diagonale = property (_getDiagonale, _setDiagonale)

    circumcircle = property (_getCircumcircle, _setCircumcircle)


##########################################################


class Square:
    __type__ = "Square"

    def __init__ (self, side):
        if side > 0:
            self._side = side

        else:
            print ("\n Invalid side : it must be a positive non-zero real number !\n Initialization of default value...\n Done\n")
            self._side = 1


    def _getSide (self):
        return self._side

    def _getPerimeter (self):
        return self._side * 4

    def _getSurface (self):
        return self._side**2

    def _getApothem (self):
        return self._side / 2

    def _getDiagonale (self):
        return self._side * 2**0.5

    def _getCircumcircle (self):
        return Disk ((self._side * 2**0.5).real / 2)

    def _getInscribedCircle (self):
        return Disk (self._side / 2)


    def _setSide (self, nSide):
        if nSide > 0:
            self._side = nSide

        else:
            print ("\n Invalid new side : it must be a positive non-zero real number !\n")

    def _setPerimeter (self, nPerimeter):
        if nPerimeter > 0:
            self._side = nPerimeter / 4

        else:
            print ("\n Invalid new perimeter : it must be a positive non-zero real number !\n")

    def _setSurface (self, nSurface):
        if nSurface > 0:
            self._side = nSurface**0.5

        else:
            print ("\n Invalid new surface : it must be a positive non-zero real number !\n")

    def _setApothem (self, nApothem):
        if isOK (nApothem):
            self._side = nApothem * 2

        else:
            print ("\n Invalid new apothem : it must be a positive non-zero real number !\n")

    def _setDiagonale (self, nDiagonale):
        if isOK (nDiagonale):
            self._side = nDiagonale / 2**0.5

        else:
            print ("\n Invalid new apothem : it must be a positive non-zero real number !\n")

    def _setCircumcircle (self, n):
        if isOK (n):
            self._side = (n * 2**0.5).real

        elif type (x) is Disk:
            self._side = (n.radius * 2**0.5).real

        else:
            print ("\n Invalid new circumscribed circle : it could be a Disk or a positive non-zero real number !\n")

    def _setInscribedCircle (self, n):
        if isOK (n):
            self._side = n * 2

        elif type (n) is Disk:
            self._side = n.radius * 2

        else:
            print ("\n Invalid new inscribed circle : it could be a Disk or a positive non-zero real number !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw square {5} {0} {1} {2} {3} {4}'.format (self.side, self.perimeter, self.surface, self.apothem, self.diagonale, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._side *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._side /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Square (self._side * n)

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Square (self._side / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Square:
            return self.side == n.side

        print ("\n Invalid operands : they must be two squares !\n")

    def __ne__ (self, n):
        if type (n) is Square:
            return self.side != n.side

        print ("\n Invalid operands : they must be two squares !\n")


    side = property (_getSide, _setSide)
    
    perimeter = property (_getPerimeter, _setPerimeter)
    surface = property (_getSurface, _setSurface)
    apothem = property (_getApothem, _setApothem)
    diagonale = property (_getDiagonale, _setDiagonale)

    circumcircle = property (_getCircumcircle, _setCircumcircle)
    inscribedCircle = property (_getInscribedCircle, _setInscribedCircle)


##########################################################


class Ellipsoid:
    __type__ = "Ellipsoid"
    
    def __init__ (self, a, b = None, c = None):
        if b is None:
            b = a
            c = a

        if isOK (a) and isOK (b) and isOK (c):
            self._a = a
            self._b = b
            self._c = c

        else:
            print ("\n Invalid arguments : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")

            self._a = 1
            self._b = 1
            self._c = 1


    def _getA (self):
        return self._a

    def _getB (self):
        return self._b

    def _getC (self):
        return self._c

    def _getRadius (self):
        if self._a == self._b == self._c:
            return self._a

        print ("\n You can't access to this property !\n")
        raise RuntimeError

    def _getVolume (self):
        return 4 * pi * self._a * self._b * self._c / 3

    def _getSurface (self):
        if self._a == self._b == self._c:
            return 4 * pi * self._a * self._a

        print ("\n You can't access to this property !\n")
        raise RuntimeError


    def _setA (self, nA):
        if isOK (nA):
            self._a = nA
                            
        else:
            BSOD ()

    def _setB (self, nB):
        if isOK (nB):
            self._b = nB
                            
        else:
            BSOD ()
                            
    def _setC (self, nC):
        if isOK (nC):
            self._c = nC

        else:
            print ("\n Invalid value : it must be a positive non-zero real number !\n")

    def _setRadius (self, nRadius):
        if isOK (nRadius):
            self._a = nRadius
            self._b = nRadius
            self._c = nRadius

        else:
            print ("\n Invalid new radius : it must be a positive non-zero real number !\n")

    def _setVolume (self, nVolume):
        print ("\n Impossible to change it !\n")

    def _setSurface (self, nSurface):
        print ("\n Impossible to change it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named {} in this object !\n".format (name))

    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw ellipsoid {4} {0} {1} {2} {3}'.format (self.a, self.b, self.c, self.volume, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._a *= n
            self._b *= n
            self._c *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._a /= n
            self._b /= n
            self._c /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Ellipsoid (self._a * n, self._b * n, self._c * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Ellipsoid (self._a / n, self._b / n, self._c / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Ellipsoid:
            return self.a == n.a and self.b == n.b and self.c == n.c

        print ("\n Invalid operands : they must be two ellipsoids !\n")

    def __ne__ (self, n):
        if type (n) is Ellipsoid:
            return self.a != n.a or self.b != n.b or self.c != n.c

        print ("\n Invalid operands : they must be two ellipsoids !\n")


    a = property (_getA, _setA)
    b = property (_getB, _setB)
    c = property (_getC, _setC)
    radius = property (_getRadius, _setRadius)
    volume = property (_getVolume, _setVolume)
    surface = property (_getSurface, _setSurface)


##########################################################


class Ellipse:
    __type__ = "Ellipse"
    
    def __init__ (self, a, b = None):
        if b is None:
            b = a

        if isOK (a) and isOK (b):
            self._a = a
            self._b = b

        else:
            print ("\n Invalid values : they must be positive non-zero real numbers !\n Initialization of default values...\n Done\n")
            self._a = 1
            self._b = 1


    def _getA (self):
        return self._a

    def _getB (self):
        return self._b

    def _getRadius (self):
        if self._a == self._b:
            return self._a

        print ("\n You can't access to this attribute !\n")
        raise RuntimeError

    def _getPerimeter (self):
        return 2 * pi * ((self._a * self._a + self._b * self._b) / 2)**0.5

    def _getSurface (self):
        return self._a * self._b * pi


    def _setA (self, nA):
        if isOK (nA):
            self._a = nA
            
        else:
            BSOD ()

    def _setB (self, nB):
        if isOK (nB):
            self._b = nB
            
        else:
            print ("\n Invalid new value : it must be a positive non-zero real number !\n")

    def _setRadius (self, nRadius):
        if isOK (nRadius):
            self._a = nRadius
            self._b = nRadius
            
        else:
            print ("\n Invalid new radius : it must be a positive non-zero real number !\n")
    
    def _setPerimeter (self, nPerimeter):
        print ("\n You are not allowed to do it !\n")

    def _setSurface (self, nSurface):
        print ("\n You are not allowed to do it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named {} in this object !\n".format (name))
                
    def __repr__ (self):
        print ("\n Loading resources...")
        system ('Graphics.pyw ellipse {4} {0} {1} {2} {3}'.format (self.a, self.b, self.perimeter, self.surface, _decimals_))

        return "\n Done !\n"


    def __imul__ (self, n):
        if isOK (n):
            self._a *= n
            self._b *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._a /= n
            self._b /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Ellipse (self._a * n, self._b * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Ellipse (self._a / n, self._b / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Ellipse:
            return self.a == n.a and self.b == n.b

        print ("\n Invalid operand type : they must be two ellipses !\n")

    def __ne__ (self, n):
        if type (n) is Ellipse:
            return self.a != n.a or self.b != n.b

        print ("\n Invalid operand type : they must be two ellipses !\n")


    a = property (_getA, _setA)
    b = property (_getB, _setB)
    radius = property (_getRadius, _setRadius)
    perimeter = property (_getPerimeter, _setPerimeter)
    surface = property (_getSurface, _setSurface)


##########################################################


class Polygon:
    __type__ = "Polygon"

    types = {3 : 'Equilateral triangle',
                 4 : 'Square',
                 5 : 'Pentagon',
                 6 : 'Hexagon',
                 7 : 'Heptagon',
                 8 : 'Octagon',
                 9 : 'Nonagon',
                 10 : 'Decagon',
                 12 : 'Duodecagon',
                 15 : 'Pentadecagon'}


    def __init__ (self, nSides, side):
        if isOK (nSides, 2) and isOK (side):
            self._nSides = nSides
            self._side = side

        else:
            print ("\n Do not try to make me crash !\n Initialization of default values...\n Done")
            self._nSides = 3
            self._side = 1

        try:
            self._type = Polygon.types[self._nSides]

        except KeyError:
            self._type = 'Polygon'


    def _getNSides (self):
        return self._nSides

    def _getSide (self):
        return self._side

    def _getApothem (self):
        return self._side / (2 * stan (pi / self._nSides))

    def _getPerimeter (self):
        return self._nSides * self._side

    def _getSurface (self):
        return (self._nSides * self._side**2 / (2 * stan (pi / self._nSides))) / 2

    def _getCircumcircle (self):
        return Disk (((self._side / 2 / ssin (pi / self._nSide))).real)

    def _getInscribedCircle (self):
        return Disk ((self._side / (2 * stan (pi / self._nSides))).real)


    def _setNSides (self, nNSides):
        if isOK (nNSides, 2):
            self._nSides = nNSides

            try:
                self._type = Polygon.types[self._nSides]

            except KeyError:
                self._type = 'Polygon'

        else:
            print ("\n Invalid new number of sides : it must be greater than 2 !\n")

    def _setSide (self, nSide):
        if isOK (nSide):
            self._side = nSide

        else:
            print ("\n Invalid new side : it must be a positive non-zero real number !\n")

    def _setApothem (self, nApothem):
        if isOK (nApothem):
            self._side = nApothem * 2 * stan (pi / self._nSides)

        else:
            print ("\n Invalid new apothem : it must be a positive non-zero real number !\n")

    def _setPerimeter (self, nPerimeter):
        if isOK (nPerimeter):
            self._side = nPerimeter / self._nSides

        else:
            print ("\n Invalid new perimeter : it must be a positive non-zero real number !\n")

    def _setSurface (self, nSurface):
        if isOK (nSurface):
            self._side = 2 * (stan (pi / self._nSides) * nSurface / self._nSides)**0.5

        else:
            print ("\n Invalid new surface : it must be a positive non-zero real number !\n")

    def _setCircumcircle (self, n):
        if isOK (n):
            self._side = 2 * n * ssin (pi / self._nSides)

        elif type (n) is Disk:
            self._side = 2 * n.radius * ssin (pi / self._nSides)

        else:
            print ("\n You can't do it, sorry !\n")

    def _setInscribedCircle (self, n):
        if isOK (n):
            self._side = n * 2 * stan (pi / self._nSides)

        elif type (n) is Disk:
            self._side = n.radius * 2 * stan (pi / self._nSides)

        else:
            print ("\n The new inscribed circle must be a Disk or its radius, please be nice...\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        return "\n Type : {0}\n Number of sides : {1}\n Side : {2}\n Apothem : {3}\n Perimeter : {4}\n Surface : {5}\n".format (self._type, self._nSides, formated (self._side), formated (self.apothem), formated (self.perimeter), formated (self.surface))


    def __imul__ (self, n):
        if isOK (n):
            self._side *= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __itruediv__ (self, n):
        if isOK (n):
            self._side /= n

        else:
            print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

        return self

    def __mul__ (self, n):
        if isOK (n):
            return Polygon (self._nSides, self._side * n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __truediv__ (self, n):
        if isOK (n):
            return Polygon (self._nSides, self._side / n)

        print ("\n Invalid coefficient : it must be a positive non-zero real number !\n")

    def __rmul__ (self, n):
        return self * n


    def __eq__ (self, n):
        if type (n) is Polygon:
            return self.nSides == n.nSides and self.side == n.side

        print ("\n Invalid operand type : they must be two {} !\n".format (self._type))

    def __ne__ (self, n):
        if type (n) is Polygon:
            return self.nSides != n.nSides or self.side != n.side

        print ("\n Invalid operand type : they must be two {} !\n".format (self._type))


    nSides = property (_getNSides, _setNSides)
    side = property (_getSide, _setSide)

    apothem = property (_getApothem, _setApothem)
    perimeter = property (_getPerimeter, _setPerimeter)
    surface = property (_getSurface, _setSurface)

    circumcircle = property (_getCircumcircle, _setCircumcircle)
    inscribedCircle = property (_getInscribedCircle, _setInscribedCircle)


##########################################################


class Vector:
    __type__ = "Vector"
    
    def __init__ (self, x = 0, y = 0):
        if (type (x) is not complex) and (type (y) is not complex):
            self._x = x
            self._y = y

        else:
            print ("\n Do not try to make me crash !\n Initialization of default values...\n Done")
            self._x = 0
            self._y = 0

    def _getX (self):
        return self._x

    def _getY (self):
        return self._y

    def _getLength (self):
        return (self._x * self._x + self._y * self._y)**0.5


    def _setX (self, nX):
        if type (nX) is not complex:
            self._x = nX

    def _setY (self, nY):
        if type (nY) is not complex:
            self._y = nY

    def _setLength (self, nLength):
        print ("\n Impossible to change it !\n")


    def __getattr__ (self, name):
        print ("\n There is no attribute named \"{}\" in this object !\n".format (name))

    def __repr__ (self):
        return "\n ({0} ; {1})\n Length : {2}\n".format (formated (self.x), formated (self.y), formated (self.length))


    def __add__ (self, n):
        if type (n) is Vector:
            return Vector (self.x + n.x, self.y + n.y)

        print ("\n Invalid operands : they must be two vectors !\n")

    def __sub__ (self, n):
        if type (n) is Vector:
            return Vector (self.x - n.x, self.y - n.y)

        print ("\n Invalid operands : they must be two vectors !\n")

    def __mul__ (self, n):
        if type (n) is Vector:
            return self.x * n.x + self.y * n.y

        elif (type (n) is int) or (type (n) is float):
            return Vector (self.x * n, self.y * n)

        print ("\n Error : invalid operands !\n")

    def __rmul__ (self, n):
        return self * n

    def __truediv__ (self, n):
        if type (n) is int or type (n) is float:
            return Vector (self.x / n, self.y / n)

        print ("\n Error : invalid operands !\n")

    def __iadd__ (self, n):
        if type (n) is Vector:
            self._x += n.x
            self._y += n.y

        else:
            print ("\n Error : invalid operands !\n")

        return self

    def __isub__ (self, n):
        if type (n) is Vector:
            self._x -= n.x
            self._y -= n.y

        else:
            print ("\n Error : invalid operands !\n")

        return self

    def __imul__ (self, n):
        if type (n) is Vector:
            return self.x * n.x + self.y * n.y

        elif type (n) is int or type (n) is float:
            self._x *= n
            self._y *= n

        else:
            print ("\n Error : invalid operands !\n")

        return self

    def __itruediv__ (self, n):
        if type (n) is int or type (n) is float:
            self._x /= n
            self._y /= n

        else:
            print ("\n Error : invalid operands !\n")

        return self


    def __eq__ (self, n):
        if type (n) is Vector:
            return self.x == n.x and self.y == n.y

        print ("\n Invalid operands : they must be two vectors !\n")

    def __ne__ (self, n):
        if type (n) is Vector:
            return self.x != n.x or self.y != n.y

        print ("\n Invalid operands : they must be two vectors !\n")

    def __gt__ (self, n):
        if type (n) is Vector:
            return self.length > n.length

        print ("\n Invalid operands : they must be two vectors !\n")

    def __lt__ (self, n):
        if type (n) is Vector:
            return self.length < n.length

        print ("\n Invalid operands : they must be two vectors !\n")

    def __ge__ (self, n):
        if type (n) is Vector:
            return self.length >= n.length

        print ("\n Invalid operands : they must be two vectors !\n")

    def __le__ (self, n):
        if type (n) is Vector:
            return self.length <= n.length

        print ("\n Invalid operands : they must be two vectors !\n")


    length = property (_getLength, _setLength)
    x = property (_getX, _setX)
    y = property (_getY, _setY)


    ##########################################################


##########################################################   It's finished !


print ("\n\n All modules are loaded !\n")


