
import pygame 

class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def movement(self, dirnx, dirny):
        pass

    def drawing(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        for key in keys:
            if keys [pygame.K_LEFT] :
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]        

            elif keys [pygame.K_RIGHT] :
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]    

            elif keys [pygame.K_UP] :
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys [pygame.K_DOWN] :
                self.dirnx = 0
                self.dirny = 1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Random movement of new cube
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn [0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)  

            else:
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)

# Creating grid
def drawGrid(w, rows,surface):
    sizeBtwn = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0), (x, w))
        pygame.draw.line(surface, (255,255,255), (0, y), (w, y))

# Updating grid
def redrawWindow(surface):
    global rows, width
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()

# Main loop of the game
def main():
    global width, rows
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, width)) # Defining display
    snake = snake((255, 0, 0), (10, 10)) # Creating snake object
    flag = True 

    clock_game = pygame.time.Clock() # Defining variable related to the speed of the movement

    while flag:
        # Controlling the speed of movement
        pygame.time.delay(50)
        clock_game.tick(10)

        redrawWindow (win)

    pass    
    