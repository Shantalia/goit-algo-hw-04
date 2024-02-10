from colorama import Fore, Back, Style
from pathlib import Path
import sys

# pip install -r requirements.txt python Task3.py
def script(path):


    return


#path = Path("C:/Users/Shantalia/Documents/Python_course/goit-algo-hw-04/Task3")
directory = Path("./.venv")
lst = sys.argv
#if len(lst) <=2:
for path in directory.iterdir():
    print(path)
#else: 
#    print("Wrong input!")
