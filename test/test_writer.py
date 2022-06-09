# TODO: Test for writer
"""from unittest.mock import patch, mock_open
import unittest
import modules.writer

maze = [["#","#"],["^","#"]]

class TestWriter(unittest.TestCase):
    def setUp(self):
        self.writer = modules.writer.Writer()

    def test_writer(self):
        open_mock = mock_open()
        with patch("writer.open", open_mock, create=True):
            self.writer.maze_to_text_file(maze)"""