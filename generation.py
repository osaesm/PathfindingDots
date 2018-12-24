import numpy as np
import dot as Dot
import random
import math

class Generation:
    def __init__(self, starting_pos, goal_pos, gen_size=50, movement_size=1):
        self.size = gen_size
        self.movement_size = movement_size
        self.dots = []
        self.starting_pos = starting_pos.copy()
        self.goal_pos = goal_pos.copy()
        self.shortest_success = float('inf')
        self.x_move_stats = []
        self.y_move_stats = []
        for i in range(gen_size):
            self.dots.append(Dot.Dot(starting_pos[0], starting_pos[1]))

    def calculate_random_vector(self, stats_vec):
        mean, stdev = stats_vec
        return np.random.randn() * stdev + mean

    def do_moves(self, dims):
        x_bound, y_bound = dims
        total_scores = 0
        self.shortest_success = float('inf')
        for i in range(self.size):
            if self.dots[i].score < 10:
                self.dots[i] = Dot.Dot(self.starting_pos[0], self.starting_pos[1])
                for j in range(min(len(self.x_move_stats), self.shortest_success)):
                    self.dots[i].set_score(self.goal_pos)
                    if self.dots[i].score > 10:
                        break
                    self.dots[i].move(np.array([self.calculate_random_vector(self.x_move_stats[j]), self.calculate_random_vector(self.y_move_stats[j])]), self.movement_size)
                while 0 <= self.dots[i].pos[0] <= x_bound and 0 <= self.dots[i].pos[1] <= y_bound and self.dots[i].num_moves < self.shortest_success:
                    self.dots[i].set_score(self.goal_pos)
                    if self.dots[i].score > 10:
                        self.shortest_success = min(self.dots[i].num_moves, self.shortest_success)
                        break
                    self.dots[i].move(np.random.randn(2), self.movement_size)
                self.dots[i].set_score(self.goal_pos)
            total_scores += self.dots[i].score
        print(total_scores/self.size)

    def set_stats(self):
        x_sums = []
        x_sums_2 = []
        y_sums = []
        y_sums_2 = []
        score_totals = []
        for dot in self.dots:
            j = 0
            for j in range(min(len(x_sums), len(dot.all_v), self.shortest_success)):
                x_sums[j] += dot.score*dot.all_v[j][0]
                y_sums[j] += dot.score*dot.all_v[j][1]
                x_sums_2[j] += dot.score*dot.all_v[j][0]*dot.all_v[j][0]
                y_sums_2[j] += dot.score*dot.all_v[j][1]*dot.all_v[j][1]
                score_totals[j].append(dot.score)
            for k in range(j, min(len(dot.all_v), self.shortest_success)):
                x_sums.append(dot.score*dot.all_v[k][0])
                y_sums.append(dot.score*dot.all_v[k][1])
                x_sums_2.append(dot.score*dot.all_v[k][0]*dot.all_v[k][0])
                y_sums_2.append(dot.score*dot.all_v[k][1]*dot.all_v[k][1])
                score_totals.append([dot.score])
        self.x_move_stats = []
        self.y_move_stats = []
        for i in range(len(score_totals)):
            self.x_move_stats.append([x_sums[i]/sum(score_totals[i]), x_sums_2[i] - x_sums[i]*x_sums[i]])
            self.y_move_stats.append([y_sums[i]/sum(score_totals[i]), y_sums_2[i] - y_sums[i]*y_sums[i]])