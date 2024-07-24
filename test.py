import os
import time
from functions import *
width,height = os.get_terminal_size()
height-=1
space=width*height
if sys.argv[1].isdigit():
  string = sys.argv[1]
else:
  with open(sys.argv[1],"r") as f:
    string = f.read()
    f.close()
last=0.1
clear()
steps=int(sys.argv[2])
times = []
x,y=0,0
while True:
  if len(sys.argv) == 5 and steps-int(sys.argv[2]) == int(sys.argv[3]):
    with open(sys.argv[4],"w") as f:
      f.write(string)
      f.close()
    exit()
