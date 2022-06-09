import sys
import modules.loader
import modules.walker
import modules.path
import modules.writer
                
def main():
    loader = modules.loader.Loader()
    walker = modules.walker.Walker()
    path = modules.path.Path()
    writer = modules.writer.Writer()

    maze = loader.load_maze(sys.argv[1])
    solution = walker.walk_allowed_steps(maze, [20, 150, 200])
    walked_maze = path.mark_straightest_path(solution[1], solution[0])
    writer.maze_to_text_file(walked_maze, "solution.txt")
   
if __name__ == '__main__':
    main()