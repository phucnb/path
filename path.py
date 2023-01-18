# Python Program to create and change
# the directory then create a python file for same name

import os
import sys

# Check command-line arguments
if len(sys.argv) not in [2, 3]:
    sys.exit()

name = sys.argv[1] # folder name

if not os.path.exists(name): # Check if folder exists
    os.mkdir(name) # if not then create one

os.chdir(name) # change directory to the folder

# option to create test_[name].py for testing purpose
if (len(sys.argv) == 3 and sys.argv[2] == '-t'):
    os.system(f"code test_{name}.py")

# Open the file
os.system(f"code {name}.py")

# remain the currect directory after exit program
os.system("/bin/bash")

