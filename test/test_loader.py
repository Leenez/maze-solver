import unittest
import modules.loader

maze_bad_char = [["#","X","#"],["#"," ","#"],["#","^","#"]]
maze_no_start = [["#","#","#"],["#"," ","#"],["#","E","#"]]

class TestLoader(unittest.TestCase):
    def setUp(self):
        self.loader = modules.loader.Loader()

    def test_characters(self):
        error = "Maze can only contain following characters: #, ' ', E, ^"
        try:
            self.loader.validate_maze(maze_bad_char)
        except Exception as e:
            self.assertEqual(error, str(e))        

    def test_start_position(self):
        error = "Maze must have one start position"
        try:
            self.loader.validate_maze(maze_no_start)
            print(maze_no_start)
        except Exception as e:
            self.assertEqual(error, str(e))

    def test_valid_maze_loads(self):
        try:
            self.loader.load_maze("data/maze1.txt")
        except Exception:
            self.fail("Must not raise exception")
        