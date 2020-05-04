"""
NyanMaths CL version (Tools module) - Created by MemeTech INC

In the documentation, you can see all fonctionnalities of this application.

Creator : NY4N_M4THS
"""


from time import sleep
from os import system
from os.path import exists


if exists ('Versions/Conf.pastouche'):
    config = open ('Versions/Conf.pastouche', 'r').read ().split (' ')

    _precision_ = int (config[0])

    _unit_ = config[1]

else:
    open ('Versions/Conf.pastouche', 'w').write ("{0} {1}".format (_precision_, _unit_))


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



def primes ():
    n = input ("\n This application computes all prime numbers\n from an odd positive non-zero number to... Another greater positive number !\n Beware : the last numbers will be deleted !\n\n Calculate the prime numbers from ")
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
                sqrtn = int (n**0.5 + 1)
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
        return ''

    else:
        x = 0
        div = int (n / 2) + 1

        while div > 1:
            if n % div == 0:
                print (" By {0}       {1} times".format (div, int (n / div)))
                x += 1

            div -= 1

        if x > 0:
            print ("\n That's all !\n")

        else:
            print ("\n There's no divider : {} is prime !\n".format (n))


def UIR ():
    print ("\n Thanks to this application, you can calculate the relationship between intensity, electric tension and resistance.\n Give me 0 for the value you want to get.")

    try:
        u = float (input ("\n Input elecric tension :  "))
        r = float (input ("\n Resistance, please :  "))
        i = float (input ("\n To finish, intensity (Not \"please\"  :-D) :  "))

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


def PUI ():
    "\n This tool can compute the relationship between intensity, electric tension and power.\n Give it 0 for the value you want to get."
    
    print ("\n This tool can compute the relationship between intensity, electric tension and power.\n Give it 0 for the value you want to get.")

    try:
        u = float (input ("\n Input elecric tension :  "))
        p = float (input ("\n Enter power, please :  "))
        i = float (input ("\n To finish, intensity (Not \"please\", cause I work for you) :  "))

        assert (u == 0) ^ (p == 0) ^ (i == 0)

    except:
        print ("\n\n Please don't try to make me crash !\n")

    else:
        if u == 0:
            print ("\n Electric tension :  {}\n".format (trans (p / i)))

        elif i == 0:
            print ("\n Intensity :  {}\n".format (trans (p / u)))

        else:
            print ("\n Power :  {}\n".format (trans (u * i)))


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


def MVD ():
    print ("\n Thanks to this tool, you can calculate the relationship between density, weight and volume.\n Give me 0 for the value you want to get.")

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
    print ("\n Helloooooooo !\n Thanks to this little tool, you can convert temperature units :\n\n a) Celsius --> Fahreneit\n b) Celsius --> Kelvin\n c) Fahreneit --> Celsius\n d) Fahreneit --> Kelvin\n e) Kelvin --> Celsius\n f) Kelvin --> Fahreneit")

    c = input ("\n\n Choose the conversion to do : ")

    if c == 'a' or c == 'A':
        try:
            n = float (input ("\n Input the value in °C : "))
            print ("\n\n {0}°C = {1}°F\n".format (trans (n), trans ((1.8 * n) + 32)))

        except:
            BSOD ()

    elif c == 'b' or c == 'B':
        try:
            n = float (input ("\n Input the value in °C : "))
            print ("\n\n {0}°C = {1}°K\n".format (trans (n), trans (n + 273.15)))

        except:
            BSOD ()

    elif c == 'c' or c == 'C':
        try:
            n = float (input ("\n Input the value in °F : "))
            print ("\n\n {0}°F = {1}°C\n".format (trans (n), trans ((n - 32) / 1.8)))

        except:
            BSOD ()

    elif c == 'd' or c == 'D':
        try:
            n = float (input ("\n Input the value in °F : "))
            print ("\n\n {0}°F = {1}°K\n".format (trans (n), trans ((n - 32) / 1.8 + 273.15)))

        except:
            BSOD ()

    elif c == 'e' or c == 'E':
        try:
            n = float (input ("\n Input the value in °K : "))
            print ("\n\n {0}°K = {1}°C\n".format (trans (n), trans (n - 273.15)))

        except:
            BSOD (True)

    elif c == 'f' or c == 'F':
        try:
            n = float (input ("\n Input the value in °K : "))
            print ("\n\n {0}°K = {1}°F\n".format (trans (n), trans ((n - 273.15) * 1.8 + 32)))

        except:
            BSOD ()

    else:
        BSOD (True)
