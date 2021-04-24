import random as r
player = r.randint(1,2)
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def Render():
  i=0
  print("  1  2  3")
  for row in game:
    i += 1 
    print(i, end = '')
    print(row)

  PlayerChange()
  

def DataPlot():
  global x 
  global y
  x=input("X --> ")
  y=input("Y --> ")
  x = int(x)
  y = int(y)
  if x >= 4:
    x=3

  if x <= 0:
    x=1

  if y >= 4:
    y=3

  if y <= 0:
    y=1

  game[y-1][x-1] = player
  Render()


def PlayerChange():
  global player
  if player == 1:
    player = 2
  else:
    player = 1
  DataPlot()

input("Enter to continue")
Render()

