import unittest
import modules.path

maze = [["#","#","#",0,"#"],
        ["#",5,"#",1,"#"],
        ["#",4,3,2,"#"],
        ["#",5,"#","#","#"],
        ["#","E","#","#","#"]]

model_result = [['#', '#', '#', 'S', '#'], 
                ['#', " ", '#', 'R', '#'], 
                ['#', 'R', 'R', 'R', '#'], 
                ['#', 'R', '#', '#', '#'], 
                ['#', 'E', '#', '#', '#']]

class TestPath(unittest.TestCase):
    def setUp(self):
        self.path = modules.path.Path()
    
    def test_path_writing(self):
        routed_maze = self.path.mark_straightest_path(maze,[3,1])
        self.assertEqual(routed_maze, model_result)