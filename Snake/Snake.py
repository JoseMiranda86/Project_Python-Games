
import pygame 

class dot(object):
    rows = 0
    w =0

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def movement(self, dirnx, dirny):
        pass

    def drawing(self, surface, eyes=False):
        pass

class snake(object):
    def __init__(self, color, pos):
        pass

    def movement(self):
        pass

# Main loop of the game
def main():
    Width = 500
    Height = 500
    Rows = 20

    Window = pygame.display.set_mode((Width, Height)) # Defining display
    Snake = snake((255, 255, 255), (10, 10)) # Creating snake object
    Flag = True 

    Clock_game = pygame.time.Clock() # Defining variable related to the speed of the movement

    