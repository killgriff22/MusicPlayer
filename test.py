import os
import time
from functions import *
string = "1"
print(string)
last=0.1
clear()
while True:
  before = time.time()
  count = 0
  prev_char = string[0]
  frequencies = []
  x=1
  y=1
  for char in string+" ":
    if char == prev_char:
      count += 1
    else:
      frequencies.append([count,prev_char])
      print_at(x,y,f"{count}{prev_char}")
      x+=2
      if x >= os.get_terminal_size().columns:
        y+=1
        x=1
      if y >= os.get_terminal_size().lines:
        y=1
        clear() 
     count = 1
    prev_char = char
  new_string = ""
  for count,i in enumerate(frequencies):
    new_string += str(i[0])+i[1]
  string = new_string
  after = time.time()
  t = after-before
  percent = t/last*100//1 if t >0.0 and last > 0.0 else "N/A"
  clear()
  print(string if len(string) < os.get_terminal_size().columns else f"{t if not t > 60 else str(t//60)+'m'} (%{percent}{'+' if percent>100 else '-' if percent<100 else '='})")
  last =t
  print("sleeping for 1 sec")
  sleep(1)
