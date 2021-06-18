def move_pawn(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    if current_move == "white":
        if cell_row == 6:
            for row_inc in [-1,-2]:
                fin_row = cell_row + row_inc
                fin_col = cell_col 
                if valid_cell(fin_row,fin_col):
                    occ = occupied(board_config,fin_row,fin_col)
                    # enemy_occ= has_enemy(board_config,fin_row,fin_col,current_move)
                    if not occ:
                        movable_posns.append([fin_row,fin_col])
                    else:
                        break
        else:
            for row_inc in [-1]:
                fin_row = cell_row + row_inc
                fin_col = cell_col 
                if valid_cell(fin_row,fin_col):
                    occ = occupied(board_config,fin_row,fin_col)
                    # enemy_occ= has_enemy(board_config,fin_row,fin_col,current_move)
                    if not occ:
                        movable_posns.append([fin_row,fin_col])
                    else:
                        break
        
        for row_inc in [-1]:
            for col_inc in [+1,-1]:
                fin_row = cell_row + row_inc
                fin_col = cell_col + col_inc
                if valid_cell(fin_row,fin_col):
                    if has_enemy(board_config,fin_row,fin_col,current_move):
                        movable_posns.append([fin_row,fin_col])

        
    else:
        assert(current_move == "black")
        if cell_row == 1:
            for row_inc in [1,2]:
                fin_row = cell_row + row_inc
                fin_col = cell_col 
                if valid_cell(fin_row,fin_col):
                    occ = occupied(board_config,fin_row,fin_col)
                    # enemy_occ= has_enemy(board_config,fin_row,fin_col,current_move)
                    if not occ:
                        movable_posns.append([fin_row,fin_col])
                    else:
                        break
        else:
            for row_inc in [1]:
                fin_row = cell_row + row_inc
                fin_col = cell_col 
                if valid_cell(fin_row,fin_col):
                    occ = occupied(board_config,fin_row,fin_col)
                    # enemy_occ= has_enemy(board_config,fin_row,fin_col,current_move)
                    if not occ:
                        movable_posns.append([fin_row,fin_col])
                    else:
                        break
        for row_inc in [+1]:
            for col_inc in [+1,-1]:
                fin_row = cell_row + row_inc
                fin_col = cell_col + col_inc
                if valid_cell(fin_row,fin_col):
                    if has_enemy(board_config,fin_row,fin_col,current_move):
                        movable_posns.append([fin_row,fin_col])   

    return movable_posns             

def move_rook(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    for row_inc in range(1,8):
        col_inc = 0
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if occupied(board_config,fin_row,fin_col):
                if(has_enemy(board_config,fin_row,fin_col,current_move)):
                    movable_posns.append([fin_row,fin_col])
                break
            else:
                movable_posns.append([fin_row,fin_col])
    for row_inc in range(-1,-8,-1):
        col_inc = 0
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if occupied(board_config,fin_row,fin_col):
                if(has_enemy(board_config,fin_row,fin_col,current_move)):
                    movable_posns.append([fin_row,fin_col])
                break
            else:
                movable_posns.append([fin_row,fin_col])

    for col_inc in range(1,8):
        row_inc = 0
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if occupied(board_config,fin_row,fin_col):
                if(has_enemy(board_config,fin_row,fin_col,current_move)):
                    movable_posns.append([fin_row,fin_col])
                break
            else:
                movable_posns.append([fin_row,fin_col])
    for col_inc in range(-1,-8,-1):
        row_inc = 0
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if occupied(board_config,fin_row,fin_col):
                if(has_enemy(board_config,fin_row,fin_col,current_move)):
                    movable_posns.append([fin_row,fin_col])
                break
            else:
                movable_posns.append([fin_row,fin_col])
    return movable_posns

def move_knight(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    for row_inc in [-1,+1]:
        for col_inc in [-2,+2]:
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if valid_cell(fin_row,fin_col):
                if not occupied(board_config,fin_row,fin_col):
                    movable_posns.append([fin_row,fin_col])
                    continue
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])

    for row_inc in [-2,+2]:
        for col_inc in [-1,+1]:
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if valid_cell(fin_row,fin_col):
                if not occupied(board_config,fin_row,fin_col):
                    movable_posns.append([fin_row,fin_col])
                    continue
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])
    return movable_posns

def move_bishop(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    for inc in range(1,8):
        row_inc = col_inc = inc
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if not occupied(board_config,fin_row,fin_col):
                movable_posns.append([fin_row,fin_col])
            else:
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])
                break

    for inc in range(-1,-8,-1):
        row_inc = col_inc = inc
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if not occupied(board_config,fin_row,fin_col):
                movable_posns.append([fin_row,fin_col])
            else:
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])
                break
            
    for inc in range(1,8):
        row_inc = inc
        col_inc = -inc
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if not occupied(board_config,fin_row,fin_col):
                movable_posns.append([fin_row,fin_col])
            else:
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])
                break

    for inc in range(-1,-8,-1):
        row_inc = inc
        col_inc = -inc
        fin_row = cell_row + row_inc
        fin_col = cell_col + col_inc
        if valid_cell(fin_row,fin_col):
            if not occupied(board_config,fin_row,fin_col):
                movable_posns.append([fin_row,fin_col])
            else:
                if has_enemy(board_config,fin_row,fin_col,current_move):
                    movable_posns.append([fin_row,fin_col])
                break
    return movable_posns
def move_queen(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    movable_posns.extend(move_bishop(board_config,cell_row,cell_col))
    movable_posns.extend(move_rook(board_config,cell_row,cell_col))
    return movable_posns
def move_king(board_config,cell_row,cell_col):
    current_move = board_config[cell_row][cell_col][-5:]
    movable_posns = []
    for row_inc in [-1,0,1]:
        for col_inc in [-1,0,1]:
            if row_inc == 0 and col_inc == 0:
                continue
            fin_row = cell_row + row_inc
            fin_col = cell_col + col_inc
            if valid_cell(fin_row,fin_col):
                if not occupied(board_config,fin_row,fin_col):
                    movable_posns.append([fin_row,fin_col])
                else:
                    if has_enemy(board_config,fin_row,fin_col,current_move):
                        movable_posns.append([fin_row,fin_col])
    return movable_posns

def valid_cell(row,col):
    return 0<=row<=7 and 0<=col<=7

def occupied(board_config,row,col):
    return board_config[row][col] != ""

def has_enemy(board_config,row,col,current_move):
    if not occupied(board_config,row,col):
        return False
    return board_config[row][col][-5:] != current_move 
# def get_danger_pos(board_config,current_move):
    #says about danger positions for the current_move person

def get_moves(board_config,row,col):
    if board_config[row][col][:-6] == "pawn":
        return move_pawn(board_config,row,col)
    if board_config[row][col][:-6] == "rook":
        return move_rook(board_config,row,col)
    if board_config[row][col][:-6] == "knight":
        return move_knight(board_config,row,col)
    if board_config[row][col][:-6] == "bishop":
        return move_bishop(board_config,row,col)
    if board_config[row][col][:-6] == "queen":
        return move_queen(board_config,row,col)
    if board_config[row][col][:-6] == "king":
        return move_king(board_config,row,col)
def board_to_vec(board_config,start,dest):
    vec = []
    for i in range(8):
        for j in range(8):
            if (i,j) == start:
                piece = ""
            elif (i,j) == dest:
                piece = board_config[start[0]][start[1]]
            else:
                piece = board_config[i][j]

            vec.append(assign_value(piece))
    return vec

def assign_value(piece):
    if piece == "":
        return 0
    piece = piece[:-6]
    if piece == "pawn":
        return 1
    if piece == "rook":
        return 5
    if piece == "knight":
        return 3
    if piece == "bishop":
        return 3
    if piece == "queen":
        return 9
    assert(piece == "king")
    return 2
    
    