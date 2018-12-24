import numpy as np

class Dot:
    def __init__(self, x_pos=0, y_pos=0):
        self.pos = np.array([float(x_pos), float(y_pos)])
        self.last_v = np.array([0.0, 0.0])
        self.score = 0
        self.num_moves = 0

    # v is a 2d velocity vector
    def move(self, v, movement_size):
        self.last_v = v/np.linalg.norm(v) * movement_size
        self.pos += self.last_v
        self.num_moves += 1

    # calculate fitness score
    def set_score(self, goal_pos):
        if np.linalg.norm(self.pos - goal_pos) < 1:
            self.score = 10 + 1/(self.num_moves*self.num_moves)
        else:
            self.score = 1/np.linalg.norm(self.pos-goal_pos)