
import pygame
import math
from queue import PriorityQueue
pygame.init()
win=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("A* Algorithm")
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
def get_f(p1,p2):  #manhattan distance
         fx,fy=p1 
         sx,sy=p2 
         return abs(fx-sx)+abs(fy-sy)
def check(x,y,arr):
         return x>=0 and x<total_rows and y>=0 and y<total_rows and not arr[x][y].is_blocked()
def algorithm(win,arr,start,end):
         pq=PriorityQueue()
         h_val={}
         g_val={}
         found=False
         par={}
         for row in arr:
                  for spot in row:
                           h_val[spot]=10000000.000000
                           g_val[spot]=10000000
                           par[spot]=spot
         g_val[start]=0
         h_val[start]=get_f(start.getpos(),end.getpos())
         row,col=start.getpos()
         pq.put((h_val[start],row,col))
         while not pq.empty():
                  for event in pygame.event.get():
                           if event.type==pygame.QUIT:
                                    pygame.quit()
                  current=pq.get()
                  dis=current[0]
                  px=current[1]
                  py=current[2]
                  pre=arr[px][py]
                  if pre==end:
                           found=True
                           break
                  if check(px+1,py,arr):
                           sp=arr[px+1][py]
                           if(g_val[pre]+1<g_val[sp]):
                                    g_val[sp]=g_val[pre]+1
                                    h_val[sp]=get_f(sp.getpos(),end.getpos())+g_val[sp]
                                    pq.put((h_val[sp],px+1,py))
                                    par[sp]=pre
                                    sp.addtopath()
                  if check(px-1,py,arr):
                           sp=arr[px-1][py]
                           if(g_val[pre]+1<g_val[sp]):
                                    g_val[sp]=g_val[pre]+1
                                    h_val[sp]=get_f(sp.getpos(),end.getpos())+g_val[sp]
                                    pq.put((h_val[sp],px-1,py))
                                    par[sp]=pre
                                    sp.addtopath()
                  if check(px,py+1,arr):
                           sp=arr[px][py+1]
                           if( g_val[pre]+1<g_val[sp]):
                                    g_val[sp]=g_val[pre]+1
                                    h_val[sp]=get_f(sp.getpos(),end.getpos())+g_val[sp]
                                    pq.put((h_val[sp],px,py+1))
                                    par[sp]=pre
                                    sp.addtopath()
                  if check(px,py-1,arr):
                           sp=arr[px][py-1]
                           if(g_val[pre]+1<g_val[sp]):
                                    g_val[sp]=g_val[pre]+1
                                    h_val[sp]=get_f(sp.getpos(),end.getpos())+g_val[sp]
                                    pq.put((h_val[sp],px,py-1))
                                    par[sp]=pre
                                    sp.addtopath()
                  draw_grid(win,arr)
         if not found:
                  pygame.quit()
         spot=end
         while par[spot]!=spot:
                  spot.shortestpath()
                  spot=par[spot]
         start.shortestpath()
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
                                    if event.key==pygame.K_SPACE:
                                             started=True
                                             algorithm(win,arr,start,end)
         pygame.quit()                  
f=main(win)



                  
         
         
         
         
         



