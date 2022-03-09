
import math
import random
import pygame 
import tkinter as tk
from tkinter import messagebox

class dot(object):
    rows = 20
    width = 500

    def __init__(self, start, dirx=1, diry=0, color=(255,0,0)):
        self.pos = start
        self.dirx = 1
        self.diry = 0
        self.color = color

    def move(self, dirx, diry):
        self.dirx = dirx
        self.diry = diry
        self.pos = (self.pos[0] + self.dirx, self.pos[1] + self.diry)

    def draw(self, surface, head=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if head:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = dot(pos)
        self.body.append(self.head)
        self.dirx = 0
        self.diry = 1

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys [pygame.K_LEFT] :
                self.dirx = -1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]        

            elif keys [pygame.K_RIGHT] :
                self.dirx = 1
                self.diry = 0
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]    

            elif keys [pygame.K_UP] :
                self.dirx = 0
                self.diry = -1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

            elif keys [pygame.K_DOWN] :
                self.dirx = 0
                self.diry = 1
                self.turns[self.head.pos[:]] = [self.dirx, self.diry]

        # Random movement of new dot
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn [0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)  

            else:
                if c.dirx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirx,c.diry)

    def reset(self, pos):
        self.head = dot(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def adddot(self):
        tail = self.body[-1]
        dx, dy = tail.dirx, tail.diry
 
        if dx == 1 and dy == 0:
            self.body.append(dot((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(dot((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(dot((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(dot((tail.pos[0],tail.pos[1]+1)))
 
        self.body[-1].dirx = dx
        self.body[-1].diry = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)

# Creating grid
def drawGrid(width, rows,surface):
    sizeBtwn = width // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0), (x, width))
        pygame.draw.line(surface, (255,255,255), (0, y), (width, y))

# Updating grid
def redrawWindow(surface):
    global rows, width, snake_object, newDot
    surface.fill((0,0,0))
    snake_object.draw(surface)
    newDot.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomnewDot(rows, items):
    positions = items.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break

    return (x,y)    

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

# Main loop of the game
def main():
    global width, rows, snake_object, newDot
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, width)) # Defining display
    snake_object = snake((255, 0, 0), (10, 10)) # Creating snake object
    newDot = dot(randomnewDot(rows, snake_object), color = (0, 255, 0))
    flag = True 

    clock_game = pygame.time.Clock() # Defining variable related to the speed of the movement

    while flag:
        # Controlling the speed of movement
        pygame.time.delay(50)
        clock_game.tick(10)
        snake_object.move()
        if snake_object.body[0].pos == newDot.pos:
            snake_object.adddot()
            newDot = dot(randomnewDot(rows, snake_object), color = (0, 255, 0))

        for x in range(len(snake_object.body)):
            if snake_object.body[x].pos in list(map(lambda z:z.pos,snake_object.body[x+1:])):
                print('Score: ', len(snake_object.body))
                message_box('You Lost!', 'Play again')
                snake_object.reset((10,10))
                break

        redrawWindow (win)

    pass    
    