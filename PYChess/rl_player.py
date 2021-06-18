import numpy as np
import rules
from linear_approximator import Linear
class rl_player:
    def __init__(self,dimension):
        #dimension should say the size of linear approximator excluding the bias term.It is added inherently by the linear_approximator class 
        self.epsilon = 0.1
        self.alpha = 0.01
        try:
            param_init = np.load("param.npy")
            self.model = Linear(dimension,self.alpha,param_init)
        except:
            self.model = Linear(dimension,self.alpha)
        self.rng = np.random.default_rng()

    def get_move(self,board_config,current_move):
        np.save("param",self.model.param)
        all_moves = self.get_all_moves(board_config,current_move)
        start,end = self.select_move(board_config,all_moves,current_move)
        return (start,end)
    def get_all_moves(self,board_config,current_move):
        all_moves = []
        for i in range(8):
            for j in range(8):
                if board_config[i][j][-5:] == current_move :
                    moves = rules.get_moves_improved(board_config,i,j)        
                    for move in moves:
                        all_moves.append([(i,j),tuple(move)])
        return all_moves
    def select_move(self,board_config,all_moves,current_move):
        #if opposite color king is there in you possible moves immediately kill it
        req_col = "white" if current_move == "black" else "black"
        for move in all_moves:
            if board_config[move[1][0]][move[1][1]] == f"king_{req_col}":
                return move

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
            # print(self.model.param)
            if current_move == "white":
                # print(np.random.choice(np.flatnonzero(evaluations == np.max(evaluations))))
                return all_moves[np.random.choice(np.flatnonzero(evaluations == np.max(evaluations)))]
            else:
                # print(np.random.choice(np.flatnonzero(evaluations == np.min(evaluations))))
                return all_moves[np.random.choice(np.flatnonzero(np.isclose(evaluations, np.min(evaluations))))]
    def update(self,reward,old_config,new_config):
        old_config_vec = rules.get_vec(old_config)
        new_config_vec = rules.get_vec(new_config)
        est_value = reward + self.model.get_val(new_config_vec)
        # print(old_config_vec)
        # print(new_config_vec)
        # print(est_value)
        self.model.upd_param(est_value,old_config_vec)

