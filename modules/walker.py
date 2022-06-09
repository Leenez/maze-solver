import copy

class Walker:
    """Prints a message indicating if there are no solution within allowed number of steps or if the solution is found."""

    def find_and_init_start_position(self, _maze):
        """Writes integer 0 to the start position."""
        for row_index in range(len(_maze)):
            for column_index in range(len(_maze[row_index])):
                if _maze[row_index][column_index] == "^":
                    _maze[row_index][column_index] = 0
                    return [row_index, column_index]


    def first_step(self, _maze, start):
        """Ensures the first step is taken inside the maze."""
        if start[0] == len(_maze)-1:
            _maze[len(_maze)-2][start[1]] = 1
            return 1, [len(_maze)-2, start[1]]
        elif start[0] == 0:
            _maze[1][start[1]] = 1
            return 1, [1, start[1]]
        elif start[1] == len(_maze[start[0]])-1:
            _maze[start[0]][start[1]-1] = 1
            return 1, [start[0], start[1]-1]
        elif start[1] == 0:
            _maze[start[0]][start[1]+1] = 1
            return 1, [start[0], start[1]+1]
        return 0, start


    def update_steps(self, _maze, last_positions, step_index, step_limit):
        """Attempts BFS algorithm to find a solution within allowed number of steps."""
        newpositions = []
        if step_index == step_limit:
            return False, step_index

        for position in last_positions:
            for index in [-1, 1]:
                if _maze[position[0]+index][position[1]] == ' ':
                    _maze[position[0]+index][position[1]] = step_index + 1
                    newpositions.append([position[0]+index, position[1]])
                elif _maze[position[0]+index][position[1]] == "E":
                    return position, _maze

                if _maze[position[0]][position[1]+index] == ' ':
                    _maze[position[0]][position[1]+index] = step_index + 1
                    newpositions.append([position[0], position[1]+index])
                elif _maze[position[0]][position[1]+index] == "E":
                    return position, _maze
        return self.update_steps(_maze, newpositions, step_index + 1, step_limit)


    def walk_maze(self, _maze, step_limit):
        """Returns a solution or in case of no solution a step_limit."""
        start_position = self.find_and_init_start_position(_maze)
        first_step_index, updated_start_pos = self.first_step(_maze, start_position)
        return self.update_steps(_maze, [updated_start_pos], first_step_index, step_limit)
    
    def walk_allowed_steps(self, _maze, allowed_steps):
        """Uses an array of allowed step limits to check if a solution can be found within the limits."""
        for steps in allowed_steps:
            data = self.walk_maze(copy.deepcopy(_maze), steps)
            if data[0] == False:
                print("No solution in", data[1], "steps")
            else:
                return data
        quit()
