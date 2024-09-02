import numpy as np
import time
from tkinter import *

class node:
     def __init__(self, location = (-999, -999), p = None):
          self.location = location
          self.next = p

def PM():
     for i in range(m):
          for j in range(n):
               print(A[i, j], end = '')
          print()




head = node()
fn = input('Enter your filename: ')
fo = open(fn, 'r')
L = fo.readlines()
m = len(L)
n = max( [ len(L[i]) for i in range(m)] ) - 1
fo.close()
print(m, n)

A = np.zeros((m, n), dtype = str)

for i in range(m):
     for j in range(n):
          if j < len(L[i]) - 1:
               A[i, j] = L[i][j]


while True:
     ib = np.random.randint(0, m)
     jb = np.random.randint(0, n)
     if A[ib, jb] == ' ':
          A[ib, jb] = 'B'
          break
     
while True:
     ie = np.random.randint(0, m)
     je = np.random.randint(0, n)
     if A[ie, je] == ' ':
          A[ie, je] = ' '
          break
print(())
########

########
#L = []
i, j = ib, jb
A[i, j] = 'B'
head.next = node((i, j), head.next)
while (i, j) != (ie, je):
     if i - 1 >= 0 and A[i - 1, j] == ' ':#N
          i -= 1
          A[i, j] = '.'
          head.next = node((i, j), head.next)
     elif j + 1 < n and A[i, j + 1] == ' ':#E
          j += 1
          A[i, j] = '.'
          head.next = node((i, j), head.next)
     elif j - 1 >= 0 and A[i, j - 1] == ' ':#W
          j -= 1
          A[i, j] = '.'
          head.next = node((i, j), head.next)
     elif i + 1 < m and A[i + 1, j] == ' ':#S
          i += 1
          A[i, j] = '.'
          head.next = node((i, j), head.next)
     else:
          if head.next.next:
               head.next = head.next.next
          if head.next:
               i, j = head.next.location
          else:break
A[ie, je] = 'E'
head.next = node((ie, je), head.next)
h2 = node()

while head.next:
     ptr = head.next
     head.next = ptr.next
     ptr.next = h2.next
     h2.next = ptr

'''
ptr = h2.next

while ptr.next:
     print('->',ptr.location , end = '')
     ptr = ptr.next
'''
########
ts1 = 625
ts2 = ts1 ** 0.5
maze = Tk()
canvas = Canvas(maze, width = ts1*n, height = ts1*m)
canvas.pack()

for i in range(m):
     for j in range(n):
          if A[i, j] == '%':
               canvas.create_rectangle(ts2*j, ts2*i, ts2 + ts2*j, ts2 + ts2*i, fill = 'green', outline = 'black')
          
ob = canvas.create_arc(ts2*jb, ts2*ib, ts2 + ts2*jb, ts2 + ts2*ib, extent = 359, fill = 'yellow')

ptr = h2.next
while ptr.next:
     canvas.move(ob, ts2*(ptr.next.location[1] - ptr.location[1]), ts2*(ptr.next.location[0] - ptr.location[0]))
     ptr = ptr.next
     maze.update()
     time.sleep(0.05)

########







