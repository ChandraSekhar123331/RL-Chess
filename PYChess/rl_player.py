import numpy as np
import rules
from linear_approximator import Linear
class rl_player:
    def __init__(self,dimension):
        #dimension should say the size of linear approximator excluding the bias term.It is added inherently by the linear_approximator class 
        self.epsilon = 0.1
        self.alpha = 0.01
        self.model = Linear(dimension,self.alpha)
        self.rng = np.random.default_rng()

    def get_move(self,board_config,current_move):
        all_moves = self.get_all_moves(board_config,current_move)
        start,end = self.select_move(board_config,all_moves,current_move)
        return (start,end)
    def get_all_moves(self,board_config,current_move):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if board_config[i][j][-5:] == current_move :
                    moves = rules.get_moves(board_config,i,j)        
                    for move in moves:
                        all_moves.append([(i,j),tuple(move)])
        return all_moves
    def select_move(self,board_config,all_moves,current_move):
        rand_num = np.random.random()
        if rand_num < self.epsilon:
            return all_moves[np.random.randint(0,len(all_moves))]
        else:
            #1)need to pick the greedy action
                #the greedy action will again depend on the moving person
            #2)improve policy based on that
            evaluations = []
            for move in all_moves:
                board_vec = rules.board_to_vec(board_config,move[0],move[1])
                # print("ha",board_vec)
                evaluations.append(self.model.get_val(board_vec))
            evaluations = np.array(evaluations)
            if current_move == "white":
                # print(np.random.choice(np.flatnonzero(evaluations == np.max(evaluations))))
                return all_moves[np.random.choice(np.flatnonzero(evaluations == np.max(evaluations)))]
            else:
                # print(np.random.choice(np.flatnonzero(evaluations == np.min(evaluations))))
                return all_moves[np.random.choice(np.flatnonzero(evaluations == np.min(evaluations)))]
