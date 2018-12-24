import numpy as np
from generation import Generation
from dot import Dot
from graphics import *

boundaries = np.array([100, 100])
# win = GraphWin('window', width=boundaries[0], height=boundaries[1])
goal_pos = np.array([75, 75])
# goal = Circle(Point(goal_pos[0], goal_pos[1]), 25)
# goal.draw(win)


starting_pos = np.array([25.0,25.0])

generation_size = 100
vector_length = 1
test_gen = Generation(starting_pos, goal_pos, generation_size, vector_length)

num_generations = 1000
for i in range(num_generations):
    # for dot in test_gen.dots:
    #     point = Circle(Point(dot.pos[0], dot.pos[1]), 5)
    #     point.draw(win)
    test_gen.do_moves(boundaries)
    test_gen.set_stats()
    # time.sleep(10)

# win.getMouse() # Pause to view result
# win.close()    # Close window when done
