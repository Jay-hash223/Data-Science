import os

try:
    user_paths = os.environ['PYTHONPATH']
    print(user_paths)

except KeyError:
    user_paths = []
    print(user_paths)

#add more example of command line arguments(without class) here

import sys
print(sys.argv) #command line arguments 
print(sys.executable) # path of the python interpreter
print(sys.version) # version of the python interpreter
print(sys.platform) # platform of the python interpreter
print(sys.path) # list of the directories that will be searched  for modules
print(sys.modules) #dictionary of loadde modules
print(sys.maxsize) # maximum size of a python int on this plateform
print(sys.maxunicode) #maximum unicode point on this platform
