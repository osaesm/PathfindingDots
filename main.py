import numpy as np

from generation import Generation
from dot import Dot
from graphics import *

boundaries = np.array([1000, 1000])
win = GraphWin('window', width=boundaries[0], height=boundaries[1])
goal_pos = np.array([750, 750])
goal = Circle(Point(goal_pos[0], goal_pos[1]), 15)
goal.draw(win)


starting_pos = np.array([25.0,25.0])

generation_size = 100
vector_length = 5
num_survivors = 10

i = 0
test_gen = Generation(starting_pos, goal_pos, generation_size, vector_length, num_survivors)
while test_gen.do_moves(boundaries) is None:
    for dot in test_gen.prev_bests[1:]:
        point = Circle(Point(dot.pos[0], dot.pos[1]), 5)
        # point.setOutline('red')
        point.setFill('black')
        point.draw(win)
    point = Circle(Point(test_gen.prev_bests[0].pos[0], test_gen.prev_bests[0].pos[1]), 5)
    point.setFill('green')
    point.setOutline('green')
    point.draw(win)

print(test_gen.dots[0].num_moves)
win.getMouse() # Pause to view result
win.close()    # Close window when done
