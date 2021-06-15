import pygame
import sys
# import random
import chess_board
pygame.init()
screen = pygame.display.set_mode((1100,800)) ## returns a surface called screen
screen.fill([163, 217, 185])
cell_w = cell_h = 800/8
Board = chess_board.Board(screen,cell_w,cell_h)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill([150,120,100]) #order matters
    # pygame.draw.circle(screen,(0,0,255),(850,500),55) #order matters
    pygame.display.update() #updates display

