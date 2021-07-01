import sys
import time
from copy import deepcopy
import pygame
import chess_board
from pygame import display
from pygame.constants import K_ESCAPE
from rl_player import rl_player

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1100,800)) ## returns a surface called screen
screen.fill([163, 217, 185])
cell_w = cell_h = 800//8
board = chess_board.Board(screen,cell_w,cell_h,"white")
player = rl_player()

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
                print(str(board.board))
            else:
                print("please use left mouse key to select your piece to move.To cancel the selected piece click 'esc' key")
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                board.handle_escape()

    pygame.display.update()
    ans=player.get_move_lookahead(deepcopy(board.board))
    print(ans)
    # start_pos = board.get_row_col(ans[:2])
    # end_pos = board.get_row_col(ans[2:])
    old_board = deepcopy(board.board)
    board.handle_move_string(ans)
    # old_config = copy.deepcopy(board.board_config)
    # board.handle_mouse(start_pos[0],start_pos[1])
    pygame.display.update()
    # time.sleep(0.1)
    # board.handle_mouse(end_pos[0],end_pos[1])
    new_board = deepcopy(board.board)
    pygame.display.update()
    # time.sleep(0.1)
    player.update_by_reward(board.get_reward(),old_board,new_board)
    if board.is_game_over():
        board.print_winner()
        del board
        board = chess_board.Board(screen,cell_w,cell_h,"white")



    # new_config = board.board_config
    # winner = board.get_winner()
    # game_over = False
    # if winner == "noone":
    #     player.update(0,old_config,new_config)
    # elif winner == "black":
    #     player.update(1,old_config,new_config)
    #     print("black has won")
    #     game_over = True
    # else:
    #     print(winner)
    #     player.update(-1,old_config,new_config)
    #     print("white has won")
    #     game_over = True
    # time.sleep(0.1)
    # if game_over:
    #     del board
    #     board = chess_board.Board(screen,cell_w,cell_h,"white")
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

