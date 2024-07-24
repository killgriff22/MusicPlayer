from functions import *
string = "1"
while True:
  count = 1
  clear()
  new_string=""
  prev_chr = ""
  for chr in string:
    if prev_chr==chr: count+=1
    else:
        new_string+=str(count)+prev_chr
        count=1
    prev_chr = chr
  string = new_string
  print(string)