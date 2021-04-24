import random as r
size = input("size ")
size = int(size)
treesize = 1
print(" " * int(size - 1), end = '')
print("/|\ ")
print(" " * int((size)-3), end = '')
print("<|(|)|>")
print(" " * int(size - 1), end = '')
print("\|/")
for i in range(0, size):
  gapsize = size - int(treesize / 2) 
  print(" " * gapsize, end = '')
  for i in range(0, treesize-1):
    if r.randint(1,4) == 1:
      if r.randint(1,3) == 1:
        print("\033[1;31;40mo", end = '')
      else:
        if r.randint(1,2) == 1:
          print("\033[1;34;40mo", end = '')
        else:
          print("\033[1;33;40mo", end = '')
    else:
      print("\033[1;32;40m^",end = '')
  print("\033[1;32;40m^",end = '')
  print("\033[1;32;0m")
  treesize += 2
if size < 7:
  print(" "* 4, end = '')
  print("#")

elif size >= 7:
  for i in range(0, int(size/7)):
    print(" " * int((size + 1 / 2) - size/8) , end = '')
    print("#" * int(size / 3))
