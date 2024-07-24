import os
import time
from functions import *
from MultiTerm import *

width,height = os.get_terminal_size()
height-=1
space=width*height
topbar = Screen((width,1),(0,0))
area = Screen((width,height-1),(0,1))
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
lastchr = ""
count=0
area.blit(string,(0,0))
area.draw()
while True:
  if len(string) > space:
    string = string[:space]
  if len(sys.argv) == 5 and steps-int(sys.argv[2]) == int(sys.argv[3]):
    with open(sys.argv[4],"w") as f:
      f.write(string)
      f.close()
    exit()
  if string[x*y] == lastchr:
      count+=1
  else:
      x-=count
      string = string[:x*y]+str(count)+lastchr+string[x*y:]
      x+=2
      count=1
      lastchr = string[x*y+1]
  area.blit(string,(0,0))
  area.draw()