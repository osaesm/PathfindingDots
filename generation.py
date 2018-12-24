import numpy as np
import dot as Dot
import random
import math
import copy

class Generation:
    def __init__(self, starting_pos, goal_pos, gen_size=50, movement_size=1, num_survivors=10):
        self.size = gen_size
        self.movement_size = movement_size
        self.dots = []
        self.starting_pos = starting_pos.copy()
        self.goal_pos = goal_pos.copy()
        self.x_move_stats = []
        self.y_move_stats = []
        self.best_num = num_survivors
        self.prev_bests = []
        for i in range(self.best_num):
            self.prev_bests.append(Dot.Dot(x_pos=starting_pos[0], y_pos=starting_pos[1]))
        for i in range(gen_size):
            self.dots.append(Dot.Dot(starting_pos[0], starting_pos[1]))

    def dot_score(self, dot):
        return dot.score

    def do_moves(self, dims):
        x_bound, y_bound = dims
        self.dots = self.prev_bests
        for i in range(self.size // self.best_num - 1):
            self.dots += [copy.deepcopy(dot) for dot in self.prev_bests]
        self.prev_bests = []

        for i in range(self.best_num, self.size):
            if self.dots[i].score > 10:
                return self.dots[i].num_moves
            if 0 <= self.dots[i].pos[0] <= x_bound and 0 <= self.dots[i].pos[1] <= y_bound:
                self.dots[i].move(np.random.randn(2), self.movement_size)
                self.dots[i].set_score(self.goal_pos, self.movement_size)
        self.dots.sort(reverse=True, key=self.dot_score)
        self.prev_bests = self.dots[:self.best_num]
