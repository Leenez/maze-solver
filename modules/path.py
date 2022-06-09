class Path:
    """Draws a path through the maze and cleans it to user readable form."""

    def mark_start_and_clean(self, _maze):
        """Marks start position as S and removes all integers."""
        for row in range(len(_maze)):
            for column in range(len(_maze[row])):
                if _maze[row][column] == 0:
                    _maze[row][column] = "S"
                elif isinstance(_maze[row][column], int):
                    _maze[row][column] = " "


    def mark_straightest_path(self, _maze, current_position):
        """Draws the most straight path through the maze using R characters."""
        start_index = _maze[current_position[0]][current_position[1]]
        _maze[current_position[0]][current_position[1]] = "R"

        for step in range(start_index):
            for index in [-1,1]:
                if _maze[current_position[0]+index][current_position[1]] == start_index -step:
                    current_position = [current_position[0]+index, current_position[1]]
                    _maze[current_position[0]][current_position[1]] = "R"
                    
                if _maze[current_position[0]][current_position[1]+index] == start_index -step:
                    current_position = [current_position[0], current_position[1]+index]
                    _maze[current_position[0]][current_position[1]] = "R"
        
        self.mark_start_and_clean(_maze)
        return _maze