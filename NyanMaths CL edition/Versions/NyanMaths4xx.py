# coding: utf-8


"""
NyanMaths CL version 4.xx.xx (Main module) - Created by MemeTech INC

In the documentation, you can see all functionalities of this application.

Creator : NY4N_M4THS
"""


#######################  STL loading  #######################


from os import system
from random import randint

from os.path import exists
from os import mkdir, remove
from shutil import rmtree
import glob

from time import sleep

from cmath import log

import re


#######################  Pre-configuration 1  #######################


if exists ('Startup configuration.pastouche'):
    _startupConf = open ('Startup configuration.pastouche').read ().split (' ')

else:
    _startupConf = ['1', '1', 'f0', '4.1.1', '1', '1']


system ("title NyanMaths  --  Loading...")

system ("cls")
system ("color {}".format (_startupConf[2]))


#######################  Pre-configuration 2  #######################


constsList = [list (), list (), list (), list (), list (), list (), list (), list ()]
category = 0
modules = open ('Versions/4xx/{}.pastouche'.format (_startupConf[3])).read ().split ('\n&&&&&&&&&&&&&&&&&&&&&\n')


for moduleName in modules[0].split ('\n'):
    if moduleName == '#####################':
        category += 1

    else:
        constsList[category].append (moduleName)


if _startupConf[0] == '1':
    category += 1

    for moduleName in modules[1].split ('\n'):
        constsList[category].append (moduleName)    


if _startupConf[5] == '1':
    category += 1

    for moduleName in modules[2].split ('\n'):
        constsList[category].append (moduleName) 


drg = 'drg'
rad = 'rad'

_precision_ = 9
_unit_ = rad


if exists ('Versions/Conf.pastouche'):
    config = open ('Versions/Conf.pastouche', 'r').read ().split (' ')

    _precision_ = int (config[0])

    _unit_ = config[1]

else:
    open ('Versions/Conf.pastouche', 'w').write ("{0} {1}".format (_precision_, _unit_))


###########################################################
######################    Loading    ######################
###########################################################


categories = ['Core', 'Functions', 'Others', 'Consts', 'Objects', 'Tools']
category = 0


while category != 6:
    for moduleName in constsList[category]:
        strModule = open ('Versions/4xx/{0}/{1}.mt_data'.format (categories[category], moduleName)).read ()

        exec (strModule)

    category += 1


#######################  User functions  #######################


userFunctionName = ''

try:
    for userFunctionName in glob.glob ('User Functions/*.mt_data'):

        end = len (userFunctionName) - 1
        while userFunctionName[end] != '.':
            end -= 1

        begin = end
        while not userFunctionName[begin - 1] in ['/', '\\']:
            begin -= 1

        print ("\n Importing {}(x)...".format (userFunctionName[begin:end]))
        exec (open (userFunctionName, 'r').read ())
        constsList[category].append (userFunctionName[begin:end])

except:
    print ("\n\n Error in user module {}\n Please update the application to fix this bug !\n".format (userFunctionName))


#######################  User constants  #######################


category += 1
userConstName = ''

try:
    for userConstName in glob.glob ('User constants/*.mt_data'):

        end = len (userConstName) - 1
        while userConstName[end] != '.':
            end -= 1

        begin = end
        while not userConstName[begin - 1] in ['/', '\\']:
            begin -= 1

        print ("\n Importing {}...".format (userConstName[begin:end]))

        exec (userConstName[begin:end] + '=' + open (userConstName, 'r').read ())
        constsList[category].append (userConstName[begin:end])

except:
    print ("\n\n Error in user module {}\n Please update the application to fix this bug !\n".format (userConstName))


#############################################################
#######################   Main code   #######################
#############################################################


#######################  Help  #######################


if int (_startupConf[1]) or int (_startupConf[4]):
    if exists ('Versions/4xx/help{}.pastouche'.format (_startupConf[3])):
        helpText = open ('Versions/4xx/help{}.pastouche'.format (_startupConf[3]), 'r').read ().split ('&')

        if int (_startupConf[1]):
            print (helpText[0])

        if int (_startupConf[4]):
            print (helpText[1])

    else:
        print ("\n My help file's missing in my folder : may I get it back ?\n If you have not touched anything, please reinstall this application to fix this issue !\n")


print ("\n Welcome to NyanMaths Command Line edition !\n If you don't know how to use it : RTFM !\n\n Unit : {0}\n Floating point precision : {1}".format (_unit_, _precision_))



print ("\n\n You can check on our website for updates :\n https://memetech-inc.weebly.com/nyanmaths-cl \n\n\n")
system ("title Welcome to NyanMaths CL {} !".format (_startupConf[3]))


#######################   Dump memory   #######################


del helpText
del modules
del category
del categories
del moduleName
del userFunctionName
del userConstName


#######################  Main loop  #######################


constsList.append (open ('Versions/4xx/privateConsts.pastouche').read ().split ('\n'))

cmd = ''
last = ''

while True:  # Main loop
    cmd = input (" > What can I do ?  ")

    cmd = re.sub (' ', '', cmd)
    cmd = re.sub ('\^', '**', cmd)


    _r = None  # The return-value of user's commands

    if cmd == 'last':
        cmd = str (last)

    if cmd in ['quit', 'exit']:
        break

    if cmd != '':  # If the user entered something
        try:
            if (('=' in cmd) and (not '==' in cmd)):  # If the user want to create an object
                _index = 0
                while _index != len (constsList):
                    for const in constsList[_index]:   # Make sure the user isn't trying to edit a constant
                        if re.search ('^' + const + '=', cmd):
                            print ("\n\n You aren't allowed to edit constant values, lil script kiddy !\n\n")
                            raise RuntimeError

                    _index += 1

                exec (cmd)
                print ("\n", end = '')

            else:
                _r = eval (cmd)   # If the user want the app to compute something

            if _r is not None:
                if (type (_r) is complex) or (type (_r) is int) or (type (_r) is float):   # If there's a result to display (number)
                    print ("\n", trans (_r), "\n")

                else:   # If the result is a string or a boolean
                    print ("\n ", _r, "\n")

            last = str (cmd)


        # Exceptions management

        except TypeError:
            print ("\n Invalid operand type !\n")

        except NameError:
            print ("\n This variable or type doesn't exist !\n Don't forget to capitalize object types or import all modules !\n")

        except ZeroDivisionError:
            print ("\n Newbie's error #0 : division by zero !\n")

        except ValueError:
            print ("\n You gave an invalid value somewhere !\n")

        except KeyboardInterrupt:
            exit (0)

        except RuntimeError:  # If the exception was already managed
            pass

        except:
            print ("\n An unknown error has occurred, sorry !\n")