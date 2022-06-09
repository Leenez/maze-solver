import unittest
import modules.walker

maze_start = [["#","^","#","#"],["#"," "," ","#"],["#","#"," ","#"],["#","#","E","#"]]
maze_first_step_1 = [["#",0,"#","#"],["#"," "," ","#"],["#"," "," ","#"],["#","#","E","#"]]
maze_first_step_2 = [["#","#","#","#"],["#",0," ","#"],["#","#"," ","#"],["#","#","E","#"]]
maze_walk_1 = [["#",0,"#","#"],["#",1," ","#"],["#","#"," ","#"],["#","#","E","#"]]
maze_walk_2 = [["#",0,"#","#"],["#",1," ","#"],["#","#"," ","#"],["#","#","E","#"]]

class TestWalker(unittest.TestCase):
    def setUp(self):
        self.walker = modules.walker.Walker()

    def test_start_position(self):
        row, column = self.walker.find_and_init_start_position(maze_start)
        self.assertEqual(0, row)
        self.assertEqual(1, column)
        self.assertEqual(0, maze_start[0][1])        

    def test_first_step(self):
        index_1, location_1 = self.walker.first_step(maze_first_step_1, [0,1])
        index_2, location_2 = self.walker.first_step(maze_first_step_2, [1,1])
        self.assertEqual(1, index_1)
        self.assertEqual([1,1], location_1)
        self.assertEqual(0, index_2)
        self.assertEqual([1,1], location_2)

    def test_walking(self):
        position_1, maze_1 = self.walker.update_steps(maze_walk_1, [[1,1]], 1, 4)
        self.assertEqual([2,2], position_1)
        self.assertEqual([['#', 0, '#', '#'], ['#', 1, 2, '#'], ['#', '#', 3, '#'], ['#', '#', 'E', '#']], maze_1)
        position_2, maze_2 = self.walker.update_steps(maze_walk_1, [[1,1]], 1, 2)
        self.assertEqual(False, position_2)
        self.assertEqual(2, maze_2)

    # TODO: Test for step limit