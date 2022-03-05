
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
    