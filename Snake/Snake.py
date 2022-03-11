
import math
import random
import pygame 
import tkinter as tk
from tkinter import messagebox

class New_dot(object):
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

    def drawing(self, surface, headSnake=False):
        disgrid = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
 
        pygame.drawing.rect(surface, self.color, (i*disgrid+1,j*disgrid+1, disgrid-2, disgrid-2))
        if headSnake:
            centre = disgrid//2
            radius = 3
            circleMiddle = (i*disgrid+centre-radius,j*disgrid+8)
            circleMiddle2 = (i*disgrid + disgrid -radius*2, j*disgrid+8)
            pygame.drawing.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.drawing.circle(surface, (0,0,0), circleMiddle2, radius)

class snake(object):
    body_snake = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.headSnake = New_dot(pos)
        self._snake.append(self.headSnake)
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
                self.turns[self.headSnake.pos[:]] = [self.dirx, self.diry]        

            elif keys [pygame.K_RIGHT] :
                self.dirx = 1
                self.diry = 0
                self.turns[self.headSnake.pos[:]] = [self.dirx, self.diry]    

            elif keys [pygame.K_UP] :
                self.dirx = 0
                self.diry = -1
                self.turns[self.headSnake.pos[:]] = [self.dirx, self.diry]

            elif keys [pygame.K_DOWN] :
                self.dirx = 0
                self.diry = 1
                self.turns[self.headSnake.pos[:]] = [self.dirx, self.diry]

        # Random movement of new New_dot
        for i, c in enumerate(self._snake):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn [0], turn[1])
                if i == len(self._snake) - 1:
                    self.turns.pop(p)  

            else:
                if c.dirx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.diry == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.diry == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirx,c.diry)

    def reset(self, pos):
        self.headSnake = New_dot(pos)
        self._snake = []
        self._snake.append(self.headSnake)
        self.turns = {}
        self.dirx = 0
        self.diry = 1

    def adddot(self):
        tail = self._snake[-1]
        dx, dy = tail.dirx, tail.diry
 
        if dx == 1 and dy == 0:
            self._snake.append(New_dot((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self._snake.append(New_dot((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self._snake.append(New_dot((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self._snake.append(New_dot((tail.pos[0],tail.pos[1]+1)))
 
        self._snake[-1].dirx = dx
        self._snake[-1].diry = dy

    def drawing_snake(self, surface):
        for i, c in enumerate(self._snake):
            if i == 0:
                c.drawing_snake(surface, True)
            else:
                c.drawing_snake(surface)

# Creating grid
def drawGrid(width, rows,surface):
    sizeBtwn = width // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.drawing.line(surface, (255,255,255), (x, 0), (x, width))
        pygame.drawing.line(surface, (255,255,255), (0, y), (width, y))

# Updating grid
def redrawWindow(surface):
    global rows, width, snake_object, newDot
    surface.fill((0,0,0))
    snake_object.drawing(surface)
    newDot.drawing(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomnewDot(rows, items):
    positions = items._snake

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
    newDot = New_dot(randomnewDot(rows, snake_object), color = (0, 255, 0))
    flag = True 

    clock_game = pygame.time.Clock() # Defining variable related to the speed of the movement

    while flag:
        # Controlling the speed of movement
        pygame.time.delay(50)
        clock_game.tick(10)
        snake_object.move()
        if snake_object._snake[0].pos == newDot.pos:
            snake_object.adddot()
            newDot = New_dot(randomnewDot(rows, snake_object), color = (0, 255, 0))

        for x in range(len(snake_object._snake)):
            if snake_object._snake[x].pos in list(map(lambda z:z.pos,snake_object._snake[x+1:])):
                print('Score: ', len(snake_object._snake))
                message_box('You Lost!', 'Play again')
                snake_object.reset((10,10))
                break

        redrawWindow (win)

    pass    
    