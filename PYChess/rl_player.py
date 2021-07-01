import numpy as np
from linear_approximator import Linear
from copy import deepcopy
import random
import chess
import time
class rl_player:
    def __init__(self,dimension = 64*12):
        #dimension should say the size of linear approximator excluding the bias term.It is added inherently by the linear_approximator class 
        self.epsilon = 0.1
        self.alpha = 0.1
        try:
            param_init = np.load("param.npy")
            self.model = Linear(dimension,self.alpha,param_init)
        except:
            self.model = Linear(dimension,self.alpha)
        self.rng = np.random.default_rng()
        self.one_hot_coding = {
            0:(chess.PAWN,chess.WHITE),
            1:(chess.ROOK,chess.WHITE),
            2:(chess.KNIGHT,chess.WHITE),
            3:(chess.BISHOP,chess.WHITE),
            4:(chess.KING,chess.WHITE),
            5:(chess.QUEEN,chess.WHITE),
            6:(chess.PAWN,chess.BLACK),
            7:(chess.ROOK,chess.BLACK),
            8:(chess.KNIGHT,chess.BLACK),
            9:(chess.BISHOP,chess.BLACK),
            10:(chess.KING,chess.BLACK),
            11:(chess.QUEEN,chess.BLACK),
        }

    def evaluate_board_lookahead(self,board,depth,alpha,beta):
        #This is supposed to return a tuple of the position value and the best move at that place
        legal_moves = [str(move) for move in board.legal_moves]
        np.random.shuffle(legal_moves)
        score = None
        #need to check for empty legal_moves
        if len(legal_moves) == 0:
            outcome = board.outcome(claim_draw = True)
            assert(outcome is not None)
            if outcome.winner == None:
                score = 0
            elif outcome.winner == chess.WHITE:
                score = -1
            else:
                assert(outcome.winner == chess.BLACK)
                score = 1
            return (score,None)
        if depth ==0:
            return (self.evaluate(board),None)
        else:
            current_turn = board.turn
            score = None
            best_move = None
            for move in legal_moves:
                board.push_san(move)
                (child_val,_) = self.evaluate_board_lookahead(board,depth-1,alpha,beta)
                if score == None :
                    score = child_val
                    best_move = move
                else:
                    if current_turn == chess.WHITE:
                        if child_val < score:
                            best_move = move
                            score = min(score,child_val)
                    else:
                        assert(current_turn == chess.BLACK)
                        if child_val > score:
                            best_move = move
                            score = max(score,child_val)
                board.pop()
                
                #heres the pruning part and alpha,beta updating part
                
                if current_turn == chess.WHITE:
                    beta = min(beta,child_val)
                else:
                    alpha = max(alpha,child_val)
                
                if beta <= alpha:
                    break

            self.update_by_est_value(board,score)
            return (score,best_move)

    def get_move_lookahead(self,board,search_depth = 5):
        if board.turn == chess.WHITE:
            print("white's turn now")
        else:
            print("black's turn now")
        np.save("param.npy",self.model.param)
        rand_num = self.rng.random()
        if rand_num <self.epsilon:
            legal_moves = [str(move) for move in board.legal_moves]
            np.random.shuffle(legal_moves)
            return legal_moves[0]
        alpha = -1*(10**18)
        beta = 10**18
        res = self.evaluate_board_lookahead(deepcopy(board),search_depth,alpha,beta)
        print(res[0])
        return res[1]

    
    def board_to_vec(self,board):
        ls = [0 for i in range(64*12)]

        for cell_num in range(64):
            for one_hot_index in range(12):
                piece_type,col = self.one_hot_coding[one_hot_index]
                if board.piece_type_at(cell_num) == piece_type and board.color_at(cell_num) == col:
                    ls[cell_num*12+one_hot_index] = 1
                else:
                    ls[cell_num*12+one_hot_index] = 0
        return ls
        # ls = [0 for i in range(64)]
        # for cell_num in range(64):
        #     if board.piece_type_at(cell_num) == None:
        #         ls[cell_num] = 0
        #     elif board.piece_type_at(cell_num) == chess.PAWN:
        #         ls[cell_num] = 1
        #     elif board.piece_type_at(cell_num) == chess.ROOK:
        #         ls[cell_num] = 5
        #     elif board.piece_type_at(cell_num) == chess.KNIGHT:
        #         ls[cell_num] = 3
        #     elif board.piece_type_at(cell_num) == chess.BISHOP:
        #         ls[cell_num] = 3
        #     elif board.piece_type_at(cell_num) == chess.QUEEN:
        #         ls[cell_num] = 9
        #     elif board.piece_type_at(cell_num) == chess.KING:
        #         ls[cell_num] = 2
        #     else:
        #         print(board.piece_type_at(cell_num))
        #         assert(False)
        #     if board.color_at(cell_num) == chess.WHITE:
        #         ls[cell_num] *= -1
        # return ls[:]
    def evaluate(self,board):
        return self.model.get_val(self.board_to_vec(board))
        
    def update_by_reward(self,reward,old_board,new_board):
        old_vec = self.board_to_vec(old_board)
        new_vec = self.board_to_vec(new_board)
        est_value = reward + self.model.get_val(new_vec)
        self.model.upd_param(est_value,old_vec)
        return 
    def update_by_est_value(self,board,est_value):
        # print(est_value)
        self.model.upd_param(est_value,self.board_to_vec(board))
        # time.sleep(0.01)
        return

    # def get_move(self,board_config,current_move):
    #     np.save("param",self.model.param)
    #     all_moves = self.get_all_moves(board_config,current_move)
    #     start,end = self.select_move(board_config,all_moves,current_move)
    #     return (start,end)
    # def get_all_moves(self,board_config,current_move):
    #     all_moves = []
    #     for i in range(8):
    #         for j in range(8):
    #             if board_config[i][j][-5:] == current_move :
    #                 moves = rules.get_moves_improved(board_config,i,j)        
    #                 for move in moves:
    #                     all_moves.append([(i,j),tuple(move)])
    #     return all_moves
    # def select_move(self,board_config,all_moves,current_move):
    #     #if opposite color king is there in you possible moves immediately kill it
    #     req_col = "white" if current_move == "black" else "black"
    #     for move in all_moves:
    #         if board_config[move[1][0]][move[1][1]] == f"king_{req_col}":
    #             return move

    #     rand_num = np.random.random()
    #     if rand_num < self.epsilon:
    #         return all_moves[np.random.randint(0,len(all_moves))]
    #     else:
    #         #1)need to pick the greedy action
    #             #the greedy action will again depend on the moving person
    #         #2)improve policy based on that
    #         evaluations = []
    #         for move in all_moves:
    #             board_vec = rules.board_to_vec(board_config,move[0],move[1])
    #             # print("ha",board_vec)
    #             evaluations.append(self.model.get_val(board_vec))
    #         evaluations = np.array(evaluations)
    #         # print(self.model.param)
    #         if current_move == "white":
    #             # print(np.random.choice(np.flatnonzero(evaluations == np.max(evaluations))))
    #             return all_moves[np.random.choice(np.flatnonzero(evaluations == np.max(evaluations)))]
    #         else:
    #             # print(np.random.choice(np.flatnonzero(evaluations == np.min(evaluations))))
    #             return all_moves[np.random.choice(np.flatnonzero(np.isclose(evaluations, np.min(evaluations))))]
    # def update(self,reward,old_config,new_config):
    #     old_config_vec = rules.get_vec(old_config)
    #     new_config_vec = rules.get_vec(new_config)
    #     est_value = reward + self.model.get_val(new_config_vec)
    #     # print(old_config_vec)
    #     # print(new_config_vec)
    #     # print(est_value)
    #     self.model.upd_param(est_value,old_config_vec)

