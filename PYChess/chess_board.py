from re import T
from Cell import Cell
import chess
class Board:
    def __init__(self,screen,cell_w,cell_h,current_move):
        #number of cells is 64
        self.is_selected = False
        self.selected_piece = None
        self.possible_moves = []
        self.screen = screen
        self.image_paths = {}
        self.board = chess.Board()
        self.cells = [[Cell(screen,[col*cell_w,row*cell_h],[int(cell_w),int(cell_h)]) for col in range(8)] for row in range(8)]
        self.image_map_init()
        self.image_render(black = [242, 156, 63],white = [255, 255, 255])

    def who(player):
        return "White" if player == chess.WHITE else "Black"
    def get_cell_number(self,row,col):
        #since rows are zero indexed
        row+=1
        col+=1
        #since rows are from top to bottom in pygame and bottom to top in chess module
        return (9-row)*8 + col -9
    def get_row_col(self,posn):
        #posn is a string like a1
        #row,col tyuple is returned 
        # the row,col are in reference to usual matrix convention
        col = ord(posn[0])-ord('a')
        row = int(posn[1])
        return 8-row,col

    def image_map_init(self):
        self.image_paths = {
            "N":"images/knight_white.png",
            "R":"images/rook_white.png",
            "B":"images/bishop_white.png",
            "Q":"images/queen_white.png",
            "K":"images/king_white.png",
            "P":"images/pawn_white.png",
            "n":"images/knight_black.png",
            "r":"images/rook_black.png",
            "b":"images/bishop_black.png",
            "q":"images/queen_black.png",
            "k":"images/king_black.png",
            "p":"images/pawn_black.png",
        }
        return
    
    def get_image(self,row,col):
        try:
            return self.image_paths[str(self.board.piece_at(self.get_cell_number(row,col)))]
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
        

    # def board_init(self):
    #     self.board_config[0] = [
    #         "rook_black",
    #         "knight_black",
    #         "bishop_black",
    #         "queen_black",
    #         "king_black",
    #         "bishop_black",
    #         "knight_black",
    #         "rook_black",
    #     ]
    #     self.board_config[7] = [
    #         "rook_white",
    #         "knight_white",
    #         "bishop_white",
    #         "queen_white",
    #         "king_white",
    #         "bishop_white",
    #         "knight_white",
    #         "rook_white",
    #     ]
    #     self.board_config[1] = [
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #         "pawn_black",
    #     ]
    #     self.board_config[6] = [
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #         "pawn_white",
    #     ]
    #     return
    
    def handle_mouse(self,cell_row,cell_col):
        if self.is_selected:
            self.handle_mouse_selected(cell_row,cell_col)
        else:
            self.handle_mouse_not_selected(cell_row,cell_col)
        # print(self.board_config)

    def handle_mouse_selected(self,cell_row,cell_col):
        cell_num = self.get_cell_number(cell_row,cell_col)
        cell_name = chess.square_name(cell_num)
        start_cell_num = self.get_cell_number(self.selected_piece[0],self.selected_piece[1])
        start_cell_name = chess.square_name(start_cell_num)
        end_posns = [posn[2:] for posn in self.possible_moves]
        if cell_name in end_posns:
            self.reset_move_posns()
            self.cells[cell_row][cell_col].get_piece(self.cells[self.selected_piece[0]][self.selected_piece[1]])
            self.is_selected = False
            self.possible_moves = []
            self.board.push_san(start_cell_name+cell_name)
            self.cells[self.selected_piece[0]][self.selected_piece[1]].reset()
            self.selected_piece = None
        else:
            print("please click on the highlighted boxes to move or click esc to cancel the selected piece")
    
    
    def handle_mouse_not_selected(self,cell_row,cell_col):
        # print(cell_col,cell_row)
        clicked_cell_num = self.get_cell_number(cell_row,cell_col)
        clicked_cell_name = chess.square_name(clicked_cell_num)
        piece = self.board.piece_at(clicked_cell_num)
        piece_name = str(piece)
        if piece_name == None:
            print("There is no piece at selected location")
            return
        elif piece.color != self.board.turn:
            print(f"you have to move {self.who(self.board.turn)} piece")
            return
        # self.is_selected = True ##this line is to be done only if movable positions is non_empty
        self.possible_moves = [str(move) for move in self.board.legal_moves if str(move).startswith(clicked_cell_name)]
        print(self.possible_moves)

        if len(self.possible_moves) == 0:
            print("The selected piece has no possibility to move")
            return
        self.is_selected = True
        self.selected_piece = [cell_row,cell_col]
        self.render_move_posns()
        self.cells[cell_row][cell_col].show_as_selected()
        ##Okay so we need to handle the case on is_selected as well
        return
    # def handle_escape(self):
    #     self.reset_move_posns()
    #     self.movable_posns = []
    #     self.is_selected = False
    #     print("escape key was selected")
    def has_enemy(self,posn):
        print(posn)
        if self.board.piece_at(posn) == None:
            return False
        elif self.board.piece_at(posn).color is self.board.turn:
            return False
        else:
            return True

    def render_move_posns(self):
        end_posns = [posn[2:] for posn in self.possible_moves]
        for posn in end_posns:
            row, col = self.get_row_col(posn)
            if self.has_enemy(chess.parse_square(posn)):
                self.cells[row][col].highlight_enemy()
            else:
                self.cells[row][col].highlight_free()
            # print(posn)

    def reset_move_posns(self):
        end_posns = [posn[2:] for posn in self.possible_moves]
        for posn in end_posns:
            row,col = self.get_row_col(posn)
            self.cells[row][col].reset()
    # def handle_board_config(self,cell_row,cell_col):
    #     #this is to maintain the board config after moving the selected piece to [cell_row,cell_col]
    #     self.board_config[cell_row][cell_col] = self.board_config[self.selected_piece[0]][self.selected_piece[1]]
    #     self.board_config[self.selected_piece[0]][self.selected_piece[1]] = ""
    # def get_winner(self):
    #     black = False
    #     white = False
    #     for i in range(8):
    #         for j in range(8):
    #             if self.board_config[i][j][:-6]=="king":
    #                 if self.board_config[i][j][-5:] == "white":
    #                     white = True
    #                 else:
    #                     black = True

    #     if not black:
    #         return "white"
    #     if not white:
    #         return "black"
    #     return "noone"