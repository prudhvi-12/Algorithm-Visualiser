import pygame
import math
from queue import PriorityQueue,Queue
pygame.init()
win=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("DEPTH FIRST SEARCH")
total_rows=70
width=20
total_width=1000
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
purple=(102,0,102)
maroon=(112,0,0)
class spot:
         def __init__(self,x,y,row,col,color):
                  self.x=x
                  self.y=y
                  self.row=row
                  self.col=col
                  self.color=color
         def draw(self):
                  pygame.draw.rect(win,self.color,(self.x,self.y,width,width))
         def is_blocked(self):
                  return self.color==black
         def isstart(self):
                  return self.color==red
         def isend(self):
                  return self.color==blue 
         def make_start(self):
                  self.color=red
         def make_end(self):
                  self.color=blue
         def addtopath(self):
                  self.color=green
         def block(self):
                  self.color=black
         def reset(self):
                  self.color=white
         def getpos(self):
                  return self.row,self.col
         def shortestpath(self):
                  self.color=maroon
def make_grid(win):
         win.fill(black)
         arr=[]
         x=0
         y=0
         for i in range(total_rows):
                  arr.append([])
                  for j in range(total_rows):
                           s=spot(x,y,i,j,white)
                           arr[i].append(s)
                           x=x+width
                  y=y+width
                  x=0
         return arr
def draw_lines(win):
         x=0
         y=0
         k=total_rows*width
         for i in range(total_rows):
                  pygame.draw.line(win,black,(x,y),(x,y+k))
                  x+=width
         x=0
         y=0
         for i in range(total_rows):
                   pygame.draw.line(win,black,(x,y),(x+k,y))
                   y+=width
def draw_grid(win,arr):
         for row in arr:
                  for s in row:
                           s.draw()
         draw_lines(win)
         pygame.display.update()
def check(x,y,arr):
         return x>=0 and x<total_rows and y>=0 and y<total_rows and not arr[x][y].is_blocked()
def dfs(pre,end,vis,par,arr):
         pre.addtopath()
         draw_grid(win,arr)
         found=False
         if pre==end:
                  return True
         x,y=pre.getpos()
         if(check(x+1,y,arr) and arr[x+1][y] not in vis):
                  vis.append(arr[x+1][y])
                  par[arr[x+1][y]]=arr[x][y]
                  found =found or dfs(arr[x+1][y],end,vis,par,arr)
         if found:
                  return found
         if(check(x-1,y,arr) and arr[x-1][y] not in vis):
                  vis.append(arr[x-1][y])
                  par[arr[x-1][y]]=arr[x][y]
                  found=found or dfs(arr[x-1][y],end,vis,par,arr)
         if found:
                  return found
         if(check(x,y+1,arr) and arr[x][y+1] not in vis):
                  vis.append(arr[x][y+1])
                  par[arr[x][y+1]]=arr[x][y]
                  found=found or dfs(arr[x][y+1],end,vis,par,arr)
         if found:
                  return found
         if(check(x,y-1,arr) and arr[x][y-1] not in vis):
                  vis.append(arr[x][y-1])
                  par[arr[x][y-1]]=arr[x][y]
                  found=found or dfs(arr[x][y-1],end,vis,par,arr)
         return found
def algorithm(win,arr,start,end):
         par={}
         vis=[]
         par[start]=start
         vis.append(start)
         found=dfs(start,end,vis,par,arr)
         draw_grid(win,arr) 
         if not found:
                  pygame.quit()
         spot=end
         start.shortestpath()
         while spot!=par[spot]:
                  spot.shortestpath()
                  spot=par[spot]
                  draw_grid(win,arr)         
                  
def main(win):
         arr=make_grid(win)
         draw_grid(win,arr)
         start=None
         end=None
         started=False
         while 1:
                  draw_grid(win,arr)
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    pygame.quit()
                           elif pygame.mouse.get_pressed()[0] and not started:
                                    pos=pygame.mouse.get_pos()
                                    px,py=pos
                                    px=px//width
                                    py=py//width
                                    if start==None:
                                             start=arr[py][px]
                                             arr[py][px].make_start()
                                    elif end==None:
                                             end=arr[py][px]
                                             arr[py][px].make_end()
                                    else:
                                             if start!=None and end!=None and start!=arr[py][px] and end!=arr[py][px]:
                                                      arr[py][px].block()
                           elif pygame.mouse.get_pressed()[2] and not started:
                                    pos=pygame.mouse.get_pos()
                                    px,py=pos
                                    px=px//width
                                    py=py//width
                                    if start==arr[py][px]:
                                             start=None
                                    elif end==arr[py][px]:
                                             end=None
                                    arr[py][px].reset()
                           elif event.type==pygame.KEYDOWN and not started:
                                    if event.key==pygame.K_SPACE and not started:
                                             started=True
                                             algorithm(win,arr,start,end)
         pygame.quit()                  
f=main(win)



                  
         
         
         
         
         



