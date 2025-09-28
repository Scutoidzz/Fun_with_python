import os
import sys
def clearer(sysvers):
    if sysvers == "windows":
      os.system('cls')
    if sysvers == "linux":
      os.system("clear")