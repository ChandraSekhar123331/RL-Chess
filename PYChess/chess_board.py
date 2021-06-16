import pygame
from Cell import Cell
class Board:
    def __init__(self,screen,cell_w,cell_h,current_move):
        #number of cells is 64
        self.current_move = current_move
        self.is_selected = False
        self.selected_piece = None
        self.movable_posns = []
        self.screen = screen
        self.image_paths = {}
        self.board_config = [["" for col in range(8)] for row in range(8)]
        self.cells = [[Cell(screen,[col*cell_w,row*cell_h],[int(cell_w),int(cell_h)]) for col in range(8)] for row in range(8)]
        self.image_map_init()
        self.board_init()
        self.image_render(black = [242, 156, 63],white = [255, 255, 255])

    def image_map_init(self):
        pieces = [
            "knight_white",
            "knight_black",
            "rook_white",
            "rook_black",
            "bishop_white",
            "bishop_black",
            "king_white",
            "king_black",
            "queen_white",
            "queen_black",
            "pawn_white",
            "pawn_black",
        ]
        for piece in pieces:
            self.image_paths[piece] = f"images/{piece}.png"

        return

    def get_image(self,row,col):
        try:
            return self.image_paths[self.board_config[row][col]]
        except:
            return ""

    def image_render(self,black,white):
        ##filling colors
        for i in range(8):
            for j in range(8):
                if(i%2 == j%2):
                    self.cells[i][j].fill_color(white)
                else:
                    self.cells[i][j].fill_color(black)
        
        #rendering images
        for i in range(8):
            for j in range(8):
                self.cells[i][j].render(self.get_image(i,j))
        

    def board_init(self):
        self.board_config[0] = [
            "rook_black",
            "knight_black",
            "bishop_black",
            "queen_black",
            "king_black",
            "bishop_black",
            "knight_black",
            "rook_black",
        ]
        self.board_config[7] = [
            "rook_white",
            "knight_white",
            "bishop_white",
            "queen_white",
            "king_white",
            "bishop_white",
            "knight_white",
            "rook_white",
        ]
        self.board_config[1] = [
            "pawn_black",
            "pawn_black",
            "pawn_black",
            "pawn_black",
            "pawn_black",
            "pawn_black",
            "pawn_black",
            "pawn_black",
        ]
        self.board_config[6] = [
            "pawn_white",
            "pawn_white",
            "pawn_white",
            "pawn_white",
            "pawn_white",
            "pawn_white",
            "pawn_white",
            "pawn_white",
        ]

        return
    
    def handle_mouse(self,cell_row,cell_col):
        if self.is_selected:
            self.handle_mouse_selected(cell_row,cell_col)
        else:
            self.handle_mouse_not_selected(cell_row,cell_col)
        # print(self.board_config)
    def handle_mouse_selected(self,cell_row,cell_col):
        if [cell_row,cell_col] in self.movable_posns:
            self.reset_move_posns()
            self.cells[cell_row][cell_col].get_piece(self.cells[self.selected_piece[0]][self.selected_piece[1]])
            self.current_move = "black" if (self.current_move == "white") else "white"
            self.is_selected = False
            self.movable_posns = []
            self.handle_board_config(cell_row,cell_col)
            self.selected_piece = None
        else:
            print("please click on the highlighted boxes to move or click esc to cancel the selected piece")
        
    def handle_mouse_not_selected(self,cell_row,cell_col):
        # print(cell_col,cell_row)
        piece = self.board_config[cell_row][cell_col]
        if piece == "":
            print("There is no piece at selected location")
            return
        elif piece[-5:] != self.current_move:
            print(f"you have to move {self.current_move} piece")
            return
        # self.is_selected = True ##this line is to be done only if movable positions is non_empty
        piece_name = piece[:-6]
        if piece_name == "pawn":
            self.move_pawn(cell_row,cell_col)
        elif piece_name == "rook":
            self.move_rook(cell_row,cell_col)
        elif piece_name == "knight":
            self.move_knight(cell_row,cell_col)
        elif piece_name == "bishop":
            self.move_bishop(cell_row,cell_col)
        elif piece_name == "queen":
            self.move_queen(cell_row,cell_col)
        elif piece_name == "king":
            self.move_king(cell_row,cell_col)
        else:
            assert(False)
        print(self.movable_posns)

        if len(self.movable_posns) == 0:
            print("The selected piece has no possibility to move")
            return
        self.is_selected = True
        self.selected_piece = [cell_row,cell_col]
        self.render_move_posns()
        ##Okay so we need to handle the case on is_selected as well
        return
    def handle_escape(self):
        self.reset_move_posns()
        self.movable_posns = []
        self.is_selected = False
        print("escape key was selected")
        
    def move_pawn(self,cell_row,cell_col):
        if self.current_move == "white":
            if cell_row == 6:
                for row_inc in [-1,-2]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col 
                    if self.valid_cell(fin_row,fin_col):
                        occ = self.occupied(fin_row,fin_col)
                        # enemy_occ= self.has_enemy(fin_row,fin_col)
                        if not occ:
                            self.movable_posns.append([fin_row,fin_col])
                        else:
                            break
            else:
                for row_inc in [-1]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col 
                    if self.valid_cell(fin_row,fin_col):
                        occ = self.occupied(fin_row,fin_col)
                        # enemy_occ= self.has_enemy(fin_row,fin_col)
                        if not occ:
                            self.movable_posns.append([fin_row,fin_col])
                        else:
                            break
            
            for row_inc in [-1]:
                for col_inc in [+1,-1]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col + col_inc
                    if self.valid_cell(fin_row,fin_col):
                        if self.has_enemy(fin_row,fin_col):
                            self.movable_posns.append([fin_row,fin_col])

            
        else:
            assert(self.current_move == "black")
            if cell_row == 1:
                for row_inc in [1,2]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col 
                    if self.valid_cell(fin_row,fin_col):
                        occ = self.occupied(fin_row,fin_col)
                        # enemy_occ= self.has_enemy(fin_row,fin_col)
                        if not occ:
                            self.movable_posns.append([fin_row,fin_col])
                        else:
                            break
            else:
                for row_inc in [1]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col 
                    if self.valid_cell(fin_row,fin_col):
                        occ = self.occupied(fin_row,fin_col)
                        # enemy_occ= self.has_enemy(fin_row,fin_col)
                        if not occ:
                            self.movable_posns.append([fin_row,fin_col])
                        else:
                            break
            for row_inc in [+1]:
                for col_inc in [+1,-1]:
                    fin_row = cell_row + row_inc
                    fin_col = cell_col + col_inc
                    if self.valid_cell(fin_row,fin_col):
                        if self.has_enemy(fin_row,fin_col):
                            self.movable_posns.append([fin_row,fin_col])                
    def move_rook(self,cell_row,cell_col):
        for row_inc in range(1,8):
            col_inc = 0
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if self.occupied(fin_row,fin_col):
                    if(self.has_enemy(fin_row,fin_col)):
                        self.movable_posns.append([fin_row,fin_col])
                    break
                else:
                    self.movable_posns.append([fin_row,fin_col])
        for row_inc in range(-1,-8,-1):
            col_inc = 0
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if self.occupied(fin_row,fin_col):
                    if(self.has_enemy(fin_row,fin_col)):
                        self.movable_posns.append([fin_row,fin_col])
                    break
                else:
                    self.movable_posns.append([fin_row,fin_col])

        for col_inc in range(1,8):
            row_inc = 0
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if self.occupied(fin_row,fin_col):
                    if(self.has_enemy(fin_row,fin_col)):
                        self.movable_posns.append([fin_row,fin_col])
                    break
                else:
                    self.movable_posns.append([fin_row,fin_col])
        for col_inc in range(-1,-8,-1):
            row_inc = 0
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if self.occupied(fin_row,fin_col):
                    if(self.has_enemy(fin_row,fin_col)):
                        self.movable_posns.append([fin_row,fin_col])
                    break
                else:
                    self.movable_posns.append([fin_row,fin_col])
    def move_knight(self,cell_row,cell_col):
        for row_inc in [-1,+1]:
            for col_inc in [-2,+2]:
                fin_row = cell_row + row_inc
                fin_col = cell_col + col_inc
                if self.valid_cell(fin_row,fin_col):
                    if not self.occupied(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                        continue
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])

        for row_inc in [-2,+2]:
            for col_inc in [-1,+1]:
                fin_row = cell_row + row_inc
                fin_col = cell_col + col_inc
                if self.valid_cell(fin_row,fin_col):
                    if not self.occupied(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                        continue
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
    def move_bishop(self,cell_row,cell_col):
        for inc in range(1,8):
            row_inc = col_inc = inc
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if not self.occupied(fin_row,fin_col):
                    self.movable_posns.append([fin_row,fin_col])
                else:
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                    break

        for inc in range(-1,-8,-1):
            row_inc = col_inc = inc
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if not self.occupied(fin_row,fin_col):
                    self.movable_posns.append([fin_row,fin_col])
                else:
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                    break
                
        for inc in range(1,8):
            row_inc = inc
            col_inc = -inc
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if not self.occupied(fin_row,fin_col):
                    self.movable_posns.append([fin_row,fin_col])
                else:
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                    break

        for inc in range(-1,-8,-1):
            row_inc = inc
            col_inc = -inc
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if self.valid_cell(fin_row,fin_col):
                if not self.occupied(fin_row,fin_col):
                    self.movable_posns.append([fin_row,fin_col])
                else:
                    if self.has_enemy(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                    break
    def move_queen(self,cell_row,cell_col):
        self.move_bishop(cell_row,cell_col)
        self.move_rook(cell_row,cell_col)
    def move_king(self,cell_row,cell_col):
        for row_inc in [-1,0,1]:
            for col_inc in [-1,0,1]:
                if row_inc == 0 and col_inc == 0:
                    continue
                fin_row = cell_row + row_inc
                fin_col = cell_col + col_inc
                if self.valid_cell(fin_row,fin_col):
                    if not self.occupied(fin_row,fin_col):
                        self.movable_posns.append([fin_row,fin_col])
                    else:
                        if self.has_enemy(fin_row,fin_col):
                            self.movable_posns.append([fin_row,fin_col])

    def valid_cell(self,row,col):
        return 0<=row<=7 and 0<=col<=7
    
    def occupied(self,row,col):
        return self.board_config[row][col] != ""
    
    def has_enemy(self,row,col):
        if not self.occupied(row,col):
            return False
        return self.board_config[row][col][-5:] != self.current_move 
    def render_move_posns(self):
        for row,col in self.movable_posns:
            if self.has_enemy(row,col):
                self.cells[row][col].highlight_enemy()
            else:
                self.cells[row][col].highlight_free()

    def reset_move_posns(self):
        for row,col in self.movable_posns:
            self.cells[row][col].reset()
    def handle_board_config(self,cell_row,cell_col):
        #this is to maintain the board config after moving the selected piece to [cell_row,cell_col]
        self.board_config[cell_row][cell_col] = self.board_config[self.selected_piece[0]][self.selected_piece[1]]
        self.board_config[self.selected_piece[0]][self.selected_piece[1]] = ""