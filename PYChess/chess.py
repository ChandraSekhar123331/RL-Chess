import pygame
import sys

from pygame import display
from rl_player import rl_player
import time
from pygame.constants import K_ESCAPE
import copy
# import random
import chess_board
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1100,800)) ## returns a surface called screen
screen.fill([163, 217, 185])
cell_w = cell_h = 800//8
board = chess_board.Board(screen,cell_w,cell_h,"white")
player = rl_player(64)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_processes = pygame.mouse.get_pressed()
            if mouse_processes[0]:
                print("Left Mouse Key was clicked")
                x, y = pygame.mouse.get_pos()
                cell_col = x//cell_w
                cell_row = y//cell_h
                board.handle_mouse(cell_row,cell_col)
            else:
                print("please use left mouse key to select your piece to move.To cancel the selected piece click 'esc' key")
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                board.handle_escape()

    ans=player.get_move(board.board_config,board.current_move)
    old_config = copy.deepcopy(board.board_config)
    board.handle_mouse(ans[0][0],ans[0][1])
    pygame.display.update()
    time.sleep(0.1)
    board.handle_mouse(ans[1][0],ans[1][1])
    pygame.display.update()
    new_config = board.board_config
    winner = board.get_winner()
    game_over = False
    if winner == "noone":
        player.update(0,old_config,new_config)
    elif winner == "black":
        player.update(1,old_config,new_config)
        print("black has won")
        game_over = True
    else:
        print(winner)
        player.update(-1,old_config,new_config)
        print("white has won")
        game_over = True
    time.sleep(0.1)
    if game_over:
        del board
        board = chess_board.Board(screen,cell_w,cell_h,"white")
    pygame.display.update()

    
    # left, middle, right = pygame.mouse.get_pressed()
    # if left:
    #     print('left_key_pressed')
    # if right:
    #     print('right_key_pressed')
    # if middle:
    #     print('middle_key_pressed')
    # screen.fill([150,120,100]) #order matters
    # pygame.draw.circle(screen,(0,0,255),(850,500),55) #order matters
    # clock.tick(20)
    # pygame.display.update() #updates display

