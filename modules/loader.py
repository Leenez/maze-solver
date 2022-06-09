class Loader:
    """Loads and validates maze file to be solved."""

    def validate_maze(self, _maze):
        """Validates characters and a singular start position in the maze file."""
        num_of_start_pos = 0
        for line in _maze:
            for char in line:
                if char not in ['#',' ','E','^']:
                    raise Exception("Maze can only contain following characters: #, ' ', E, ^")
                if char == '^':
                    num_of_start_pos += 1
        if num_of_start_pos != 1:
            raise Exception("Maze must have one start position")

    def load_maze(self, maze_file):
        def split(string):
            return [char for char in string]

        with open(maze_file, 'r') as maze_file:
            _maze = [split(line.strip()) for line in maze_file.readlines()]
        try:
            self.validate_maze(_maze)
        except Exception as e:
            print(str(e))
            quit()
        return _maze