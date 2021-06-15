import pygame
from Cell import Cell
class Board:
    def __init__(self,screen,cell_w,cell_h):
        #number of cells is 64
        self.screen = screen
        self.image_path = {}
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
            self.image_path[piece] = f"images/{piece}.png"

        return

    def get_image(self,row,col):
        try:
            return self.image_path[self.board_config[row][col]]
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
    
        